from __future__ import annotations

import argparse
import json
from pathlib import Path

REQUIRED_FIELDS = ("id", "name_zh", "name_en", "publisher", "category", "license")


def validate_entry(entry: dict) -> list[str]:
    return [field for field in REQUIRED_FIELDS if not entry.get(field)]


def load_catalog(path: str) -> list[dict]:
    rows = []
    for line_number, line in enumerate(Path(path).read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        item = json.loads(line)
        item["_line"] = line_number
        item["_missing"] = validate_entry(item)
        rows.append(item)
    return rows


def search(rows: list[dict], query: str = "", category: str | None = None) -> list[dict]:
    query_lower = query.lower()
    result = []
    for item in rows:
        text = " ".join(str(item.get(key, "")) for key in ("name_zh", "name_en", "publisher", "category")).lower()
        if query_lower and query_lower not in text:
            continue
        if category and item.get("category") != category:
            continue
        result.append(item)
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("catalog")
    parser.add_argument("--query", default="")
    parser.add_argument("--category")
    args = parser.parse_args()
    print(json.dumps(search(load_catalog(args.catalog), args.query, args.category), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
