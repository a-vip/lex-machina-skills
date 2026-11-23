---
name: cjeu-icj-precedent-counsel
description: Synthesizes binding Court of Justice of the European Union (CJEU) jurisprudence (SCHUFA C-634/21 on automated AI scoring, Schrems II C-311/18 on international AI/cloud transfers, Meta v Bundeskartellamt C-252/21 on profiling & competition, La Quadrature du Net C-511/18 on automated traffic analysis) and International Court of Justice (ICJ) IHL precedent (1996 Nuclear Weapons Advisory Opinion on intransgressible principles & the Martens Clause). Use when briefing courts, drafting litigation risk memos, or interpreting statutory ambiguities via binding judicial holdings. Do NOT use for purely statutory compliance checklists without judicial interpretation.
license: CC-BY-NC-4.0 OR Commercial-Enterprise
compatibility: Requires lex-machina MCP server v3.0 (get_provision, search_corpus, get_citation_graph, verify_citations). Works in Claude Code, Cursor, Windsurf, Copilot, and Agensi.
metadata:
  author: Avi Perera / Lex Machina Consortium
  version: "3.0.0"
  domain: judicial-precedent
  jurisdiction: eu-and-international
---

# CJEU & ICJ Binding Judicial Precedent Counsel (v3.0)

## Scope of Grounded Primary Judgments (`caselaw/`)
All rulings in `lex-machina` v3.0 are ingested **verbatim** from EUR-Lex CELLAR Formex XHTML (`CELEX 6...`) and official UN ODS transmissions (`A/51/218`) with SHA-256 digests:
- **`caselaw/cjeu/schufa-c-634-21`**: Automated probability/credit scoring strongly relied upon by downstream decision-makers triggers GDPR Article 22(1) automated decision-making restrictions.
- **`caselaw/cjeu/schrems-ii-c-311-18`**: Essential-equivalence safeguards, Transfer Impact Assessments, and SCC surveillance boundaries for transatlantic AI & cloud pipelines.
- **`caselaw/cjeu/meta-bundeskartellamt-c-252-21`**: Prohibition on justifying personalized AI behavioral profiling via contractual necessity; interplay of competition law and GDPR Arts. 6 & 9.
- **`caselaw/cjeu/la-quadrature-du-net-c-511-18`**: Strict EU Charter proportionality limits on bulk metadata retention and automated real-time algorithmic traffic analysis.
- **`caselaw/icj/nuclear-weapons-1996`**: Intransgressible principles of IHL (distinction, unnecessary suffering) and Martens Clause applicability to all new weapons technologies (bedrock for AP I Art. 36 & LAWS reviews).

## Mandatory `lex-machina` MCP Execution Sequence
1. Call `search_corpus(query, jurisdiction="caselaw")` to pinpoint relevant judicial reasoning sections and Operative Parts / Dispositifs.
2. Call `get_provision` on the relevant `caselaw/...` instrument to retrieve exact verbatim judicial text (never paraphrase the Operative Part from memory).
3. Call `get_citation_graph` on the ruling to traverse directly to the interpreted statutory articles (`eu/gdpr`, `eu/ai-act`, `eu/cyber/nis2`, `ihl/geneva-conventions`, `un/ccw-laws`).
4. Cross-check `references/landmark_judicial_holdings.md` for doctrinal tests and national divergence notes (e.g., UK `Data (Use and Access) Act 2025` diverging from *SCHUFA* on UK GDPR Art. 22).
5. Call `verify_citations(draft_text, as_of_date)` before delivering the memorandum and append the ABA Formal Opinion 512 verification footer.
