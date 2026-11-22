---
name: legislative-intent-detective
description: Reconstructs statutory legislative intent (travaux preparatoires) using CJEU teleological/contextual canons, concordance-aware multi-stage redline diffs, and phrase-level institutional git blame across Commission proposals, Council approaches, Parliament mandates, trilogue texts, and Official Journal enactments. Use when interpreting ambiguous legal clauses, drafting regulatory litigation briefs, or proving which institution introduced an amendment. Do NOT use for simple point-in-time compliance checklists without interpretive ambiguity.
license: CC-BY-NC-4.0 OR Commercial-Enterprise
compatibility: Requires lex-machina MCP server v2.0 (concordance-aware diff_provisions & phrase-level blame_provision). Works in Claude Code, Cursor, Windsurf, Copilot, and Agensi.
metadata:
  author: Avi Perera / Lex Machina Consortium
  version: "2.0.0"
  domain: statutory-interpretation
  jurisdiction: eu-international
---

# Travaux Preparatoires & Legislative Intent Detective (v2.0)

## Doctrinal Mission
Resolving statutory ambiguity before the Court of Justice of the European Union (CJEU) (*Cilfit*, Case 283/81; *Nilsson*, Case C-162/97) or international tribunals (VCLT Articles 31–32) requires tracing a legal norm across its full drafting evolution—even when **article numbers shifted between legislative drafts** (e.g., EU AI Act Proposal Art. 52 → Final Art. 50; Parliament Art. 29a → Final Art. 27; GDPR Proposal Art. 20 → Final Art. 22; CoE Draft Art. 4 → Adopted Art. 2).

---

## Mandatory `lex-machina` MCP Execution Sequence
1. **Concordance-Aware Institutional Blame**: Call `blame_provision(instrument_path, provision)` to obtain **clause- and token-level institutional attribution** (preserving original Commission/Parliament authorship even after Official Journal lawyer-linguist formatting edits).
2. **4-Column Redline Diffs**: Call `diff_provisions(instrument_path, provision, stage_a, stage_b)` across:
   - `commission_proposal` → `parliament_mandate` (reveals Parliamentary fundamental-rights expansion)
   - `council_general_approach` → `parliament_mandate` (reveals Council vs. Parliament fault lines)
   - `parliament_mandate` → `official_journal_final` (reveals exact Trilogue compromise concessions)
   - `official_journal_final` → `digital_omnibus_2026_1744` (where applicable, reveals 2026 statutory amendments)
3. **Recital-to-Article Teleological Grounding**: Read `linked_recitals` returned by `get_provision` or `get_citation_graph`, then fetch those exact recitals via `get_provision(instrument_path, "recitals/recital-XXX.md")` to ground the *effet utile* analysis. Consult `references/travaux_preparatoires_methodology.md`.
4. **Deterministic Citation Audit**: Run `verify_citations(draft_text)` before returning the legal opinion.

---

## Analytical Deliverable Structure
1. **Statutory Ambiguity & Competing Constructions**: Identify the disputed text and competing literal readings.
2. **4-Column Legislative Evolution Table**: Present Proposal vs. Council vs. Parliament vs. Final/Amended text with exact document symbols (`COM(2021) 206 final`, `ST 14954/22`, `P9_TA(2023)0236`, `ST 5662/24`, `OJ L 2024/1689`, `Regulation (EU) 2026/1744`) and concordance notes for renumbered articles.
3. **Institutional Blame Breakdown**: Report token-level provenance percentages from `blame_provision` showing which co-legislator authored each restrictive clause or carve-out.
4. **Teleological & Judicial Conclusion**: Synthesize the authoritative construction most likely to survive CJEU/VCLT scrutiny, explicitly distinguishing primary verbatim texts (`full_primary_xhtml_akn` / `full_primary_pdf`) from analytical milestone briefs (`structured_regulatory_brief`).

---

## Abstention & Integrity Guardrails
- Always inspect `provenance.provenance_mode` returned by `get_provision`. If a historical negotiating stage is marked `structured_regulatory_brief`, explicitly disclose that limitation rather than quoting it as verbatim legislative text.
- Never omit the SHA-256 primary-source digest or ABA Formal Opinion 512 verification block.
