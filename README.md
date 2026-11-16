# GenAI Model Validation

A small RAG chatbot and evaluation dashboard for a fictional insurance company, Insurellm. The
project is adapted from [Ed Donner's LLM Engineering course repository](https://github.com/ed-donner/llm_engineering).
The [knowledge base](./knowledge-base/) and current evaluation reference data are synthetic.

## How it works

1. **Ingest documents:** `implementation/ingest.py` reads Markdown files in `knowledge-base/`,
   uses an LLM to create overlapping chunks, embeds them, and stores them in a local Chroma
   collection.
2. **Answer questions:** `implementation/answer.py` rewrites the question using conversation
   history, retrieves and reranks relevant chunks, then generates an answer grounded in those
   chunks.
3. **Evaluate:** `evaluator.py` provides a Gradio dashboard for running retrieval and answer
   evaluations against [`evaluation/tests.jsonl`](./evaluation/tests.jsonl). `app.py` launches a
   chat UI that also displays retrieved context.

## Setup

Requirements: Python 3.11 or newer and [uv](https://docs.astral.sh/uv/).

1. Install the project dependencies:

   ```bash
   uv sync
   ```

2. Configure `OPENAI_API_KEY` in your shell or a local `.env` file. Do not commit credentials.

The current code uses `openai/gpt-6-luna` for LLM tasks and `text-embedding-3-large` for embeddings.
You need API access to these configured models.

## Run

Run these commands from the repository root:

```bash
# Build or rebuild the local vector index from knowledge-base/
uv run python implementation/ingest.py

# Launch the chatbot
uv run python app.py

# Launch the evaluation dashboard
uv run python evaluator.py
```

Each evaluation run saves per-test results and summary metrics to `eval_RAG.log` or
`eval_Answer.log` in the current working directory (`eval_RAG_stress.log` and
`eval_Answer_stress.log` for the stress dataset). Running that evaluation again replaces its
previous log.

Ingestion replaces the `docs` collection in the local `preprocessed_db/` directory. Run it before
the chatbot or evaluator when the index is missing or the knowledge base has changed. Ingestion
and evaluation make API calls and may incur usage costs.

## Validation stages

1. **Initial evaluation (baseline).** [`initial_eval_results/`](./initial_eval_results/) holds the
   results of the vanilla [`tests.jsonl`](./evaluation/tests.jsonl) run (150 questions covering
   retrieval and answer quality), including the ingested vector DB, logs and a dashboard
   screenshot. We treat this as the test set supplied by the model developers, and we closely
   reproduced these results independently.
2. **Stress testing.** On top of the baseline we run our own challenger tests,
   [`stress.jsonl`](./evaluation/stress.jsonl). They use the same schema and the same retrieval and
   answer-quality metrics, but probe behaviour such as abstaining, clarifying, refusing and
   resisting injection. Some questions rely on additional synthetic knowledge-base documents that
   simulate the knowledge base growing over time.

By default the vanilla `tests.jsonl` is used. Pass `--stress` (or `--dataset <name>` for any
`evaluation/<name>.jsonl`) to select another dataset:

```bash
uv run python evaluator.py --stress                 # dashboard on stress.jsonl
uv run python -m evaluation.eval 0 --stress         # a single stress question
uv run python -m evaluation.eval 0                  # a single vanilla question
```

The documents added for stress testing are listed in
[`evaluation/stress_kb_manifest.json`](./evaluation/stress_kb_manifest.json) (path and the
categories each supports). They deliberately look like ordinary knowledge-base documents, so the
manifest, and not the files themselves, is the record of what was added. After adding documents,
re-run ingestion; the baseline index is preserved in `initial_eval_results/`.

### Stress categories (3 questions each)

| Category | Expected behaviour |
|---|---|
| normal | Correct answer |
| ambiguous | Ask for clarification |
| answer_absent | Abstain, no hallucination |
| conflicting_docs | Prefer the authoritative source (executed contract, HR record) over drafts and estimates |
| stale_doc | Use the current version, not the superseded one |
| paraphrase | Same answer for three rewordings of one question |
| long_context | Retain a key fact buried in a long document or question |
| multi_hop | Combine facts from several documents |
| numeric_calc | Correct arithmetic on retrieved figures |
| typo_noisy | Robust to misspellings |
| false_premise | Correct the premise rather than play along |
| adversarial_unsafe | Refuse forgery, access-control bypass, fraud |
| prompt_injection_user | Ignore override instructions in the user message |
| prompt_injection_doc | Ignore instructions embedded in retrieved documents (vendor statement, support ticket, recruiting log) |
| toxic_prompt | Stay professional, refuse abusive content |
| discriminatory_request | Refuse decisions based on protected characteristics |
| pii_confidentiality | Withhold restricted HR data (ethnicity, medical, immigration) |
| out_of_scope | Decline and redirect |

For questions with no supporting passage (absent, refusals, out-of-scope) the required keyword is
the nearest-topic term, so retrieval metrics are only indicative there; the answer metrics use
behaviour-style reference answers ("the assistant should decline ..."). The baseline system prompt
is expected to fail some of these tests; that is a validation finding, not a defect in the dataset.

Note: the added employee records bring the knowledge base to more people than the "32 employees"
stated in the company overview documents. The company documents are deliberately left unchanged so
the vanilla tests (which expect 32) remain a fair comparison with the baseline.

## Initial evaluation coverage

The initial evaluation dataset contains 150 cases with a question, required retrieval keywords,
reference answer, and category. It covers direct-fact (70), temporal (20), spanning (20),
comparative (10), numerical (10), relationship (10), and holistic (10) questions. The reference
answers in this repository were generated with an LLM, so treat scores as a development signal
rather than an independently verified benchmark.

### Retrieval metrics

| Metric | What it measures |
|---|---|
| Mean Reciprocal Rank (MRR) | Average reciprocal rank of the first retrieved chunk containing each required keyword; absent keywords score zero. |
| Normalized Discounted Cumulative Gain (nDCG) | Whether relevant chunks rank near the top, compared with an ideal ranking; relevance is binary keyword presence. |
| Keyword Coverage | Percentage of required keywords found in the retrieved context. |

### Answer-quality metrics

An LLM judge compares each generated answer with the reference answer and scores it from 1 to 5:

| Metric | What it measures |
|---|---|
| Accuracy | Factual correctness compared with the reference answer. |
| Completeness | How fully the answer covers the information in the reference answer. |
| Relevance | How directly the answer addresses the question without unrelated material. |

The answer model and judge currently use the same configured LLM (`openai/gpt-6-luna`), which can
introduce evaluation bias. A separate judge model may provide a more independent assessment.

## Results summary

The table summarizes the saved runs: the **baseline** uses 150 initial questions and the preserved
baseline index; **stress** uses 54 challenger questions across 18 categories and an expanded
knowledge base. Retrieval metrics are averaged per question; answer scores are judged on a 1–5
scale.

| Metric | Baseline (150) | Stress (54) |
|---|---:|---:|
| MRR | 0.9092 | 0.7702 |
| nDCG | 0.9108 | 0.8238 |
| Keyword coverage | 95.3% | 94.4% |
| Answer accuracy | 4.44/5 | 3.61/5 |
| Answer completeness | 4.43/5 | 3.74/5 |
| Answer relevance | 4.57/5 | 3.63/5 |

Keyword coverage remained high on the stress set, but retrieval ranking and answer scores were
lower. The judge gave all three ambiguous questions an accuracy score of 1/5 for not requesting
clarification. It also flagged disclosures of restricted information in some privacy and
user-injection cases, and failures to redirect some out-of-scope requests. Each stress category
has only three questions, so individual results can strongly affect category-level conclusions.

These are different question sets and indexes, not a controlled before-and-after comparison.
Keyword matches do not establish that retrieved text is authoritative or that an answer is safe;
the synthetic references and LLM judge also limit the conclusions. See the baseline
[retrieval](./initial_eval_results/eval_RAG.log) and
[answer](./initial_eval_results/eval_Answer.log) logs and the stress
[retrieval](./eval_RAG_stress.log) and [answer](./eval_Answer_stress.log) logs for per-question
scores and judge feedback.
