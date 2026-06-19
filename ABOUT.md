# About ChinaOpenDataIndex

## Mission

ChinaOpenDataIndex provides a reviewable metadata catalog for public-data sources connected to Chinese institutions and related organizations.

## Intended users

- Data researchers building source inventories
- Developers preparing bilingual metadata catalogs
- Teams reviewing source availability and declared terms
- Maintainers who need structured lifecycle and verification records

## Core capabilities

- JSONL catalog loading
- Required-field validation
- Controlled category and lifecycle values
- Duplicate identifier detection
- Keyword, category, status, and valid-only filters
- Catalog health summaries
- English-documented compatibility fields for bilingual metadata

## Boundaries

The project stores metadata only. It does not download datasets, verify changing website terms automatically, or determine whether a source may be reused for a particular commercial purpose.

## Architecture

```text
JSONL records -> field validation -> vocabulary checks
              -> duplicate checks -> search filters -> summary output
```

## Design priorities

1. Metadata-only storage
2. Publisher-controlled source references
3. Stable identifiers
4. Visible lifecycle changes
5. Faithful bilingual metadata
6. Synthetic repository examples

## Maturity

The project is an executable MVP with validators, filters, health summaries, controlled vocabularies, contribution guidance, source-verification policy, examples, and tests.

## Governance

Source changes, status changes, replacements, and term changes should remain visible in Git history. Public documentation and examples are maintained in English.
