# WordPress 7.0 Release Readiness

A CLI tool to analyze WordPress installations for future compatibility with the upcoming WordPress 7.0 major release.

## Features
- Check PHP version compatibility.
- Identify Classic vs. Block themes.
- Detect outdated plugin patterns.
- Generate a "Release Squad" readiness report.

## Installation
```bash
pip install -r requirements.txt
```

## Usage
```bash
python -m wp_7_readiness.checker /path/to/wordpress/root
```
