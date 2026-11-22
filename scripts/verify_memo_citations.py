#!/usr/bin/env python3
"""
Deterministic Legal Citation & Bitemporal Guardrail Verifier (`scripts/verify_memo_citations.py`).

Pure Python standard-library script (0 external dependencies, 0 local disk cache)
runnable standalone or as a Claude Code `PostToolUse` hook to enforce ABA Formal
Opinion 512 candor and prevent Stanford-RegLab-documented misgrounding/fabrications:
1. Flags out-of-range fabricated article citations (EU AI Act > 113, GDPR > 99,
   EU CRA > 71, NIS2 > 46, DORA > 64, CETS 225 > 36, AP I > 102).
2. Flags stale citations to revoked US Executive Order 14110 (revoked 2025-01-20)
   if revocation is not disclosed.
3. Flags outdated pre-Digital-Omnibus claims asserting EU AI Act Annex III high-risk
   rules entered application on August 2, 2026 without noting the Regulation (EU)
   2026/1744 postponement to December 2, 2027.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

# Exact authoritative maximum article numbers per enacted statute/treaty
STATUTE_MAX_ARTICLES: list[tuple[str, str, int]] = [
    (r"(?:EU\s+AI\s+Act|Regulation\s*\(EU\)\s*2024/1689)[^.\n]{0,50}?\bArticle\s+(\d+)", "EU AI Act (2024/1689)", 113),
    (r"(?:GDPR|Regulation\s*\(EU\)\s*2016/679)[^.\n]{0,50}?\bArticle\s+(\d+)", "EU GDPR (2016/679)", 99),
    (r"(?:Cyber\s+Resilience\s+Act|\bCRA\b|Regulation\s*\(EU\)\s*2024/2847)[^.\n]{0,50}?\bArticle\s+(\d+)", "EU CRA (2024/2847)", 71),
    (r"(?:NIS\s*2|Directive\s*\(EU\)\s*2022/2555)[^.\n]{0,50}?\bArticle\s+(\d+)", "EU NIS2 (2022/2555)", 46),
    (r"(?:\bDORA\b|Regulation\s*\(EU\)\s*2022/2554)[^.\n]{0,50}?\bArticle\s+(\d+)", "EU DORA (2022/2554)", 64),
    (r"(?:CETS\s*(?:No\.?\s*)?225|CoE\s+AI\s+Convention)[^.\n]{0,50}?\bArticle\s+(\d+)", "CoE AI Convention (CETS 225)", 36),
    (r"(?:Additional\s+Protocol\s+I|\bAP\s*I\b)[^.\n]{0,50}?\bArticle\s+(\d+)", "Additional Protocol I (1977)", 102),
]


def audit_legal_text(text: str) -> dict[str, Any]:
    errors: list[str] = []
    warnings: list[str] = []
    checked = 0

    for pattern, label, max_art in STATUTE_MAX_ARTICLES:
        for m in re.finditer(pattern, text, re.I):
            checked += 1
            num = int(m.group(1))
            if num < 1 or num > max_art:
                errors.append(
                    f"FABRICATED CITATION: '{m.group(0).strip()}' — {label} only contains Articles 1-{max_art}."
                )

    # Bitemporal trap 1: Revoked EO 14110
    if re.search(r"Executive\s+Order\s+14110|\bEO\s*14110\b", text, re.I):
        checked += 1
        if not re.search(r"revok|rescind|repeal", text, re.I):
            errors.append(
                "STALE BITEMPORAL ERROR: Text cites US Executive Order 14110 without noting it was revoked on 2025-01-20."
            )

    # Bitemporal trap 2: Pre-Omnibus high-risk deadline claim
    if re.search(r"Annex\s+III[^.\n]{0,80}(?:August\s+2,?\s+2026|2\s+August\s+2026|2026-08-02)", text, re.I):
        checked += 1
        if not re.search(r"2026/1744|Omnibus|December\s+2,?\s+2027|2027-12-02|postpon", text, re.I):
            warnings.append(
                "BITEMPORAL DEADLINE WARNING: Annex III high-risk enforcement was postponed from 2026-08-02 to 2027-12-02 by Regulation (EU) 2026/1744 (Digital Omnibus on AI)."
            )

    # Bitemporal trap 3: Fabricated '72 hours' EU AI Act Art. 73 serious incident deadline
    if re.search(r"(?:AI\s+Act|Article\s+73)[^.\n]{0,80}\b72\s*hours?\b", text, re.I):
        warnings.append(
            "STATUTORY PRECISION WARNING: Verify exact EU AI Act Article 73 serious incident timelines (2-day / 10-day / 15-day statutory windows, not GDPR's 72-hour clock)."
        )

    status = "FAIL" if errors else ("WARN" if warnings else "PASS")
    return {
        "aba_formal_opinion_512_guardrail": status,
        "checks_run": checked,
        "errors": errors,
        "warnings": warnings,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Deterministic legal citation & bitemporal guardrail verifier.")
    parser.add_argument("file", nargs="?", type=Path, help="Markdown/text legal document to audit")
    parser.add_argument("--stdin-hook", action="store_true", help="Read Claude Code PostToolUse JSON payload from stdin")
    args = parser.parse_args()

    target_text = ""
    if args.stdin_hook:
        raw = sys.stdin.read().strip()
        if not raw:
            sys.exit(0)
        try:
            payload = json.loads(raw)
        except json.JSONDecodeError:
            sys.exit(0)
        tool_input = payload.get("tool_input") or {}
        fpath = tool_input.get("file_path") or tool_input.get("path") or ""
        if not str(fpath).lower().endswith((".md", ".txt")):
            sys.exit(0)
        target_text = tool_input.get("content") or tool_input.get("new_string") or ""
        if not target_text and fpath and Path(fpath).exists():
            target_text = Path(fpath).read_text(encoding="utf-8", errors="ignore")
    elif args.file:
        target_text = args.file.read_text(encoding="utf-8")
    else:
        target_text = sys.stdin.read()

    if not target_text.strip():
        sys.exit(0)

    report = audit_legal_text(target_text)
    if args.stdin_hook:
        if report["errors"] or report["warnings"]:
            print(json.dumps({"systemMessage": f"Lex Machina ABA Opinion 512 Guardrail: {json.dumps(report)}"}))
        sys.exit(0)

    print(json.dumps(report, indent=2))
    if report["errors"]:
        sys.exit(1)


if __name__ == "__main__":
    main()
