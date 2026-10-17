# Understanding AI Memory

A structured summary of where an AI system's "memory" lives, how saved records reach an answer, and how to store, retrieve, and evaluate them.

## 1. Where information lives

| Location | Nature | What it holds | How it changes |
| --- | --- | --- | --- |
| **Learned weights** | Parametric knowledge | Knowledge and patterns distributed across model parameters. Ordinary inference does not update these weights. | Changed through training |
| **Active context** | Available to this model call | Instructions, recent messages, task state and retrieved evidence assembled into a finite input for the model. | Selected for each call |
| **Saved records** | External, persistent storage | Profiles, notes, past events and files kept outside the model. Relevant records can be loaded into later calls. | Written by the application |

> Common LLM systems shown here; some architectures also retain latent or recurrent state.

## 2. How saved memory reaches an answer

A common retrieval-based design:

**Current task** (question + scope)
→ **Retrieve records** (scope/ACL filter, search, rank)
→ **Assemble context** (instructions + state + evidence)
→ **Run the model** (learned weights + context)
→ **Answer / action** (use the selected evidence)

The loop closes after the answer via **task / result / feedback**, which feeds **select + validate writes**, then the **persistent record store**, which supplies later retrievals.

> Policy decides what to save; saving every message is not required.

## 3. Memory roles: what is retained?

| Role | Retains | Example |
| --- | --- | --- |
| **Semantic** | Facts + concepts | "Project Atlas uses PostgreSQL." |
| **Episodic** | Events + outcomes | "Yesterday's migration failed on a lock." |
| **Procedural** | Skills + instructions | "Check locks before retrying migration." |

- Working memory maintains active task state; selected contents become context for an LLM call.
- Roles can overlap; they do not specify a format or human-like cognition.

## 4. Saving a memory is a lifecycle

**Extract → Validate → Reconcile → Persist**

Example: a project-specific preference changes.

> "For Atlas, use JavaScript now."

Extracted record:

```text
scope: project/atlas      key: language
value: JavaScript         source: message-42
valid_from: 2026-10-11    supersedes: preference-7
```

- Resolve conflicting versions; keep history when needed.
- Set retention and deletion rules for records and indexes.

## 5. Context is a limited workspace

Everything supplied to a model call competes for a finite token budget.

**Rules · History · Evidence · Task / tools**

> Input allocation is schematic; also budget for generation.

| Move | Action |
| --- | --- |
| **Select** | Retrieve what this task needs. |
| **Compress** | Summarize older interaction. |
| **Preserve** | Keep source links and key details. |

> Summaries can lose important information.

## 6. KV cache: reuse computation

Attention keys and values for previously processed tokens are reused during autoregressive inference.

The diagram shows **previously cached** K and V blocks plus a **new token** block.

> Schematic: one layer, full-attention cache.

- The cache stores computational state, not a curated user profile. Reuse and eviction depend on the serving system.
- It does not update the model's weights.

## 7. RAG, memory and fine-tuning

| Mechanism | What it does |
| --- | --- |
| **RAG** | Retrieves external information to condition generation. |
| **Persistent memory** | Retains and updates information for later interactions. |
| **Fine-tuning** | Changes learned parameters through additional training. |

> These can work together: a memory system can use RAG to recall its records.

## 8. Storage and retrieval choices

A vector database is optional. Semantic memory ≠ semantic search.

| Option | Best for |
| --- | --- |
| **Files / JSON** | Notes, profiles, exact lookups |
| **SQL / filters** | Structured facts, dates, scope |
| **Vector search** | Candidates by embedding similarity |
| **Graphs** | Entities and relationships |

> Combine methods when useful. Similarity is not a truth or freshness score.

## 9. Why an assistant "forgets"

Trace the failure, stage by stage.

| Stage | What to check |
| --- | --- |
| **Never saved** | Check write policy and extraction. |
| **Saved, not found** | Inspect queries, filters and ranking. |
| **Found, not included** | Check context selection and budget. |
| **Included, misused** | Test reading and reasoning. |
| **Old fact returned** | Inspect timestamps and updates. |

> Stored ≠ retrieved ≠ used correctly

## 10. Measure useful recall

Test more than one remembered fact.

| Capability | What it exercises |
| --- | --- |
| **Extract** | Recover the requested detail. |
| **Connect** | Reason across multiple sessions. |
| **Order** | Resolve dates and event sequence. |
| **Update** | Use the fact valid for the question. |
| **Abstain** | Say when evidence is insufficient. |

- Track evidence recall, answer correctness, tokens and latency.
- Test scope isolation and resistance to poisoned records.

> Memory quality is an end-to-end property.

---
