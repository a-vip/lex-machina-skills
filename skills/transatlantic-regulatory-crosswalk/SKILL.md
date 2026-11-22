---
name: transatlantic-regulatory-crosswalk
description: Maps and harmonizes multi-jurisdictional AI compliance across the EU AI Act (post-Digital Omnibus 2026/1744), US NIST AI RMF 1.0/600-1 & Binding US State AI Laws (Texas TRAIGA, Colorado AI Act, California SB 53/AB 2013 after Jan 2025 EO 14110 revocation), China CAC AI Measures (incl. Sept 2025 Labeling Measures / GB 45438), and CoE CETS 225. Use when designing global AI governance programs or comparing international AI laws. Do NOT use for single-jurisdiction litigation briefs.
license: CC-BY-NC-4.0 OR Commercial-Enterprise
compatibility: Requires lex-machina MCP server v2.0 (check_applicability, get_citation_graph, verify_citations). Works in Claude Code, Cursor, Windsurf, Copilot, and Agensi.
metadata:
  author: Avi Perera / Lex Machina Consortium
  version: "2.0.0"
  domain: comparative-ai-law
  jurisdiction: global
---

# Transatlantic & Global AI Regulatory Crosswalk (v2.0 — 2026 Current)

## Critical 2025-2026 Jurisdictional Shifts Enforced by This Skill
1. **US Federal Pivot (Jan 20, 2025)**: Executive Order 14110 was **FORMALLY REVOKED** on January 20, 2025. Never cite EO 14110 as active US law! Binding US AI obligations now originate primarily from **FTC Section 5 enforcement** and **state statutes**: **Texas TRAIGA (HB 149, effective Jan 1, 2026)**, **California AB 2013 & SB 53 (TFAIA)**, and **Colorado AI Act (SB 24-205 / SB 26-189)**. **NIST AI RMF 1.0 (AI 100-1) & AI 600-1** persist as voluntary enterprise standards and statutory safe harbors.
2. **EU AI Act Post-Digital Omnibus (`Regulation (EU) 2026/1744`)**: Prohibitions live (Feb 2, 2025; NCII/CSAM expansion Dec 2, 2026); GPAI live (Aug 2, 2025); Transparency Art. 50 live (Aug 2, 2026; legacy cutoff Dec 2, 2026); High-risk deferred to **Dec 2, 2027 (Annex III)** and **Aug 2, 2028 (Annex I)**.
3. **China Supply-Chain Labeling Mandate (Sept 1, 2025)**: *Measures for the Labeling of AI-Generated Synthetic Content* (paired with mandatory national standard **GB 45438-2025**) enforces both explicit user-facing notices and implicit file-metadata provenance across generators, platforms, and app stores.
4. **Council of Europe CETS 225 (EU Concluded 2026)**: Binding human rights AI treaty formally approved/concluded by the EU in mid-2026 alongside US/UK/global signatories.

---

## Mandatory `lex-machina` MCP Execution Sequence
1. Call `check_applicability` for each target jurisdiction (`eu/ai-act`, `national/us/nist-ai-rmf`, `national/us/state-ai-laws`, `national/cn/cac-ai-measures`, `coe/ai-convention`) on the client's deployment date.
2. Call `get_provision` across the 5 jurisdictions and `get_citation_graph("eu/ai-act")` to map regulatory interlocks.
3. Cross-reference `references/nist_eu_cac_mapping_matrix.md` to separate **Universal Controls** (build once, satisfy everywhere) from **Divergent Jurisdictional Controls** (e.g., China CAC algorithm registry filing, EU CE marking, Texas AG cure-period workflow, California AB 2013 training disclosures).
4. Call `verify_citations(draft_text, as_of_date=...)`—which automatically blocks any accidental citation to revoked EO 14110 as active law!

---

## 4-Step Harmonization Protocol
1. **Risk Management Harmonization**: Map NIST AI RMF (`GOVERN`/`MAP`/`MEASURE`/`MANAGE`) + ISO/IEC 42001 onto EU AI Act Art. 9, CoE CETS 225 Art. 16, and Colorado AI Act rebuttable-presumption safe harbors.
2. **Prohibited Practices Alignment**: Intersect EU AI Act Art. 5 (incl. Dec 2026 NCII/CSAM) with Texas TRAIGA HB 149 (self-harm manipulation, biometric consent, social scoring) and China CAC Art. 4.
3. **Synthetic Provenance & Watermarking Unification**: Design one C2PA + cryptographic metadata architecture satisfying EU AI Act Art. 50(2), China's Sept 2025 Labeling Measures (`GB 45438-2025`), and NIST AI 600-1 `MANAGE 2.2`.
4. **Deliver Global Regulatory Alignment Matrix**: Produce a board-ready matrix distinguishing currently enforceable obligations vs. deferred 2027–2028 milestones, signed with the ABA Formal Opinion 512 verification footer.
