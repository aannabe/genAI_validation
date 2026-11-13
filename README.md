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
`eval_Answer.log` in the current working directory. Running that evaluation again replaces its
previous log.

Ingestion replaces the `docs` collection in the local `preprocessed_db/` directory. Run it before
the chatbot or evaluator when the index is missing or the knowledge base has changed. Ingestion
and evaluation make API calls and may incur usage costs.

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
