import argparse
import json
import unittest
from collections import Counter
from pathlib import Path

from evaluation import test as eval_data
from evaluation.test import EVAL_DIR, dataset_path

KB_DIR = Path(__file__).parent.parent / "knowledge-base"


class DatasetSelectionTests(unittest.TestCase):
    def tearDown(self):
        eval_data.select_dataset(argparse.Namespace(stress=False, dataset="tests"))

    def test_default_is_initial_dataset(self):
        self.assertEqual(dataset_path(), EVAL_DIR / "tests.jsonl")

    def test_stress_flag_selects_stress_dataset(self):
        parser = argparse.ArgumentParser()
        eval_data.add_dataset_args(parser)
        eval_data.select_dataset(parser.parse_args(["--stress"]))
        tests = eval_data.load_tests()
        self.assertEqual(len(tests), 54)
        self.assertEqual(set(Counter(t.category for t in tests).values()), {3})


class StressManifestTests(unittest.TestCase):
    def test_manifest_files_exist_in_knowledge_base(self):
        manifest = json.loads(
            (EVAL_DIR / "stress_kb_manifest.json").read_text(encoding="utf-8")
        )
        missing = [
            f["path"] for f in manifest["files"] if not (KB_DIR / f["path"]).is_file()
        ]
        self.assertEqual(missing, [])


if __name__ == "__main__":
    unittest.main()
