# ChinaOpenDataIndex

ChinaOpenDataIndex is a bilingual metadata validator and search tool for open-data catalogs published by Chinese public institutions and related organizations. The repository stores metadata records only; it does not download or redistribute source datasets.

> Status: metadata-focused MVP. Structural validation does not prove that a source is current, official, or reusable for a particular purpose.

## Use cases

- Build a bilingual index of public-data catalogs
- Validate metadata records before import or publication
- Search by keyword or exact category
- Track publisher, category, declared license, source page, and review date
- Prepare a reviewable source inventory for downstream data projects

## Current capabilities

- Validate stable record identifiers
- Require Chinese-title and English-title fields
- Require publisher, category, and declared-license metadata
- Read one JSON object per line
- Search across record values
- Filter by exact category
- Report missing required fields
- Run locally with no paid API

## Requirements

- Python 3.10 or newer

## Search by keyword

```bash
python main.py examples/catalog.jsonl --query transport
```

## Filter by category

```bash
python main.py examples/catalog.jsonl --category environment
```

## Run tests

```bash
python tests.py
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
  "access_type": "download",
  "formats": ["csv", "json"],
  "language": ["zh-CN"],
  "last_verified": "2026-06-19",
  "status": "draft",
  "notes": "Synthetic metadata example"
}
```

The example domain is intentionally non-operational. Real records should preserve verifiable source evidence and review dates.

## Metadata principles

- **Metadata only**: do not copy source datasets into this repository.
- **Evidence based**: preserve the publisher-controlled source page when available.
- **Faithful naming**: English titles should describe the source without adding unsupported claims.
- **License aware**: keep declared labels separate from review conclusions.
- **Versioned**: record meaningful changes to availability, schema, and source terms.
- **Reviewable**: preserve review dates, status changes, and replacement identifiers.

## Verification workflow

1. Open the publisher-controlled source page.
2. Confirm the title and publisher.
3. Record the source URL and access method.
4. Record the displayed license or terms label exactly.
5. Confirm that the repository record contains metadata only.
6. Add the review date and status.
7. Recheck periodically because links and terms can change.

## Search behavior

Keyword search is intended for discovery rather than semantic ranking. Exact-category filtering depends on a controlled category vocabulary. Add one primary category and use tags for secondary topics.

## Known limitations

- Passing structural validation does not verify source authenticity or reuse rights.
- The tool does not download source datasets.
- The tool does not inspect changing website terms automatically.
- Source-title translation may require human review.
- Search does not rank synonyms or related concepts.

## Documentation

- [Record Format](docs/RECORD_FORMAT.md)
- [Contribution Process](docs/CONTRIBUTING_RECORDS.md)
- [Category Vocabulary](docs/CATEGORY_VOCABULARY.md)
- [Source Verification](docs/SOURCE_VERIFICATION.md)
- [Source Acceptance Policy](docs/SOURCE_ACCEPTANCE.md)
- [Maintenance Trace](MAINTENANCE_TRACE.md)

## License

MIT
