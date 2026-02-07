# WordPress 7.0 Roadmap and AI Integration Review

This repository contains a short, source-backed review of the WordPress 7.0 roadmap and AI integration goals, plus a tiny validator that checks the source list.

## Contents

- `report.md`: Review with citations
- `data/sources.json`: Source list used for the review
- `scripts/validate_sources.py`: Validates the source list

## Usage

```bash
python scripts/validate_sources.py
```

## Development

```bash
python -m unittest
python -m ruff check .
```
