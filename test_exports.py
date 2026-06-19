import csv
import json
import tempfile
import unittest
from pathlib import Path

import main


class CatalogExportTest(unittest.TestCase):
    def setUp(self):
        self.rows = [
            {
                "id": "demo-1",
                "name_zh": "Example title field",
                "name_en": "Example Dataset",
                "publisher": "Example Publisher",
                "category": "transport",
                "license": "review-required",
                "status": "reviewed",
                "tags": ["transport", "demo"],
                "_line": 1,
                "_missing": [],
                "_issues": [],
            }
        ]

    def test_export_entry_removes_internal_fields(self):
        exported = main.export_entry(self.rows[0])
        self.assertNotIn("_line", exported)
        self.assertNotIn("_issues", exported)
        self.assertEqual(exported["validation_status"], "valid")
        self.assertEqual(exported["issue_count"], 0)

    def test_json_output_is_clean(self):
        content = main.write_output(self.rows, None, "json")
        value = json.loads(content)
        self.assertEqual(value[0]["id"], "demo-1")
        self.assertNotIn("_line", value[0])

    def test_csv_output_flattens_tags(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "catalog.csv"
            main.write_output(self.rows, str(path), "csv")
            with path.open("r", encoding="utf-8", newline="") as handle:
                rows = list(csv.DictReader(handle))
        self.assertEqual(rows[0]["tags"], "transport;demo")
        self.assertEqual(rows[0]["validation_status"], "valid")

    def test_markdown_records(self):
        content = main.render_markdown(self.rows)
        self.assertIn("# Catalog Results", content)
        self.assertIn("Example Dataset", content)

    def test_markdown_summary_contains_issue_types(self):
        content = main.render_markdown({
            "records": 2,
            "valid_records": 1,
            "invalid_records": 1,
            "categories": {"transport": 2},
            "statuses": {"reviewed": 2},
            "issue_types": {"missing": 1},
        })
        self.assertIn("## Issue Types", content)
        self.assertIn("| missing | 1 |", content)

    def test_csv_summary_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "summary.csv"
            with self.assertRaises(ValueError):
                main.write_output({"records": 1}, str(path), "csv")


if __name__ == "__main__":
    unittest.main()
