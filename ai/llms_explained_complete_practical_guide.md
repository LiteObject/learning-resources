# LLMs Explained: A Practical Guide for Engineers

> Rewritten and extended from [LiteObject/learning-resources – LLMs Explained](https://github.com/LiteObject/learning-resources/blob/main/ai/llms_explained_complete_practical_guide.md).
> **What's new in this version:** top-k explained alongside top-p (with runnable code), a full section on parameter-efficient fine-tuning (LoRA, QLoRA), a deeper quantization section (what gets quantized, memory math, quality trade-offs), a corrected picture of epochs in LLM pre-training, and runnable API examples instead of pseudocode.

---

## Contents

1. [What an LLM is](#1-what-an-llm-is)
2. [What "large" means](#2-what-large-means)
3. [Tokens](#3-tokens)
4. [How text gets generated](#4-how-text-gets-generated)
5. [The Transformer and attention](#5-the-transformer-and-attention)
6. [How LLMs are trained](#6-how-llms-are-trained)
7. [Training vocabulary](#7-training-vocabulary)
8. [Fine-tuning in practice: LoRA, QLoRA and other PEFT methods](#8-fine-tuning-in-practice-lora-qlora-and-other-peft-methods)
9. [Prompting vs. RAG vs. fine-tuning](#9-prompting-vs-rag-vs-fine-tuning)
10. [Inference and decoding: temperature, top-k, top-p](#10-inference-and-decoding-temperature-top-k-top-p)
11. [Quantization](#11-quantization)
12. [Context windows and memory](#12-context-windows-and-memory)
13. [Hallucinations](#13-hallucinations)
14. [LLMs vs. traditional ML](#14-llms-vs-traditional-ml)
15. [Model types](#15-model-types)
16. [Building LLM applications](#16-building-llm-applications)
17. [Evaluation](#17-evaluation)
18. [Risks and controls](#18-risks-and-controls)
19. [The ecosystem](#19-the-ecosystem)
20. [Calling an LLM from code](#20-calling-an-llm-from-code)
21. [Learning roadmap](#21-learning-roadmap)
22. [Interview questions](#22-interview-questions)
23. [Exercises](#23-exercises)
24. [Cheat sheet](#24-cheat-sheet)

---

## 1. What an LLM is

A large language model (LLM) is a neural network trained on very large amounts of text (and often code) to model language. Mechanically, it does one thing: given a sequence of tokens, it outputs a probability distribution over what token comes next. Everything else — chat, summarization, code generation, translation — is built by repeating that step.

A useful mental model is "extremely capable autocomplete." It is a weak mental model in one important way: an LLM is **not a database**. It doesn't look up a stored, verified answer. It generates text that is statistically plausible given its training and the context you give it. Fluent output can still be wrong.

## 2. What "large" means

"Large" refers to several things at once:

| Dimension | Meaning |
|---|---|
| Parameters | The learned numerical weights inside the model (billions in modern LLMs). |
| Training data | Trillions of tokens of text and code for frontier-scale models. |
| Compute | The GPU/TPU time needed to train, measured in FLOPs. |
| Context window | How many tokens the model can consider in a single request. |

More parameters do not automatically mean a better model. Data quality, architecture, training recipe, alignment and the inference setup all matter. A well-trained smaller model regularly beats a poorly trained larger one.

Parameters are not a table of facts. Knowledge is distributed across them in ways that aren't directly readable or editable.

## 3. Tokens

Models don't see characters or words; they see **tokens** — chunks produced by a tokenizer. A token may be a whole word, part of a word, punctuation, whitespace or a symbol.

```
raw text → tokenizer → token IDs → model → output token IDs → detokenizer → text
```

For example, `"Data analytics is powerful!"` might split into `["Data", " analytics", " is", " powerful", "!"]`, but the exact split depends on the tokenizer, and different model families use different ones.

Why tokens matter in practice:

- **Context limits** are measured in tokens, not words or pages.
- **API pricing** is usually per input token and per output token (output often costs more).
- **Latency** grows with prompt length and, especially, output length.
- **Code, numbers, rare names and non-English text** often use more tokens per word than ordinary English. A common rule of thumb for English prose is roughly ¾ of a word per token, but treat it as a rough estimate only.

## 4. How text gets generated

Most widely used LLMs are **decoder-only Transformers** that generate **autoregressively**: one token at a time, each conditioned on everything before it.

1. **Prompt** — system instructions, conversation history, retrieved documents and user input.
2. **Tokenize** — convert to token IDs.
3. **Embed** — map each ID to a vector, plus positional information.
4. **Transformer layers** — repeated attention and feed-forward blocks refine those vectors.
5. **Logits** — the final layer produces a score for every token in the vocabulary.
6. **Decode** — turn scores into probabilities and choose one token (see [Section 10](#10-inference-and-decoding-temperature-top-k-top-p)).
7. **Append and repeat** — the chosen token is added to the sequence and the loop runs again.
8. **Stop** — at an end-of-sequence token, a stop sequence, or the max output limit.

To avoid recomputing everything each step, inference engines keep a **KV cache** — the attention keys and values for tokens already processed. The KV cache is a big reason long contexts consume so much GPU memory.

## 5. The Transformer and attention

The Transformer was introduced in the 2017 paper *Attention Is All You Need* (Vaswani et al.). Its core idea is **self-attention**: every token builds a context-aware representation by weighing every other token it is allowed to see.

Example: in "I went to the bank to deposit a check," attention lets the representation of *bank* be shaped by *deposit* and *check*, pushing it toward the financial meaning. (Attention patterns are learned numbers, not human-readable rules — this example is only an intuition.)

**Queries, keys and values.** Each token's vector is projected three ways using learned weight matrices:

| Projection | Intuition |
|---|---|
| Query (Q) | "What am I looking for?" |
| Key (K) | "What do I contain?" |
| Value (V) | "What information do I pass along if selected?" |

**Scaled dot-product attention:**

```
Attention(Q, K, V) = softmax( Q·Kᵀ / √d_k ) · V
```

- `Q·Kᵀ` scores how relevant each token is to each other token.
- Dividing by `√d_k` (the key dimension) keeps scores from growing too large, which would push softmax into near-one-hot outputs with tiny gradients.
- `softmax` turns scores into weights that sum to 1.
- The weights take a weighted average of the value vectors.
- In decoder-only models a **causal mask** stops each token from attending to tokens after it.

**Multi-head attention** runs several attention operations in parallel, each with its own projections, so different heads can specialize (syntax, coreference, position, and so on). Their outputs are concatenated and projected back.

**The rest of the block.** Each layer also has a feed-forward network, residual connections and normalization, which together make deep stacks trainable.

**Position.** Attention by itself has no sense of word order, so models add positional information — learned or sinusoidal embeddings in early models, rotary position embeddings (RoPE) and similar methods in most current ones.

## 6. How LLMs are trained

Training means adjusting parameters to reduce a loss. Modern chat models typically go through three broad stages, though recipes vary by provider.

### Stage 1: Pre-training

The model learns general language and world patterns from a huge corpus. For decoder-only models the objective is **next-token prediction**:

```
context: "The capital of France is"   →   target: " Paris"
```

The loss (cross-entropy) measures how much probability the model gave the correct next token; an optimizer nudges the parameters to raise it. This is the expensive stage — by far the most compute.

Other architectures use other objectives (for example, masked-token prediction for encoder models like BERT), so next-token prediction is common but not universal.

**How many epochs?** Classic ML often trains for many epochs. LLM pre-training usually doesn't: frontier models typically see their corpus about once, or less, with higher-quality sources (curated web, code, books) upsampled so they appear a few times. Repeating the whole corpus many times wastes compute and encourages memorization. For a sense of scale, the "Chinchilla" study (Hoffmann et al., 2022) found compute-optimal training at roughly 20 tokens per parameter; many current models are deliberately trained well beyond that to make them cheaper to serve.

### Stage 2: Supervised fine-tuning (SFT)

The model is trained on curated prompt/response pairs so it follows instructions and answers in a useful format.

```
prompt:   "Explain a SQL LEFT JOIN to a beginner."
response: "A LEFT JOIN returns every row from the left table, plus matching rows from the right table..."
```

SFT datasets are tiny compared with pre-training data and typically run for 1–3 epochs.

### Stage 3: Preference alignment

The model is tuned toward responses people (or a trained judge) prefer — more helpful, honest and safe. Common approaches:

- **RLHF** — collect human rankings of candidate responses, train a reward model on them, then optimize the LLM against the reward model with reinforcement learning (classically PPO).
- **DPO** (Direct Preference Optimization, 2023) and related methods — skip the separate reward model and train directly on preferred/rejected pairs. Simpler and widely used.
- **AI feedback** — preferences or critiques generated by a model following written principles, used alongside or instead of human labels.

Many recent models also add reinforcement learning on tasks with checkable answers (math, code with tests) to strengthen step-by-step reasoning.

## 7. Training vocabulary

| Term | Meaning |
|---|---|
| Epoch | One full pass over the training dataset. (LLM pre-training often runs for ~1 epoch or less — see Section 6.) |
| Batch | The examples processed together in one training step. |
| Learning rate | How big each parameter update is. |
| Loss | A number measuring prediction error; training tries to reduce it. |
| Gradient descent | Updating parameters in the direction that reduces loss. Real training uses variants such as AdamW. |
| Backpropagation | The algorithm that computes the gradient of the loss for every parameter. |
| Fine-tuning | Further training an existing model for a task, style or behavior. |
| Overfitting | Fitting the training data so closely that the model performs worse on new data. |
| Inference | Running a trained model to produce output. |

## 8. Fine-tuning in practice: LoRA, QLoRA and other PEFT methods

**Full fine-tuning** updates every parameter. For a large model that means storing gradients and optimizer state for billions of weights — many times the memory of the model itself — and saving a full new copy of the model for every task. For most teams that is impractical.

**Parameter-efficient fine-tuning (PEFT)** freezes the base model and trains only a small number of new parameters. It is how most practical fine-tuning is done today.

### LoRA (Low-Rank Adaptation)

Introduced by Hu et al. (2021). The idea: the change a fine-tune makes to a weight matrix can be approximated by a low-rank matrix.

For a frozen weight matrix `W` (size d × k), LoRA learns two small matrices:

```
W' = W + (α / r) · B·A        where  B is d × r,  A is r × k,  r ≪ min(d, k)
```

- `r` (rank) is typically 8–64. `α` is a scaling factor.
- `B` starts at zero, so training begins from exactly the base model's behavior.
- LoRA is usually applied to the attention projections (Q, K, V, output) and often the feed-forward layers.
- **Scale of savings:** for a 4096 × 4096 matrix (~16.8M weights), rank 8 trains only 2 × 4096 × 8 ≈ 65K weights — about 0.4%.

Practical benefits:

- Much less GPU memory, because there are no gradients or optimizer state for the frozen weights.
- Adapter files are megabytes, not gigabytes. You can keep one base model and swap adapters per task or customer.
- Adapters can be merged into the base weights for deployment, adding no inference latency.

### QLoRA

Dettmers et al. (2023). QLoRA combines LoRA with quantization: the frozen base model is stored in **4-bit** precision (a format called NF4), while the LoRA adapters train in 16-bit. It also uses double quantization and paged optimizers to save more memory. The paper fine-tuned a 65B-parameter model on a single 48 GB GPU with quality close to 16-bit fine-tuning. QLoRA is a common way to fine-tune open-weight models on a single workstation or cloud GPU.

### Other PEFT methods

| Method | What is trained |
|---|---|
| Adapters | Small bottleneck layers inserted inside each Transformer block. |
| Prefix / prompt tuning | Learned "virtual token" vectors prepended to the input or to each layer. |
| DoRA and other LoRA variants | Refinements that split weights into magnitude and direction, or vary rank by layer. |

### When to fine-tune at all

Fine-tune for **behavior**: a consistent output format, a house style, a narrow classification task, or a smaller model imitating a larger one. Don't fine-tune to add **facts** that change — use retrieval (RAG) instead. Try prompting first; fine-tune when prompting plateaus and you have a few hundred to a few thousand high-quality examples plus an evaluation set to prove the improvement.

Tools: Hugging Face `peft` and `trl`, Unsloth, Axolotl, and managed fine-tuning offered by several model providers.

## 9. Prompting vs. RAG vs. fine-tuning

| Approach | What changes | Best for |
|---|---|---|
| Prompting | Instructions and examples at request time; no weights change. | Fast iteration, most tasks. |
| RAG | Relevant documents retrieved and inserted into the prompt; no weights change. | Private, current or frequently changing knowledge; citations. |
| Fine-tuning (full or PEFT) | Model weights (or adapter weights). | Consistent format/style, specialized behavior, smaller/cheaper models. |
| Pre-training | Everything, from scratch. | Building a foundation model — rarely the right call for an application team. |

Example — a policy assistant:

- **Prompting:** "Answer in plain language and cite the policy section."
- **RAG:** retrieve the latest approved policy text and include it in the prompt.
- **Fine-tuning:** only if, after prompting and RAG, answers still don't follow the required structure and you have labeled examples.

These combine: a fine-tuned model can still use RAG and good prompts.

## 10. Inference and decoding: temperature, top-k, top-p

**Inference** is running the trained model. Useful terms:

| Term | Meaning |
|---|---|
| Input / output tokens | What you send / what the model generates; both are billed and both affect latency. |
| Latency | Time to first token and time to complete. |
| Throughput | Tokens or requests served per second. |
| Streaming | Sending tokens to the user as they are generated. |
| Batch inference | Processing many requests together, often cheaper, for non-interactive jobs. |

### Decoding strategies

At each step the model produces **logits** — one score per vocabulary token. Decoding decides which token to emit.

- **Greedy decoding:** always take the highest-probability token. Deterministic, but can be repetitive.
- **Temperature (T):** divide logits by T before softmax.
  - T < 1 sharpens the distribution toward the top tokens (more focused, more repeatable).
  - T > 1 flattens it (more varied, more surprising, more errors).
  - T = 0 is usually treated as greedy.
- **Top-k:** keep only the **k** most probable tokens, set all others to zero, renormalize, then sample. With k = 1 this is greedy. The weakness: k is fixed, so it keeps too many tokens when the model is confident and too few when many continuations are reasonable.
- **Top-p (nucleus sampling):** keep the **smallest set of tokens whose cumulative probability reaches p** (for example 0.9), renormalize, then sample. The candidate set grows or shrinks with the model's confidence, which is why top-p is often preferred over top-k.
- **Min-p** and others: newer variants, such as keeping tokens whose probability is at least a fraction of the top token's. Available controls differ by provider and engine.

Typical order: apply temperature, then top-k and/or top-p, then sample. Implementations differ, and some providers recommend adjusting temperature *or* top-p, not both.

**None of these settings makes output more factual.** Low temperature makes a model consistently say the same thing — including the same wrong thing.

### Runnable demo

Requires only NumPy (`pip install numpy`).

```python
import numpy as np

def sample_next_token(logits, temperature=1.0, top_k=None, top_p=None, rng=None):
    """Pick one token ID from raw logits using temperature, top-k and top-p."""
    rng = rng or np.random.default_rng()
    logits = np.asarray(logits, dtype=np.float64)

    if temperature == 0:                      # greedy decoding
        return int(np.argmax(logits))

    logits = logits / temperature             # 1. temperature
    probs = np.exp(logits - logits.max())
    probs /= probs.sum()

    if top_k is not None:                     # 2. top-k: keep the k most likely tokens
        cutoff = np.sort(probs)[-top_k]
        probs = np.where(probs >= cutoff, probs, 0.0)
        probs /= probs.sum()

    if top_p is not None:                     # 3. top-p: smallest set reaching p
        order = np.argsort(probs)[::-1]
        cumulative = np.cumsum(probs[order])
        keep = order[: np.searchsorted(cumulative, top_p) + 1]
        mask = np.zeros_like(probs)
        mask[keep] = 1.0
        probs = probs * mask
        probs /= probs.sum()

    return int(rng.choice(len(probs), p=probs))

vocab = ["Paris", "Lyon", "the", "a", "France"]
logits = [5.0, 2.5, 2.0, 1.0, 0.5]
rng = np.random.default_rng(0)
for settings in [dict(temperature=0), dict(temperature=1.0),
                 dict(temperature=1.0, top_k=2), dict(temperature=1.5, top_p=0.9)]:
    picks = [vocab[sample_next_token(logits, rng=rng, **settings)] for _ in range(1000)]
    counts = {w: picks.count(w) for w in vocab if picks.count(w)}
    print(settings, counts)
```

Output (1,000 samples each):

```
{'temperature': 0} {'Paris': 1000}
{'temperature': 1.0} {'Paris': 864, 'Lyon': 69, 'the': 39, 'a': 17, 'France': 11}
{'temperature': 1.0, 'top_k': 2} {'Paris': 925, 'Lyon': 75}
{'temperature': 1.5, 'top_p': 0.9} {'Paris': 759, 'Lyon': 144, 'the': 97}
```

Notice how top-k = 2 cuts off the long tail completely, while a higher temperature with top-p = 0.9 spreads probability across three candidates.

## 11. Quantization

**Quantization** stores numbers at lower precision to cut memory and, often, speed up inference.

### Memory math

Weight memory ≈ parameters × bytes per parameter:

| Precision | Bytes / param | 7B model | 70B model |
|---|---|---|---|
| FP32 | 4 | ~28 GB | ~280 GB |
| FP16 / BF16 | 2 | ~14 GB | ~140 GB |
| INT8 / FP8 | 1 | ~7 GB | ~70 GB |
| 4-bit | 0.5 | ~3.5 GB | ~35 GB |

Add memory for the KV cache (grows with context length and concurrent users) and runtime overhead. Most models are trained and served in BF16/FP16 as the baseline.

### What can be quantized

- **Weights only** (most common, e.g., "W4A16"): weights stored in 4 or 8 bits, computation done in 16-bit. Saves memory; speeds up generation because decoding is usually limited by memory bandwidth.
- **Weights and activations** (e.g., "W8A8", FP8): both in low precision so the math itself runs on faster low-precision hardware units. Bigger speedups on supported GPUs, harder to do without losing accuracy.
- **KV cache:** storing cached keys/values in 8-bit or lower to fit longer contexts or more concurrent requests.

### How it's done

- **Post-training quantization (PTQ):** quantize a finished model, often using a small calibration dataset. Common methods/formats: GPTQ, AWQ, bitsandbytes, and GGUF (used by llama.cpp and Ollama).
- **Quantization-aware training (QAT):** simulate low precision during training so the model learns to tolerate it. Better quality at very low bit widths, but needs training.

### Quality trade-offs

Quantization is lossy. As a rough guide:

- **8-bit** is usually close to the original on most benchmarks.
- **4-bit** is a popular sweet spot for local and cost-sensitive deployment, with a small but measurable quality drop.
- **Below 4-bit** degrades quickly for most models.

Losses aren't uniform: math, code, long-context reasoning and non-English tasks often suffer more than general chat, and smaller models tend to be more sensitive than larger ones. **Always evaluate a quantized model on your own task** rather than relying on generic benchmark numbers.

## 12. Context windows and memory

The **context window** is everything the model can consider in one request: system prompt, conversation history, retrieved documents, tool results, the user's message — and the output it is generating.

- It is **not persistent memory.** Once a conversation exceeds the window, older content must be dropped or summarized.
- **Persistent memory** is a product feature: the application stores facts separately and inserts relevant ones into future prompts. It can be viewed, updated or deleted.
- A long context window doesn't guarantee the model uses everything well. Retrieval accuracy can drop for information buried in the middle of very long inputs, and long prompts cost more and run slower. Put the most important instructions and evidence where the model will reliably attend to them, and test.

## 13. Hallucinations

A **hallucination** is output that sounds plausible but is false, unsupported or invented — a fake citation, a non-existent SQL column, a made-up statistic.

Common causes:

- The information isn't in the training data or the provided context.
- The prompt is ambiguous.
- The model is optimized to produce a plausible continuation, not to say "I don't know."
- The fact is obscure or newer than the training data.
- Retrieved context is missing, irrelevant or misleading.

Ways to reduce them:

1. Ground answers in trusted sources (RAG).
2. Require citations and check them.
3. Use tools — calculators, SQL, code execution — for exact work.
4. Validate structured output against schemas and business rules.
5. Instruct the model to say when evidence is insufficient, and reward that behavior in evaluation.
6. Keep a human in the loop for high-stakes decisions.
7. Measure hallucination rates with an evaluation set.

No technique eliminates hallucinations completely.

## 14. LLMs vs. traditional ML

| | Traditional ML | LLMs |
|---|---|---|
| Typical input | Structured/tabular features | Unstructured text, code, images |
| Typical output | A label, score or number | Generated text |
| Training | Task-specific, from your labeled data | Pre-trained generally, then adapted |
| Evaluation | Accuracy, precision, recall, RMSE | Rubrics, human review, task-specific tests |

LLMs are not automatically the right choice. For tabular prediction (churn, fraud scores, demand forecasting), gradient-boosted trees are often more accurate, cheaper, faster and easier to explain.

## 15. Model types

| Type | Description | Typical use |
|---|---|---|
| Foundation model | Broadly pre-trained, adaptable to many tasks. | Base for most applications. |
| Decoder-only (GPT-style) | Autoregressive generation. | Chat, code, general generation. |
| Encoder-only (BERT-style) | Bidirectional understanding; no free-form generation. | Classification, embeddings, search. |
| Encoder-decoder (T5-style) | Encodes input, then generates output. | Translation, summarization. |
| Small language model (SLM) | Fewer parameters; cheaper, can run on-device. | Narrow tasks, edge deployment. |
| Multimodal | Handles more than one modality (text, images, audio). | Document understanding, vision Q&A. |
| Mixture of experts (MoE) | Routes each token through a subset of "expert" layers, so only part of the model is active per token. | Large-capacity models with lower per-token compute. |
| Open-weight | Weights downloadable under a license. | Self-hosting, fine-tuning. |

"Open-weight" doesn't necessarily mean open training data, open code or unrestricted commercial use — read the license.

## 16. Building LLM applications

### Common business uses

- **Text-to-SQL:** "Show monthly transaction volume for 2026." Always review generated SQL for joins, filters, date logic, permissions and metric definitions; run it with read-only credentials.
- **Feedback analysis:** categorize comments, extract products and issues, summarize themes. Validate against a human-labeled sample.
- **Document extraction:** pull fields (invoice number, date, amount, currency) into JSON. Valid JSON can still contain wrong values — check against business rules.
- **Report drafting:** the LLM writes the narrative; **numbers come from SQL or a trusted data layer**, never from the model.
- **Knowledge assistants:** RAG over policies, procedures, documentation and FAQs, with citations.

### Reference architecture

```
User → App (authn/authz) → Prompt builder → [Retrieval, permission-filtered] → LLM
     → Output validation & safety checks → Response with sources → Logging & monitoring
```

Production also needs: privacy controls, logging policy, rate limits, cost monitoring, timeouts and retries, fallbacks, and a path to escalate to a human.

## 17. Evaluation

Evaluate along several dimensions: **correctness, relevance, faithfulness** (does the answer stick to the provided sources?), **instruction following, safety, robustness, latency and cost**.

Methods:

- Human review against a written rubric.
- A fixed test set with expected outputs, run on every change (regression testing).
- Automated checks for structured fields.
- Retrieval metrics such as Recall@K for RAG.
- Pairwise comparison of models or prompts.
- LLM-as-judge for scale — calibrated against human labels, since judges have their own biases.
- Production monitoring.

**Perplexity** measures how well a model predicts held-out text (lower = higher probability assigned to the actual tokens). It is useful for comparing language models but says little about usefulness, factuality, safety or chat quality.

## 18. Risks and controls

| Risk | Control |
|---|---|
| Hallucination | Grounding, citations, validation, human review. |
| Sensitive data exposure | Approved tools only, data minimization, redaction, access controls. |
| Prompt injection | Treat retrieved and user content as untrusted; least-privilege tools; confirm risky actions. |
| Bias | Test across groups; review outputs; document limitations. |
| Insecure generated code | Code review, static analysis, tests, dependency scanning. |
| Cost overruns | Token budgets, caching, smaller models where sufficient, monitoring. |
| Over-reliance | Training, clear UI signals, human accountability for decisions. |

Never paste confidential customer data, credentials or regulated data into AI services your organization hasn't approved.

## 19. The ecosystem

| Category | Examples |
|---|---|
| Model providers (API) | OpenAI, Anthropic, Google |
| Open-weight model families | Llama, Qwen, Mistral, Gemma, DeepSeek |
| Model hub | Hugging Face |
| Orchestration | LangChain, LlamaIndex |
| Fine-tuning | Hugging Face `peft`/`trl`, Unsloth, Axolotl |
| Inference engines | vLLM, llama.cpp, Ollama, TGI |
| Evaluation | lm-evaluation-harness, RAGAS |

This landscape changes quickly; check current documentation before choosing.

## 20. Calling an LLM from code

Both examples below run as written once the prerequisites are installed. Model names change frequently, so both read the model from an environment variable — check your provider's current model list. Never hard-code API keys; use environment variables or a secrets manager.

### Hosted API (Anthropic Python SDK)

```bash
pip install anthropic
export ANTHROPIC_API_KEY="..."          # from your provider console
export LLM_MODEL="<a current model ID from the provider's docs>"
```

```python
import os
import anthropic

client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY from the environment

message = client.messages.create(
    model=os.environ["LLM_MODEL"],
    max_tokens=500,
    system="You are a patient SQL tutor. Keep answers under 150 words.",
    messages=[{"role": "user", "content": "Explain a SQL INNER JOIN with a short example."}],
)

print(message.content[0].text)
print("Input tokens:", message.usage.input_tokens, "| Output tokens:", message.usage.output_tokens)
```

The OpenAI SDK follows the same pattern (`client.chat.completions.create(...)`, reading `response.choices[0].message.content`).

### Local open-weight model (Ollama)

Runs entirely on your machine — no API key, no data leaves the laptop. Install Ollama from ollama.com, then:

```bash
ollama pull llama3.2        # a small open-weight model, pre-quantized to ~4-bit
pip install ollama
```

```python
import ollama

response = ollama.chat(
    model="llama3.2",
    messages=[{"role": "user", "content": "Explain a SQL INNER JOIN with a short example."}],
    options={"temperature": 0.2, "top_k": 40, "top_p": 0.9},
)

print(response["message"]["content"])
```

Try changing `temperature`, `top_k` and `top_p` and compare outputs (see [Section 10](#10-inference-and-decoding-temperature-top-k-top-p)).

## 21. Learning roadmap

| Stage | Focus | Mini-project |
|---|---|---|
| 1. Foundations | Tokens, attention, training stages, decoding | Run the sampling demo; tokenize text with a real tokenizer and compare languages |
| 2. Prompting | Instructions, examples, structured output | Build a prompt that extracts invoice fields to JSON reliably |
| 3. APIs | SDKs, streaming, token usage, error handling | A CLI tool that summarizes a file and reports token cost |
| 4. Retrieval | Embeddings, chunking, vector search, citations | A RAG Q&A bot over a folder of internal docs |
| 5. Fine-tuning | LoRA/QLoRA, dataset prep, overfitting | QLoRA fine-tune of a small open model for a classification task |
| 6. Evaluation | Test sets, rubrics, LLM-as-judge | An eval harness comparing two prompts or a base vs. fine-tuned model |
| 7. Deployment | Quantization, serving, monitoring, security | Serve a 4-bit model with Ollama or vLLM and measure latency/quality vs. 16-bit |

## 22. Interview questions

1. **What is an LLM?** A neural network trained on large text corpora to predict the next token; chat and other abilities emerge from repeating that step.
2. **What is a token?** The unit a tokenizer splits text into — a word, sub-word, punctuation or symbol.
3. **What are parameters?** The learned weights of the model; not a lookup table of facts.
4. **What is a Transformer?** A neural architecture built on self-attention, feed-forward layers, residual connections and normalization.
5. **What does self-attention do?** Lets each token weigh the other tokens to build a context-aware representation.
6. **Why divide by √d_k?** To keep dot products from growing with dimension, which would saturate softmax and shrink gradients.
7. **What is next-token prediction?** The pre-training objective of decoder-only models: maximize the probability of the actual next token.
8. **Temperature vs. top-k vs. top-p?** Temperature reshapes the whole distribution; top-k keeps a fixed number of top tokens; top-p keeps the smallest set reaching a cumulative probability, so its size adapts to the model's confidence.
9. **What is LoRA?** A PEFT method that freezes the base weights and learns a low-rank update `B·A` for selected matrices, training well under 1% of parameters.
10. **What does QLoRA add?** A 4-bit quantized frozen base model with 16-bit LoRA adapters, cutting memory enough to fine-tune large models on one GPU.
11. **What is quantization, and what does it cost?** Storing weights (and sometimes activations or KV cache) at lower precision to save memory and speed up inference, with some — usually small at 8-bit, larger at 4-bit and below — quality loss.
12. **Why do LLMs often train for only about one epoch?** Corpora are so large that one pass already uses huge compute, and repeated passes add memorization risk with diminishing returns; high-quality subsets are upsampled instead.
13. **RAG vs. fine-tuning?** RAG supplies knowledge at request time without changing weights (good for changing facts); fine-tuning changes weights (good for behavior and format).
14. **What is a hallucination?** Plausible but unsupported or false output.
15. **Do more parameters always mean better results?** No — data, training, alignment and inference setup matter as much.
16. **When shouldn't you use an LLM?** Deterministic calculations, strict database operations, simple rules, and tabular prediction where traditional ML is cheaper and more reliable.

## 23. Exercises

1. Explain the difference between tokens and parameters in two sentences.
2. Draw the generation loop from prompt to stop condition, including the KV cache.
3. Describe Q, K and V in your own words.
4. Modify the sampling demo to add min-p sampling and compare its output.
5. With a fixed distribution, find a `top_k` and a `top_p` that keep the same tokens, then change the distribution and explain why they diverge.
6. Compute the LoRA trainable-parameter count for a 4096 × 11008 matrix at ranks 8, 16 and 64.
7. Estimate the GPU memory needed to serve a 13B model in BF16, INT8 and 4-bit.
8. Extract fields from a sample invoice to JSON and list five validation checks.
9. Build a 20-item test set for complaint classification and a rubric covering correctness, relevance and completeness.
10. Design a safe text-to-SQL workflow, including permissions and review.

## 24. Cheat sheet

| Term | One-line definition |
|---|---|
| LLM | Neural network that predicts the next token, trained on large text corpora. |
| Token | Unit of text the model reads and writes. |
| Parameter | A learned weight in the model. |
| Embedding | A vector representing a token (or text) numerically. |
| Transformer | Architecture built on self-attention. |
| Self-attention | Each token weighs other tokens to build context. |
| KV cache | Stored keys/values that avoid recomputation during generation. |
| Pre-training | Large-scale next-token training; often ~1 epoch over the corpus. |
| SFT | Fine-tuning on curated prompt/response pairs. |
| RLHF / DPO | Aligning a model to human preferences. |
| LoRA | Train a small low-rank update; freeze the base model. |
| QLoRA | LoRA on top of a 4-bit quantized base model. |
| Quantization | Lower-precision weights/activations/KV cache; saves memory, costs some quality. |
| Prompting | Instructions at request time; no weight changes. |
| RAG | Retrieve documents and add them to the prompt. |
| Inference | Running a trained model. |
| Context window | Max tokens per request, including output. |
| Temperature | Sharpens (<1) or flattens (>1) the token distribution. |
| Top-k | Sample from the k most likely tokens. |
| Top-p | Sample from the smallest set reaching cumulative probability p. |
| Hallucination | Plausible but unsupported output. |
| Evaluation | Measuring correctness, faithfulness, safety, latency and cost. |

**Key takeaway:** an LLM is a powerful language-generation component, not a source of truth. Reliable systems pair it with trusted data, validation, evaluation, security controls and human judgment.