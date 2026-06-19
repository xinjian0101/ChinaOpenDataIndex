# ChinaOpenDataIndex

Bilingual metadata validation and search for Chinese open-data catalogs.

## MVP

- Validate dataset IDs, bilingual names, publishers, categories, and licenses
- Read one JSON object per line
- Search by keyword and exact category
- Store metadata only

## Run

```bash
python main.py catalog.jsonl --query transit
python main.py catalog.jsonl --category transport
```

Required fields: `id`, `name_zh`, `name_en`, `publisher`, `category`, `license`.

## Test

```bash
python tests.py
```

## License

MIT
