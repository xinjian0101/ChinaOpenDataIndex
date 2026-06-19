from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path


REQUIRED_FIELDS = ("id", "name_zh", "name_en", "publisher", "category", "license")
CATEGORY_VALUES = {
    "economy",
    "education",
    "environment",
    "health",
    "population",
    "public-services",
    "science",
    "transport",
    "urban",
    "other",
}
STATUS_VALUES = {"draft", "reviewed", "needs-update", "historical", "replacement"}


def validate_entry(entry: dict) -> list[str]:
    return [field for field in REQUIRED_FIELDS if not entry.get(field)]


def validate_entry_details(entry: dict) -> list[dict]:
    issues = [{"field": field, "type": "missing"} for field in validate_entry(entry)]
    identifier = entry.get("id")
    if identifier is not None and (not isinstance(identifier, str) or not identifier.strip()):
        issues.append({"field": "id", "type": "invalid"})
    category = entry.get("category")
    if category and category not in CATEGORY_VALUES:
        issues.append({"field": "category", "type": "unknown_value", "value": category})
    status = entry.get("status")
    if status and status not in STATUS_VALUES:
        issues.append({"field": "status", "type": "unknown_value", "value": status})
    if status == "replacement" and not entry.get("replacement_id"):
        issues.append({"field": "replacement_id", "type": "required_for_replacement"})
    tags = entry.get("tags")
    if tags is not None:
        if not isinstance(tags, list) or any(not isinstance(tag, str) or not tag.strip() for tag in tags):
            issues.append({"field": "tags", "type": "invalid"})
        elif len(tags) != len(set(tags)):
            issues.append({"field": "tags", "type": "duplicate_value"})
    return issues


def load_catalog(path: str) -> list[dict]:
    rows: list[dict] = []
    for line_number, line in enumerate(Path(path).read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            item = json.loads(line)
        except json.JSONDecodeError as exc:
            raise ValueError(f"Invalid JSON at line {line_number}: {exc}") from exc
        if not isinstance(item, dict):
            raise ValueError(f"Line {line_number} is not an object")
        item["_line"] = line_number
        item["_missing"] = validate_entry(item)
        item["_issues"] = validate_entry_details(item)
        rows.append(item)

    counts = Counter(item.get("id") for item in rows if item.get("id"))
    for item in rows:
        identifier = item.get("id")
        if identifier and counts[identifier] > 1:
            item["_issues"].append({"field": "id", "type": "duplicate_value", "value": identifier})
    return rows


def search(
    rows: list[dict],
    query: str = "",
    category: str | None = None,
    status: str | None = None,
    valid_only: bool = False,
) -> list[dict]:
    query_lower = query.lower()
    result = []
    for item in rows:
        text = " ".join(
            str(item.get(key, ""))
            for key in ("name_zh", "name_en", "publisher", "category", "description_zh", "description_en", "tags")
        ).lower()
        if query_lower and query_lower not in text:
            continue
        if category and item.get("category") != category:
            continue
        if status and item.get("status") != status:
            continue
        if valid_only and item.get("_issues"):
            continue
        result.append(item)
    return result


def catalog_summary(rows: list[dict]) -> dict:
    categories = Counter(item.get("category", "missing") for item in rows)
    statuses = Counter(item.get("status", "unspecified") for item in rows)
    invalid = sum(bool(item.get("_issues")) for item in rows)
    return {
        "records": len(rows),
        "valid_records": len(rows) - invalid,
        "invalid_records": invalid,
        "categories": dict(sorted(categories.items())),
        "statuses": dict(sorted(statuses.items())),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Search and validate a metadata catalog.")
    parser.add_argument("catalog")
    parser.add_argument("--query", default="")
    parser.add_argument("--category")
    parser.add_argument("--status")
    parser.add_argument("--valid-only", action="store_true")
    parser.add_argument("--summary", action="store_true")
    args = parser.parse_args()
    rows = load_catalog(args.catalog)
    result = catalog_summary(rows) if args.summary else search(rows, args.query, args.category, args.status, args.valid_only)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
