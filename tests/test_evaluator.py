import os
import sys
import tempfile
import types
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

evaluation_module = types.ModuleType("evaluation.eval")
evaluation_module.evaluate_all_retrieval = lambda: iter(())
evaluation_module.evaluate_all_answers = lambda: iter(())
with patch.dict(sys.modules, {"evaluation.eval": evaluation_module}):
    import evaluator
sys.modules["evaluator"] = evaluator


class EvaluatorLogTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.original_directory = Path.cwd()
        os.chdir(self.temp_dir.name)

    def tearDown(self):
        os.chdir(self.original_directory)
        self.temp_dir.cleanup()

    def test_retrieval_evaluation_writes_case_results_and_summary(self):
        test = SimpleNamespace(
            question="Where is the office?",
            keywords=["Seattle"],
            reference_answer="Seattle",
            category="direct_fact",
        )
        result = SimpleNamespace(
            mrr=1.0,
            ndcg=1.0,
            keywords_found=1,
            total_keywords=1,
            keyword_coverage=100.0,
        )
        Path("eval_RAG.log").write_text("old results", encoding="utf-8")
        with patch.object(
            evaluator,
            "evaluate_all_retrieval",
            return_value=iter([(test, result, 1.0)]),
        ):
            evaluator.run_retrieval_evaluation(progress=lambda *args, **kwargs: None)

        log = Path("eval_RAG.log").read_text(encoding="utf-8")
        self.assertNotIn("old results", log)
        self.assertIn("Question: Where is the office?", log)
        self.assertIn("Keywords found: 1/1", log)
        self.assertIn("Average MRR: 1.0000", log)

    def test_answer_evaluation_writes_case_results_and_summary(self):
        test = SimpleNamespace(
            question="Where is the office?",
            keywords=["Seattle"],
            reference_answer="Seattle",
            category="direct_fact",
        )
        result = SimpleNamespace(
            feedback="The answer is accurate.",
            accuracy=5.0,
            completeness=4.0,
            relevance=5.0,
        )
        Path("eval_Answer.log").write_text("old results", encoding="utf-8")
        with patch.object(
            evaluator,
            "evaluate_all_answers",
            return_value=iter([(test, result, 1.0)]),
        ):
            evaluator.run_answer_evaluation(progress=lambda *args, **kwargs: None)

        log = Path("eval_Answer.log").read_text(encoding="utf-8")
        self.assertNotIn("old results", log)
        self.assertIn("Question: Where is the office?", log)
        self.assertIn("Feedback: The answer is accurate.", log)
        self.assertIn("Average accuracy: 5.00/5", log)


if __name__ == "__main__":
    unittest.main()
