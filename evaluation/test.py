import argparse
import json
from pathlib import Path
from pydantic import BaseModel, Field

EVAL_DIR = Path(__file__).parent
DEFAULT_DATASET = "tests"
_selected_dataset = DEFAULT_DATASET


def dataset_path(dataset: str | None = None) -> Path:
    """Resolve a dataset name (e.g. "tests", "stress") to its JSONL file.

    With no name, the dataset chosen by select_dataset() is used (default: "tests").
    """
    return EVAL_DIR / f"{dataset or _selected_dataset}.jsonl"


def log_name(base: str) -> str:
    """Log file name for the selected dataset: eval_RAG.log, or eval_RAG_stress.log, etc."""
    if _selected_dataset == DEFAULT_DATASET:
        return f"{base}.log"
    return f"{base}_{_selected_dataset}.log"


def add_dataset_args(parser: argparse.ArgumentParser) -> None:
    """Add the --dataset / --stress flags shared by the evaluation entry points."""
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--dataset", help="dataset name in evaluation/ (default: tests)")
    group.add_argument("--stress", action="store_true", help="shortcut for --dataset stress")


def select_dataset(args: argparse.Namespace) -> None:
    """Apply the dataset flags; with no flag the default dataset is kept."""
    global _selected_dataset
    if args.stress:
        _selected_dataset = "stress"
    elif args.dataset:
        _selected_dataset = args.dataset


class TestQuestion(BaseModel):
    """A test question with expected keywords and reference answer."""

    question: str = Field(description="The question to ask the RAG system")
    keywords: list[str] = Field(description="Keywords that must appear in retrieved context")
    reference_answer: str = Field(description="The reference answer for this question")
    category: str = Field(description="Question category (e.g., direct_fact, spanning, temporal)")


def load_tests(dataset: str | None = None) -> list[TestQuestion]:
    """Load test questions from the selected JSONL dataset."""
    tests = []
    with open(dataset_path(dataset), "r", encoding="utf-8") as f:
        for line in f:
            data = json.loads(line.strip())
            tests.append(TestQuestion(**data))
    return tests
