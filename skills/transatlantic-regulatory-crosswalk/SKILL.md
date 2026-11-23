---
name: transatlantic-regulatory-crosswalk
description: Maps and harmonizes planetary multi-jurisdictional AI compliance across 9 global regimes: EU AI Act (post-Digital Omnibus 2026/1744 + EC 2025 PDFs), US NIST AI RMF & Binding State AI Laws (verbatim Texas TRAIGA HB 149, Colorado SB 24-205/SB 26-189, California AB 2013/SB 53 post-EO 14110 revocation), China CAC (Orders 9/12/15 + Sept 2025 GB 45438-2025 Labeling), UK (DSIT/AISI/DUAA 2025), South Korea AI Basic Act (effective Jan 22, 2026), Japan AI Promotion Act (effective Sept 1, 2025), Brazil PL 2338/2023 (pending Chamber review), Singapore IMDA Agentic AI Framework (2026), CoE CETS 225, and ISO/IEC 42001:2023. Use when designing global AI governance programs or comparing international AI laws. Do NOT use for single-jurisdiction litigation briefs.
license: CC-BY-NC-4.0 OR Commercial-Enterprise
compatibility: Requires lex-machina MCP server v3.0 (check_applicability, get_citation_graph, verify_citations). Works in Claude Code, Cursor, Windsurf, Copilot, and Agensi.
metadata:
  author: Avi Perera / Lex Machina Consortium
  version: "3.0.0"
  domain: comparative-ai-law
  jurisdiction: global
---

# Planetary 9-Jurisdiction AI Regulatory Crosswalk (v3.0 — 2026 Current)

## Critical 2025–2026 Global Shifts Enforced by This Skill
1. **EU AI Act Post-Digital Omnibus (`Regulation (EU) 2026/1744`)**: Prohibitions live (Feb 2, 2025; NCII/CSAM Dec 2, 2026); GPAI live (Aug 2, 2025); Art. 50 live (Aug 2, 2026; legacy cutoff Dec 2, 2026); High-risk deferred to **Dec 2, 2027 (Annex III)** & **Aug 2, 2028 (Annex I)**.
2. **US Federal Pivot & Binding States**: **EO 14110 was REVOKED Jan 20, 2025**—never cite it as active! Binding US obligations flow from **Texas TRAIGA (`HB 149`, effective Jan 1, 2026)**, **California AB 2013 & SB 53 (TFAIA)**, **Colorado SB 24-205 / SB 26-189**, and FTC Section 5, with **NIST AI RMF & ISO/IEC 42001** as voluntary safe harbors.
3. **Asia-Pacific Binding Laws & Agentic Frameworks**:
   - **South Korea AI Basic Act (`Act No. 20676`)**: Effective **January 22, 2026** (High-Impact AI governance, GenAI advance disclosure/watermarking, extraterritorial domestic representative).
   - **Japan AI Promotion Act (`Act No. 53 of 2025`)**: Fully in force **September 1, 2025** (innovation-first promotion, AI Strategy Headquarters, mandatory misuse-investigation cooperation, no upfront EU-style fines).
   - **China CAC (`GB 45438-2025`)**: Supply-chain explicit + implicit metadata synthetic labeling mandatory since **September 1, 2025**.
   - **Singapore IMDA Model AI Governance Framework for Agentic AI (2026)**: World's flagship governance standard for tool-calling autonomous agents.
4. **UK & Latin America**:
   - **UK Data (Use and Access) Act 2025 (`2025 c. 18`)**: Reforms UK GDPR Art. 22 automated decision-making (diverging from CJEU *SCHUFA*) paired with UK AISI evaluations.
   - **Brazil `PL 2338/2023`**: Approved by Federal Senate Dec 2024, **PENDING** Chamber of Deputies Special Committee review (**NOT YET ENACTED** — never cite as currently in force!).

## Mandatory `lex-machina` MCP Execution Sequence
1. Call `check_applicability` across every target jurisdiction (`eu/ai-act`, `national/us/nist-ai-rmf`, `national/us/state-ai-laws`, `national/cn/cac-ai-measures`, `national/uk/ai-governance`, `national/kr/ai-basic-act`, `national/jp/ai-promotion-act`, `national/br/ai-bill-pl2338`, `national/sg/agentic-ai-governance`, `standards/iso-iec-42001`, `coe/ai-convention`).
2. Call `get_provision` across primary provisions and `get_citation_graph("standards/iso-iec-42001")` to anchor build-once universal controls.
3. Separate **Universal Controls** (ISO/IEC 42001 + NIST AI RMF + C2PA metadata provenance) from **Jurisdiction-Specific Mandates** (EU CE marking, Korea domestic representative, China CAC algorithm filing, Texas AG 60-day cure workflow, Singapore agentic least-privilege sandboxing).
4. Call `verify_citations(draft_text, as_of_date)` to automatically catch EO 14110, pre-Omnibus Annex III dates, and Brazil PL 2338 status errors!
