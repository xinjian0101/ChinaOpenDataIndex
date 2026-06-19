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
  "last_verified": "2026-06-19"
}
```

Records should describe source material rather than copy the source dataset into this repository.
