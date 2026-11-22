---
name: cyber-treaty-compliance-auditor
description: Audits digital products, critical infrastructure entities, financial institutions, and cross-border electronic evidence exposure against the EU Cyber Resilience Act (Regulation (EU) 2024/2847), NIS2 Directive (2022/2555), DORA (2022/2554), UN Cybercrime Convention (Hanoi Convention A/RES/79/243), Council of Europe Budapest Convention (ETS 185 & CETS 224), and Tallinn Manual 3.0 norms. Use when advising on product cybersecurity, ENISA 24h vulnerability reporting, financial ICT resilience, or international cyber law. Do NOT use for purely non-cyber AI bias audits.
license: CC-BY-NC-4.0 OR Commercial-Enterprise
compatibility: Requires lex-machina MCP server v2.0 (eu/cyber/cra, eu/cyber/nis2, eu/cyber/dora, un/cybercrime-convention, coe/budapest-convention). Works in Claude Code, Cursor, Windsurf, Copilot, and Agensi.
metadata:
  author: Avi Perera / Lex Machina Consortium
  version: "2.0.0"
  domain: cyber-and-international-law
  jurisdiction: eu-un-coe
---

# Cyber Law & International Treaty Compliance Auditor (v2.0)

## Mission & Multi-Layer Cyber Architecture
Modern digital products and AI systems sit at the intersection of **three interlocked legal layers**:
1. **Product Security (`eu/cyber/cra` — Regulation (EU) 2024/2847)**: Governs hardware/software with digital elements placed on the EU market—including **mandatory ENISA vulnerability/incident reporting live since September 11, 2026** (Art. 14) and full SBOM / secure-by-design / CE marking compliance on **December 11, 2027**, plus **presumption of conformity with EU AI Act Article 15 cybersecurity**.
2. **Entity Operational Resilience (`eu/cyber/nis2` & `eu/cyber/dora`)**: NIS2 (`2022/2555`, enforceable Oct 18, 2024) governs essential/important entities (24h early warning / 72h notification); DORA (`2022/2554`, enforceable Jan 17, 2025) operates as **lex specialis** for financial institutions and Critical ICT Third-Party Service Providers (CTPPs).
3. **Public International Cyber & Evidence Law (`un/cybercrime-convention` & `coe/budapest-convention` & Tallinn Manual 3.0)**: Contrasts the **UN Hanoi Cybercrime Convention (`A/RES/79/243`)** (opened Oct 25, 2025, open until Dec 31, 2026, requiring 40 ratifications under Art. 65) against the **Budapest Convention (`ETS 185` / `CETS 224`)** Article 15 human-rights and judicial proportionality safeguards, alongside state-responsibility/sovereignty norms under the Tallinn Manual 3.0 project.

---

## Mandatory `lex-machina` MCP Execution Sequence
1. **Check Bitemporal Enforceability First**: Call `check_applicability` on `eu/cyber/cra` (`articles/article-014.md` vs. `*`), `eu/cyber/nis2`, `eu/cyber/dora`, and `un/cybercrime-convention`.
2. **Retrieve Exact Statutory Articles**: Call `get_provision` on CRA `article-014.md` & `article-064.md`, NIS2 `article-021.md` & `article-023.md`, DORA `article-017.md`, and Budapest/Hanoi treaty provisions.
3. **Map AI-Cyber Interlocks**: Call `get_citation_graph("eu/cyber/cra")` and `get_citation_graph("eu/cyber/nis2")` to identify lex specialis preemption (DORA > NIS2) and AI Act Article 15 presumption of conformity.
4. **Verify Every Citation**: Run `verify_citations(draft_text, as_of_date=...)` prior to output.

---

## 4-Step Cyber Compliance & Treaty Protocol (Consult `references/cyber_regulatory_matrix.md`)
1. **Entity vs. Product Scoping & Lex Specialis Resolution**: Determine if the client is a product manufacturer/open-source steward (CRA), an essential/important entity (NIS2), a financial entity/CTPP (DORA overrides NIS2), or a high-risk AI provider (CRA + AI Act Art. 15 dual compliance).
2. **Incident & Vulnerability Reporting Clock Audit**: Harmonize overlapping notification windows: CRA Art. 14 actively exploited vulnerability reporting to ENISA (24h early warning / 72h notification, live Sept 11, 2026), NIS2 Art. 23 (24h/72h/1-month), DORA Art. 17/19 major ICT incidents, and GDPR Art. 33 (72h personal data breach).
3. **Cross-Border Electronic Evidence & Surveillance Risk Assessment**: Evaluate lawful-access exposure under Budapest Convention `CETS 224` direct provider orders vs. UN Hanoi Cybercrime Convention serious-crime (4+ year) cross-border evidence sharing once 40 ratifications are reached.
4. **Deliver Formal Cyber Legal Memorandum**: Use `templates/legal_memorandum_template.md` with the ABA Formal Opinion 512 Verification Certificate and SHA-256 provenance digests.
