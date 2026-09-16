#!/usr/bin/env python3
"""Regenerate site/index.html's embedded data from data/processed/crosswalk.csv.

Run from the repository root after editing crosswalk.csv:
    python3 code/02_build_site.py
"""
import csv
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CSV_PATH = ROOT / "data" / "processed" / "crosswalk.csv"
JSON_PATH = ROOT / "site" / "crosswalk_data.json"
HTML_PATH = ROOT / "site" / "index.html"


def main() -> None:
    with CSV_PATH.open() as f:
        rows = list(csv.DictReader(f))

    JSON_PATH.write_text(json.dumps(rows, ensure_ascii=False, indent=0))

    html = HTML_PATH.read_text()
    new_html, n = re.subn(
        r"var DATA = \[.*?\];",
        "var DATA = " + JSON_PATH.read_text() + ";",
        html,
        count=1,
        flags=re.S,
    )
    if n != 1:
        raise SystemExit("Could not find the DATA placeholder in site/index.html")
    HTML_PATH.write_text(new_html)

    outcomes = sorted({r["tsa_outcome_id"] for r in rows})
    print(f"Rebuilt site/index.html: {len(rows)} rows, {len(outcomes)} outcomes.")


if __name__ == "__main__":
    main()
