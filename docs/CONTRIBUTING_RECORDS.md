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
9. Add a lifecycle status when the record is not current.
10. Link a replacement identifier when a newer official record exists.

## Quality rules

- Do not guess a license.
- Do not state that reuse is allowed without supporting source terms.
- Mark unavailable information clearly rather than inventing it.
- Keep descriptions factual and concise.
- Prefer publisher-controlled pages over secondary mirrors.
- Use ISO dates in `YYYY-MM-DD` format.
- Keep one primary category and use tags for secondary topics.
- Explain every status change in the commit message.

## Review process

A maintainer should check required fields, duplicate identifiers, source reachability, bilingual consistency, category vocabulary, lifecycle status, and whether the record contains copied material.

## Review record

For each reviewed batch, record:

- affected record identifiers;
- reviewer;
- review date;
- source pages checked;
- fields changed;
- unresolved questions;
- replacement records;
- reason for any lifecycle change.

## Suggested commit messages

```text
catalog: add <publisher> <dataset name>
catalog: verify <record id>
catalog: update <record id> source metadata
catalog: mark <record id> historical
```

## Correction and retirement requests

Open an issue with the record identifier, evidence, and a clear reason. Records may be corrected, marked for another review, linked to a replacement, or retained as historical metadata. Keep the decision visible in Git history.
