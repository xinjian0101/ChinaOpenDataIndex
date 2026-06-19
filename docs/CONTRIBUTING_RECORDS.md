# Contributing Catalog Records

Contributions should add verifiable metadata, not redistribute source datasets.

## Submission checklist

1. Use a stable lowercase identifier.
2. Provide both Chinese and English display names.
3. Identify the original publisher.
4. Choose one normalized category.
5. Record the declared license label exactly as shown by the source.
6. Include the original source page when available.
7. Add the date on which the source was checked.
8. Avoid personal information and copied source content.

## Quality rules

- Do not guess a license.
- Do not state that reuse is allowed without supporting source terms.
- Mark unavailable information clearly rather than inventing it.
- Keep descriptions factual and concise.
- Prefer publisher-controlled pages over secondary mirrors.
- Use ISO dates in `YYYY-MM-DD` format.

## Review process

A maintainer should check required fields, duplicate identifiers, source reachability, bilingual consistency, and whether the record contains copied material.

## Suggested commit message

```text
catalog: add <publisher> <dataset name>
```

## Removal requests

Open an issue with the record identifier and a clear reason. Records may be corrected, marked unavailable, or removed when the metadata cannot be verified.
