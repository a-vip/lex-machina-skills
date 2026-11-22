---
name: eu-ai-act-auditor
description: Audits AI systems and GPAI models against Regulation (EU) 2024/1689 (EU AI Act) as amended by Digital Omnibus Regulation (EU) 2026/1744, including Article 5 prohibitions, Article 6/Annex III high-risk classification, Article 27 FRIA, Article 50 transparency, and Articles 51-55 GPAI rules. Use when classifying AI risk tiers, checking EU enforceability dates, or drafting EU AI compliance memos. Do NOT use for purely non-EU domestic statutes or non-AI general contract drafting.
license: CC-BY-NC-4.0 OR Commercial-Enterprise
compatibility: Requires lex-machina MCP server (Streamable HTTP or stdio). Works in Claude Code, Cursor, Windsurf, Copilot, and Agensi.
metadata:
  author: Avi Perera / Lex Machina Consortium
  version: "2.0.0"
  domain: eu-ai-regulation
  jurisdiction: eu
---

# EU AI Act Compliance & Bitemporal Risk Auditor (v2.0 — Post-Digital Omnibus)

## Critical 2025-2026 Regulatory Traps Prevented by This Skill
Standard LLMs routinely hallucinate outdated 2024 EU AI Act timelines and miss amending legislation. This skill deterministically prevents four high-liability errors:
1. **Digital Omnibus Postponement Trap (`Regulation (EU) 2026/1744`)**: Standalone Annex III high-risk compliance was formally decoupled and postponed from August 2, 2026 to **December 2, 2027**, and Annex I regulated-product AI safety components to **August 2, 2028**.
2. **December 2, 2026 Article 5 Expansion & Legacy Cutoff**: Two newly added Article 5 bans (non-consensual sexual deepfakes & CSAM) AND the transition deadline for legacy generative AI systems (placed on market before Aug 2, 2026) under Article 50(2) both take effect on **December 2, 2026**.
3. **Article 6(3) Profiling Override**: Even if an Annex III system performs a narrow procedural/preparatory task, if it performs **profiling** of natural persons (GDPR Art. 4(4)), it is **always High-Risk**.
4. **Incident Reporting Timeline Precision**: Never invent "72 hours" for EU AI Act serious incidents—always verify exact tiered deadlines directly from `get_provision("eu/ai-act", "articles/article-073.md")` (2-day / 10-day / 15-day statutory windows).

---

## Mandatory `lex-machina` MCP Execution Sequence
1. **Retrieve Verbatim Statutory Text**: Call `get_provision("eu/ai-act", ...)` for `articles/article-002.md`, `article-003.md`, `article-005.md`, `article-006.md`, `article-009.md`, `article-014.md`, `article-015.md`, `article-027.md`, `article-050.md`, `article-051.md`, `article-053.md`, `article-055.md`, `article-073.md`, `article-099.md`, and `annexes/annex-iii.md`.
2. **Run Bitemporal Enforceability Gate**: Call `check_applicability("eu/ai-act", provision, as_of_date=..., placed_on_market_date=...)` for EVERY triggered obligation. Never state a clause is currently enforceable without checking `check_applicability`.
3. **Cross-Check Cyber & Privacy Interlocks**: Call `get_citation_graph("eu/ai-act")` to verify GDPR (Art. 22 / Art. 35) and EU Cyber Resilience Act (CRA Art. 14 / Art. 15 presumption of conformity) overlaps.
4. **Mandatory Pre-Delivery Citation Audit**: Run `verify_citations(draft_text, as_of_date=...)` before presenting any memo. If `aba_formal_opinion_512_audit != "PASS"`, fix every flagged citation before replying.

---

## 5-Step Audit Protocol
1. **Territorial & Material Scope (Art. 2)**: Verify EU market nexus and test military/national security (Art. 2(3)), scientific R&D (Art. 2(6)), personal use, and open-source exceptions (Art. 2(12)).
2. **Article 5 Unacceptable-Risk Gate (Active since Feb 2, 2025; expanded Dec 2, 2026)**: Screen against all 8 baseline bans (incorporating Feb 2025 Commission Guidelines `C(2025) 884 final`) plus the Dec 2, 2026 NCII/CSAM deepfake prohibitions. Consult `references/prohibited_practices_checklist.md`.
3. **High-Risk Classification & Derogations (Art. 6, Annex I & III)**: Apply `references/risk_classification_tree.md`, test Art. 6(3) accessory derogation + mandatory profiling override, and record the **post-Omnibus enforceability date** (`2027-12-02` Annex III vs. `2028-08-02` Annex I).
4. **GPAI Models (Arts. 51-55 & July 2025 Code of Practice)**: Check generality (Art. 3(63)), systemic risk compute presumption (`> 10^25` FLOPs), copyright/training summary duties (Art. 53, enforceable Aug 2, 2025; legacy grace until Aug 2, 2027), and adversarial red-teaming (Art. 55).
5. **Transparency & FRIA (Arts. 27 & 50)**: Verify direct-interaction disclosures, machine-readable synthetic marking (Art. 50(2), enforceable Aug 2, 2026; legacy cutoff Dec 2, 2026), and public/essential-service FRIA duties.

---

## Abstention & Escalation Rules (ABA Formal Opinion 512)
- If `get_provision` returns `PROVISION NOT IN CORPUS`, explicitly state `PROVISION NOT IN CORPUS`—**never synthesize missing text from memory**.
- Output using `templates/legal_memorandum_template.md`, embedding the **ABA Formal Opinion 512 Verification Certificate** and **SHA-256 Provenance Footer**.
