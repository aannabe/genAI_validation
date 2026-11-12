# GenAI Model Validation

GenAI model (Chatbot with RAG) and synthetic data from Ed Donner's LLM Engineering Course
[LINK]
The following folders / files are taken from there:

knowledge-base
implementation
evaluation
evaluator.py
app.py

We have a golden source of truth dataset in evaluation/tests.jsonl (Typically provided by developers or subject-matter-experts)
Here is it is artifically built with an LLM.

The LLM in the GenAI model is OpenAI GPT-Luna. The LLM-as-a-judge uses the same LLM.
This is likely OK, as we give the judge golden source of truth (answers).
However, it is generally recommended to use another, bigger LLM for judge, to avoid bias.

Steps:
* uv run python implementation/ingest.py (embed chunks as vectors)
* uv run python evaluator.py (run RAG and Answer quality evaluations)
* uv run python app.py (GUI for chatting)
