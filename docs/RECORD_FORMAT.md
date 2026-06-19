# Record Format

Each catalog line is a JSON object.

## Required fields

- `id`: stable record identifier
- `name_zh`: Chinese display name
- `name_en`: English display name
- `publisher`: publishing organization
- `category`: normalized category
- `license`: declared license label

## Recommended fields

- `source_url`
- `last_verified`
- `description_zh`
- `description_en`
- `tags`
- `status`
- `status_reason`
- `replacement_id`
- `reviewer`

## Lifecycle fields

`status` records the metadata review state, not the legal reuse status of the source dataset. Suggested values are `draft`, `reviewed`, `needs-update`, `historical`, and `replacement`.

When `status` is `replacement`, include `replacement_id`. When the source changed or became unavailable, include a concise `status_reason` and update `last_verified`.

## Example

```json
{
  "id": "demo-transport-001",
  "name_zh": "示例交通数据",
  "name_en": "Example Transport Data",
  "publisher": "Example Publisher",
  "category": "transport",
  "license": "review-required",
  "source_url": "https://example.invalid/data",
  "last_verified": "2026-06-19",
  "status": "draft",
  "status_reason": "Demonstration record only",
  "reviewer": null,
  "tags": ["transport", "demo"]
}
```

## Validation guidance

- Keep identifiers stable after publication.
- Use ISO dates in `YYYY-MM-DD` form.
- Store one primary category and use tags for secondary topics.
- Keep Chinese and English names semantically aligned.
- Preserve declared source terms exactly as metadata.
- Do not invent missing publisher, license, or source facts.

Records should describe source material rather than copy the source dataset into this repository.
