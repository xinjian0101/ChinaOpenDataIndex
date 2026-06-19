# ChinaOpenDataIndex

ChinaOpenDataIndex is a bilingual metadata validator and search tool for open-data catalogs published by Chinese public institutions and related organizations. The repository stores metadata records only; it does not download or redistribute source datasets.

> Status: metadata-focused MVP. Structural validation does not prove that a source is current, official, or reusable for a particular purpose.

## Use cases

- Build a bilingual index of public-data catalogs
- Validate metadata records before import or publication
- Search by keyword, category, or lifecycle status
- Track publisher, category, declared license, source page, and review date
- Detect duplicate record identifiers and malformed lifecycle metadata
- Produce a catalog-level summary before publication

## Current capabilities

- Validate stable record identifiers
- Require Chinese-title and English-title fields
- Require publisher, category, and declared-license metadata
- Validate controlled category and status values
- Require a replacement target for replacement records
- Detect duplicate identifiers and duplicate tags
- Read one JSON object per line
- Search across titles, descriptions, publisher, category, and tags
- Filter by category, status, and validation result
- Summarize category counts, status counts, and invalid records
- Run locally with no paid API

## Requirements

- Python 3.10 or newer

## Search examples

```bash
python main.py examples/catalog.jsonl --query transport
python main.py examples/catalog.jsonl --category environment
python main.py examples/catalog.jsonl --status reviewed
python main.py examples/catalog.jsonl --valid-only
```

## Catalog summary

```bash
python main.py examples/catalog.jsonl --summary
```

Example output:

```json
{
  "records": 2,
  "valid_records": 2,
  "invalid_records": 0,
  "categories": {
    "environment": 1,
    "transport": 1
  },
  "statuses": {
    "unspecified": 2
  }
}
```

## Run tests

```bash
python -m unittest -v
```

## Required fields

| Field | Type | Description |
|---|---|---|
| `id` | string | stable catalog record identifier |
| `name_zh` | string | source title in the Chinese-title field |
| `name_en` | string | English display title |
| `publisher` | string | publishing organization |
| `category` | string | normalized category identifier |
| `license` | string | declared license or access label |

Field names such as `name_zh` remain part of the public metadata contract. Repository prose and demonstration values are maintained in English.

## Extended record example

```json
{
  "id": "city-transport-001",
  "name_zh": "Example source title for the Chinese-title field",
  "name_en": "Public Transit Route Metadata",
  "publisher": "Example Municipal Data Office",
  "category": "transport",
  "license": "review-required",
  "source_url": "https://example.invalid/catalog/001",
  "formats": ["csv", "json"],
  "last_verified": "2026-06-19",
  "status": "draft",
  "tags": ["transport", "routes"],
  "notes": "Synthetic metadata example"
}
```

The example domain is intentionally non-operational. Real records should preserve verifiable source evidence and review dates.

## Controlled values

Categories are defined in `docs/CATEGORY_VOCABULARY.md`.

Supported lifecycle values:

- `draft`
- `reviewed`
- `needs-update`
- `historical`
- `replacement`

A record with `status: replacement` must provide `replacement_id`.

## Metadata principles

- **Metadata only**: do not copy source datasets into this repository.
- **Evidence based**: preserve the publisher-controlled source page when available.
- **Faithful naming**: English titles should describe the source without adding unsupported claims.
- **License aware**: keep declared labels separate from review conclusions.
- **Versioned**: record meaningful changes to availability, schema, and source terms.
- **Reviewable**: preserve review dates, status changes, and replacement identifiers.

## Known limitations

- Passing structural validation does not verify source authenticity or reuse rights.
- The tool does not download source datasets.
- The tool does not inspect changing website terms automatically.
- Search is substring based rather than semantic.
- Controlled vocabularies are maintained in code and documentation rather than loaded dynamically.

## Documentation

- [Record Format](docs/RECORD_FORMAT.md)
- [Contribution Process](docs/CONTRIBUTING_RECORDS.md)
- [Category Vocabulary](docs/CATEGORY_VOCABULARY.md)
- [Source Verification](docs/SOURCE_VERIFICATION.md)
- [Source Acceptance Policy](docs/SOURCE_ACCEPTANCE.md)
- [Maintenance Trace](MAINTENANCE_TRACE.md)

## License

MIT
