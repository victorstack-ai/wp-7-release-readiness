#!/usr/bin/env python3
"""Validate sources.json for the WordPress 7.0 + AI review."""

from __future__ import annotations

from pathlib import Path

from wp7_review.validator import load_sources, validate_sources


def main() -> int:
    repo_root = Path(__file__).resolve().parents[1]
    sources_path = repo_root / "data" / "sources.json"
    sources = load_sources(sources_path)
    issues = validate_sources(sources)
    if issues:
        print("Source validation failed:")
        for issue in issues:
            print(f"- {issue}")
        return 1
    print(f"Sources OK ({len(sources)} entries).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
