# ChinaOpenDataIndex

Bilingual metadata validation and search for Chinese open-data catalogs.

## MVP

- Validate dataset names, publishers, categories, licenses, and source URLs
- Track commercial-use review status
- Search JSONL catalogs by keyword and category
- Store metadata only; do not redistribute source datasets

## Run

```bash
python main.py examples/catalog.jsonl --query transit --commercial review_required
```

## Test

```bash
python -m unittest -v
```

## License

MIT
