import json
import tempfile
import unittest
from pathlib import Path

import main


class CatalogValidationTest(unittest.TestCase):
    def test_unknown_category_is_reported(self):
        issues = main.validate_entry_details({
            "id": "demo",
            "name_zh": "Example",
            "name_en": "Example",
            "publisher": "Publisher",
            "category": "unknown-category",
            "license": "review-required",
        })
        self.assertTrue(any(item["field"] == "category" for item in issues))

    def test_replacement_requires_target(self):
        issues = main.validate_entry_details({
            "id": "demo",
            "name_zh": "Example",
            "name_en": "Example",
            "publisher": "Publisher",
            "category": "transport",
            "license": "review-required",
            "status": "replacement",
        })
        self.assertTrue(any(item["field"] == "replacement_id" for item in issues))

    def test_duplicate_ids_and_summary(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "catalog.jsonl"
            record = {
                "id": "same",
                "name_zh": "Example",
                "name_en": "Example",
                "publisher": "Publisher",
                "category": "transport",
                "license": "review-required",
            }
            path.write_text(json.dumps(record) + "\n" + json.dumps(record) + "\n", encoding="utf-8")
            rows = main.load_catalog(str(path))
        summary = main.catalog_summary(rows)
        self.assertEqual(summary["records"], 2)
        self.assertEqual(summary["invalid_records"], 2)

    def test_valid_only_filter(self):
        rows = [
            {"name_en": "Valid", "category": "transport", "_issues": []},
            {"name_en": "Invalid", "category": "transport", "_issues": [{"type": "missing"}]},
        ]
        result = main.search(rows, valid_only=True)
        self.assertEqual([item["name_en"] for item in result], ["Valid"])


if __name__ == "__main__":
    unittest.main()
