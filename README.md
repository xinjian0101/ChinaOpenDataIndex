# ChinaOpenDataIndex

A bilingual metadata validator and search tool for Chinese open-data catalogs.

中文定位：面向中国公开数据目录的中英双语元数据索引、校验与检索工具。项目只保存数据集元数据，不抓取或重新分发原始数据内容。

> Current status: metadata-focused MVP. A catalog entry is not automatically verified merely because it passes structural validation.

## Use cases

- Build a bilingual index of Chinese government and institutional open-data catalogs
- Validate catalog records before publishing or importing them
- Search metadata by keyword or exact category
- Track publisher, category, license, and source evidence
- Prepare a reviewable source inventory for downstream dataset projects

## Current capabilities

- Validate dataset IDs
- Validate Chinese and English names
- Require publisher, category, and license metadata
- Read one JSON object per line
- Search by keyword
- Filter by exact category
- Store metadata only
- Run locally without a paid API

## Quick start

### Requirements

- Python 3.10 or newer

### Search by keyword

```bash
python main.py catalog.jsonl --query transit
```

### Filter by category

```bash
python main.py catalog.jsonl --category transport
```

### Run tests

```bash
python tests.py
```

## Required fields

| Field | Type | Description |
|---|---|---|
| `id` | string | Stable catalog record identifier |
| `name_zh` | string | Chinese dataset name |
| `name_en` | string | English dataset name |
| `publisher` | string | Publishing organization |
| `category` | string | Normalized category |
| `license` | string | Declared license or access term |

## Recommended extended fields

```json
{
  "id": "city-transport-001",
  "name_zh": "公共交通线路元数据",
  "name_en": "Public Transit Route Metadata",
  "publisher": "Example Municipal Data Office",
  "category": "transport",
  "license": "review-required",
  "source_url": "https://example.invalid/catalog/001",
  "access_type": "download",
  "formats": ["csv", "json"],
  "language": ["zh-CN"],
  "updated_at": "2026-06-01",
  "verified_at": null,
  "verification_status": "unverified",
  "notes": "Metadata example only"
}
```

The example domain is intentionally non-operational. Real records should preserve verifiable source evidence and review dates.

## Metadata principles

- **Metadata only**: do not copy restricted source data into this repository.
- **Evidence-based**: preserve the official catalog URL and review date.
- **Bilingual but faithful**: English names should describe the source accurately, not add unsupported claims.
- **License-aware**: distinguish declared terms from independently verified reuse rights.
- **Versioned**: record meaningful changes to source availability, schema, and terms.
- **Privacy-conscious**: avoid cataloging datasets that expose personal information without a clear lawful basis.

## Recommended verification workflow

1. Open the official publisher or catalog page.
2. Confirm the dataset title and publisher.
3. Record the source URL and access method.
4. Review the stated license, terms, attribution, and redistribution conditions.
5. Confirm that the record contains metadata only.
6. Mark the verification date and reviewer status.
7. Recheck periodically because links and terms may change.

## Search behavior

Keyword search is intended for discovery, not semantic ranking. Exact-category filtering depends on a consistent category vocabulary. Contributors should normalize categories before adding records rather than creating near-duplicate labels.

## Known limitations

- Passing validation does not prove that a source is official, available, current, or commercially reusable.
- The tool does not download source datasets.
- The tool does not automatically inspect changing website terms.
- English names may require human translation review.
- License compatibility and database rights require separate analysis.
- Search is intentionally lightweight and may not rank synonyms or related concepts.

## Documentation

- [Record format](docs/RECORD_FORMAT.md)
- [Contribution process](docs/CONTRIBUTING_RECORDS.md)
- [Category vocabulary](docs/CATEGORY_VOCABULARY.md)
- [Source verification](docs/SOURCE_VERIFICATION.md)
- [Source Acceptance Policy](docs/SOURCE_ACCEPTANCE.md)
- [Maintenance Trace](MAINTENANCE_TRACE.md)

## Maintenance cycle 3

The third portfolio maintenance cycle strengthens documentation discoverability and prepares the catalog for explicit lifecycle, review-template, and retirement-policy records. Changes remain visible as independent Git commits.

## License

MIT
