<div align="center">

# ChinaOpenDataIndex

**Reviewable bilingual metadata catalogs for public-data discovery and source tracking.**

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Format](https://img.shields.io/badge/Catalog-JSONL-0969da)](docs/RECORD_FORMAT.md)
[![License](https://img.shields.io/badge/License-MIT-2ea44f)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active%20MVP-f59e0b)](MAINTENANCE_TRACE.md)

[Quick start](#quick-start) · [Validation](#validation-model) · [Exports](#export-formats) · [About](ABOUT.md) · [Source policy](docs/SOURCE_VERIFICATION.md)

</div>

---

ChinaOpenDataIndex is a metadata-only catalog validator and search tool for public-data sources connected to Chinese institutions and related organizations. It tracks titles, publishers, categories, declared terms, source pages, review status, and lifecycle changes without downloading or redistributing source datasets.

> [!IMPORTANT]
> Structural validation and a recorded license label do not prove that a source is official, current, or reusable for a particular purpose. Source evidence still requires human review.

## At a glance

| Area | Current support |
|---|---|
| Catalog format | JSONL |
| Metadata | Bilingual title fields, publisher, category, declared terms |
| Validation | Required fields, vocabularies, tags, replacement links |
| Integrity | Duplicate identifier detection |
| Search | Keyword, category, status, valid-only |
| Summary | Health counts, categories, statuses, issue types |
| Exports | Clean JSON, CSV, Markdown |
| Runtime | Python standard library |

## Quick start

Search the example catalog:

```bash
python main.py examples/catalog.jsonl --query transport
```

Show only reviewed and structurally valid entries:

```bash
python main.py examples/catalog.jsonl \
  --status reviewed \
  --valid-only
```

Generate a Markdown health report:

```bash
python main.py examples/catalog.jsonl \
  --summary \
  --format markdown \
  -o catalog-summary.md
```

Run tests:

```bash
python -m unittest -v
```

## Capability matrix

| Capability | Status | Notes |
|---|---:|---|
| Required metadata validation | ✅ | Six stable core fields |
| Controlled categories and statuses | ✅ | Defined in code and documentation |
| Duplicate ID detection | ✅ | Catalog-wide check |
| Clean export without internal fields | ✅ | JSON, CSV, Markdown |
| Source lifecycle tracking | ✅ | Draft, reviewed, needs-update, historical, replacement |
| Automatic source-page verification | ⏳ | Not implemented |
| Automatic reuse-rights decision | ❌ | Requires source review |

## Record example

```json
{
  "id": "city-transport-001",
  "name_zh": "Example source title field",
  "name_en": "Public Transit Route Metadata",
  "publisher": "Example Municipal Data Office",
  "category": "transport",
  "license": "review-required",
  "source_url": "https://example.invalid/catalog/001",
  "last_verified": "2026-06-20",
  "status": "draft",
  "tags": ["transport", "routes"]
}
```

Stable fields such as `name_zh` remain part of the metadata contract. Repository prose and synthetic example values are maintained in English.

## Validation model

| Check | Example failure |
|---|---|
| Required fields | Missing publisher or license label |
| Category vocabulary | Unknown category identifier |
| Lifecycle vocabulary | Unsupported status value |
| Replacement integrity | `replacement` without `replacement_id` |
| Tag structure | Empty or duplicate tags |
| Identifier integrity | Duplicate catalog IDs |

## Search and filters

```bash
python main.py catalog.jsonl --query climate
python main.py catalog.jsonl --category environment
python main.py catalog.jsonl --status needs-update
python main.py catalog.jsonl --valid-only
```

Filters can be combined in one command.

## Export formats

```bash
python main.py catalog.jsonl --format json -o catalog.json
python main.py catalog.jsonl --format csv -o catalog.csv
python main.py catalog.jsonl --format markdown -o catalog.md
```

Exported records remove internal implementation fields and add `validation_status`, `issue_count`, and reviewable issue details.

## Lifecycle values

| Status | Meaning |
|---|---|
| `draft` | Metadata has not completed review |
| `reviewed` | Core metadata was checked on the recorded date |
| `needs-update` | One or more fields require another review |
| `historical` | Retained for reference but not considered current |
| `replacement` | Superseded by another record |

## Repository map

| Path | Purpose |
|---|---|
| `main.py` | Loading, validation, search, summaries, and exports |
| `examples/` | Synthetic catalog fixtures |
| `schema/` | Status vocabulary and future contracts |
| `docs/` | Record format, categories, source review, and contribution policy |
| `test_*.py` | Validation, filtering, summary, and export tests |
| `ABOUT.md` | Mission, maturity, boundaries, and governance |

## Metadata principles

- Store metadata, not copied source datasets.
- Prefer publisher-controlled pages.
- Keep declared terms separate from review conclusions.
- Preserve review dates and lifecycle changes.
- Use stable identifiers and controlled vocabulary.
- Keep examples synthetic and non-sensitive.

## Documentation

- [About the project](ABOUT.md)
- [Record format](docs/RECORD_FORMAT.md)
- [Contribution process](docs/CONTRIBUTING_RECORDS.md)
- [Category vocabulary](docs/CATEGORY_VOCABULARY.md)
- [Source verification](docs/SOURCE_VERIFICATION.md)
- [Source acceptance](docs/SOURCE_ACCEPTANCE.md)
- [Maintenance trace](MAINTENANCE_TRACE.md)

## License

MIT
