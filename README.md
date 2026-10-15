# Learning Resources

Notes, guides, and hands-on exercises for **software architecture** and **AI/ML** — organized as separate tracks so each has a clear audience and entry point.

## Repository map

| Folder | What it is | Start here if… |
| --- | --- | --- |
| [`software-architecture/`](./software-architecture/) | Deep-dive notes on system design: patterns, CQRS & event sourcing, distributed systems, TOGAF, high-throughput design | You design, review, or scale large systems |
| [`engineering-practices/`](./engineering-practices/) | Practical day-to-day notes: defensive coding, managing external libraries, writing good Jira stories | You want pragmatic coding- and team-practice advice |
| [`ai/`](./ai/) | All AI/ML material, organized as five tracks (see below) | You're learning AI from any level |
| [`book-notes/`](./book-notes/) | Summaries of books I've read (engineering + ML) | You want the gist of a book |

## The AI tracks

`ai/` deliberately contains separate tracks — pick by your goal:

| Track | Purpose | Audience |
| --- | --- | --- |
| [`ai/explained-simply/`](./ai/explained-simply/) | Plain-English introduction to AI/ML (no coding required) | Complete beginners, business professionals |
| [`ai/ml-curriculum/`](./ai/ml-curriculum/) | Structured ML curriculum: fundamentals → learning types → models & algorithms → advanced topics → deployment → AI types | Self-directed learners who want a full path |
| [`ai/engineering-notebook/`](./ai/engineering-notebook/) | AI **product engineering**: problem framing, data strategy, architecture, ethics, UX, cost — plus an interactive Jupyter notebook | Software engineers building AI systems |
| [`ai/llm-deep-dives/`](./ai/llm-deep-dives/) | Focused technical notes: attention, Flash Attention, LoRA, sampling, entropy, inference optimization | Practitioners needing quick, technical refreshers |
| [`ai/exercises/`](./ai/exercises/) | Hands-on practice: scikit-learn notebooks, sample exams, datasets | Anyone learning by doing |

## Suggested reading orders

**New to AI entirely**
1. [`ai/explained-simply/`](./ai/explained-simply/) — start with [Types of Machine Learning](./ai/explained-simply/fundamentals/types-of-machine-learning.md)
2. [`ai/ml-curriculum/`](./ai/ml-curriculum/) — follow the numbered sections in order
3. [`ai/engineering-notebook/`](./ai/engineering-notebook/) — when you're ready to build something, then dive into the [interactive notebook](./ai/engineering-notebook/AI-Engineering-Notebook.ipynb)
4. Use [`ai/exercises/`](./ai/exercises/) alongside

**Software engineer moving into AI**
1. [`ai/engineering-notebook/`](./ai/engineering-notebook/)
2. [`ai/llm-deep-dives/`](./ai/llm-deep-dives/) for the topics you actually deploy
3. [`ai/ml-curriculum/`](./ai/ml-curriculum/) to fill knowledge gaps

**Architecture refresher**
1. [`software-architecture/Essential_Design_Patterns.md`](./software-architecture/Essential_Design_Patterns.md)
2. [`CQRS.md`](./software-architecture/CQRS.md) + [`EVENT_SOURCING.md`](./software-architecture/EVENT_SOURCING.md)
3. [`DISTRIBUTED_SYSTEM.md`](./software-architecture/DISTRIBUTED_SYSTEM.md) + [`High_Throughput_Systems.md`](./software-architecture/High_Throughput_Systems.md)

## Housekeeping notes

- Older notes keep their original `Pascal_Case` filenames; newer notes use `kebab-case`. New files should prefer `kebab-case`.
- Known overlaps to reconcile later: the two attention notes and the two sampling notes in [`ai/llm-deep-dives/`](./ai/llm-deep-dives/).
- [`ai/engineering-notebook/README.md`](./ai/engineering-notebook/README.md) references a `LICENSE` file and an old clone URL that no longer apply — small cleanup pending.