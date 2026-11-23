# Lex Machina Pro v2.0 — Institutional AI, Cyber & International Law Agent Skills Suite

[![Validate Skills & Verifier Hook](https://github.com/a-vip/lex-machina-skills/actions/workflows/validate-skills.yml/badge.svg)](https://github.com/a-vip/lex-machina-skills/actions/workflows/validate-skills.yml)
[![Standard: agentskills.io](https://img.shields.io/badge/Spec-agentskills.io_v1-blue.svg)](https://agentskills.io)
[![Claude Code Plugin](https://img.shields.io/badge/Claude_Code-Native_Plugin-purple.svg)](.claude-plugin/plugin.json)
[![Agensi Compatible](https://img.shields.io/badge/Marketplace-agensi.io-teal.svg)](marketplace.json)
[![Engine: lex-machina v2.0](https://img.shields.io/badge/Corpus_Engine-a--vip%2Flex--machina-orange.svg)](https://github.com/a-vip/lex-machina)
[![ABA Formal Opinion 512](https://img.shields.io/badge/Ethics-ABA_Opinion_512_Guardrails-brightgreen.svg)](scripts/verify_memo_citations.py)

> **The only AI legal skill suite on Earth backed by full-text SHA-256 primary-source provenance, bitemporal 2026 enforceability logic, concordance-aware institutional `git blame`, a deterministic ABA Formal Opinion 512 citation-verification hook, and a 100-case open empirical benchmark.**

---

## Why No Competitor on Earth Has Done This — And Why It Beats Every Alternative

Empirical evaluations by **Stanford RegLab** (*Journal of Empirical Legal Studies* 2025; *Benchmarking Legal RAG* 2026; *PNAS* 2026) revealed that even elite commercial legal AI platforms (**Lexis+ AI ~17%**, **Westlaw AI ~33%**) suffer severe **misgrounding** and score only **58%–64%** on multi-jurisdictional statutory surveys. Meanwhile, **SkillsBench (2026)** proved that curated, modular `agentskills.io` skills paired with deterministic verification scripts drive double-digit accuracy gains over baseline models, whereas static prose prompts fail on edge cases.

**What makes `lex-machina-skills` v2.0 categorically superior to every legal skill, prompt pack, or MCP wrapper on the planet:**

1. **Catches the Exact 2025–2026 Statutory Traps That Break Frontier Models**:
   - Knows **EU Digital Omnibus `Regulation (EU) 2026/1744`** postponed standalone Annex III high-risk enforcement to **Dec 2, 2027** and Annex I to **Aug 2, 2028**, while adding NCII sexual deepfake & CSAM Article 5 bans and closing the legacy Art. 50(2) window on **Dec 2, 2026**.
   - Actively **blocks stale citations to US Executive Order 14110** (formally **revoked January 20, 2025**), routing US compliance to binding state statutes (**Texas TRAIGA HB 149** live Jan 1, 2026; **California AB 2013 & SB 53/TFAIA**; **Colorado AI Act**), FTC Section 5, and voluntary NIST AI RMF safe harbors.
   - Integrates **EU Cyber Resilience Act (`2024/2847`)** (ENISA 24h vulnerability reporting live **Sept 11, 2026**; full compliance Dec 11, 2027), **NIS2**, **DORA** (*lex specialis*), **Budapest Convention (`ETS 185`/`CETS 224`)**, **UN Hanoi Cybercrime Convention (`A/RES/79/243`, 40-ratification threshold)**, and **China's Sept 1, 2025 Mandatory AI Labeling Measures (`GB 45438-2025`)**.
2. **Deterministic Hard Guardrail (`PostToolUse` Hook + `verify_citations`)**:
   - Ships with a zero-dependency Python verifier ([`scripts/verify_memo_citations.py`](scripts/verify_memo_citations.py)) wired directly into Claude Code's [`hooks/hooks.json`](hooks/hooks.json) `PostToolUse` lifecycle—automatically rejecting fabricated articles (`EU AI Act Art. 199`), stale revoked EO 14110 claims, and misquoted deadlines before an attorney ever sees the output.
3. **True 4-Column Concordance & Token-Level Institutional `git blame`**:
   - Tracks renumbered provisions seamlessly across 2021–2026 legislative stages (e.g., Proposal Art. 52 → Final Art. 50; Parliament Art. 29a → Final Art. 27; GDPR Proposal Art. 20 → Final Art. 22) and attributes exact phrases to the European Commission, Council, Parliament, or Trilogue negotiators.
4. **Native Cross-Platform Packaging + Open 100-Case Empirical Benchmark**:
   - Strict `agentskills.io` progressive disclosure (< 100 lines per `SKILL.md` with explicit **positive AND negative triggers**), native `.claude-plugin/` marketplace manifest, `.mcp.json` (`uvx` + Cloudflare Edge Streamable HTTP), Cursor `.mdc` rules, Agensi (`agensi.io`) metadata, and continuous verification via [`LexMachina-Eval`](https://github.com/a-vip/lex-machina/blob/main/evals/lexmachina_bench.jsonl).

---

## The Five Institutional Skills (`skills/`)

| # | Skill | Domain & 2026 Authority | Core Differentiator |
| :- | :--- | :--- | :--- |
| 1 | [**`eu-ai-act-auditor`**](skills/eu-ai-act-auditor/SKILL.md) | EU AI Act (`2024/1689`) + **Digital Omnibus (`2026/1744`)** + 2025 Guidelines & GPAI Code | Bitemporal `check_applicability` gate + Art. 6(3) profiling override + verified Art. 73 incident clocks |
| 2 | [**`legislative-intent-detective`**](skills/legislative-intent-detective/SKILL.md) | CJEU Teleological & VCLT *Travaux Préparatoires* | 4-column renumbering concordance + token-level institutional `git blame` + linked recitals |
| 3 | [**`ihl-weapons-review-sentinel`**](skills/ihl-weapons-review-sentinel/SKILL.md) | Geneva Conventions (1949), AP I Art. 36 (1977) & **UN CCW LAWS (2019–2026)** | 5-pillar weapons review + Seventh Review Conference context + ML retraining re-review mandate |
| 4 | [**`transatlantic-regulatory-crosswalk`**](skills/transatlantic-regulatory-crosswalk/SKILL.md) | **EU 2026 vs. US State/NIST (post-EO 14110) vs. China Sept 2025 vs. CoE CETS 225** | Unified global control matrix preventing EO 14110 errors & unifying C2PA / `GB 45438` / Art. 50 |
| 5 | [**`cyber-treaty-compliance-auditor`**](skills/cyber-treaty-compliance-auditor/SKILL.md) | **EU CRA (`2024/2847`), NIS2, DORA, UN Hanoi Cybercrime & Budapest Conventions** | Harmonizes CRA Sept 2026 ENISA clocks, DORA *lex specialis*, AI Act Art. 15 interlock & treaty risk |

---

## 1-Click Installation Across Every Major AI Agent Platform

### 1. Claude Code (Native Plugin Marketplace — Recommended)
```bash
/plugin marketplace add a-vip/lex-machina-skills
/plugin install lex-machina@lex-machina-marketplace
```
Installs all 5 skills, the `lex-machina` MCP server (`.mcp.json`), and the automatic ABA Formal Opinion 512 `PostToolUse` citation verifier hook (`hooks/hooks.json`).

### 2. Agensi (`agensi.io`)
Every skill under `skills/*/SKILL.md` strictly conforms to the open **`agentskills.io`** specification consumed natively by `agensi.io`'s agent-gated MCP (`https://mcp.agensi.io`), with explicit negative boundaries and deterministic verification protocols.

### 3. Cursor / Windsurf / Copilot
Drop `.cursorrules` and `.cursor/rules/legal-analysis.mdc` into your workspace and configure `.mcp.json` (`uvx --from git+https://github.com/a-vip/lex-machina lex-machina-mcp` or the remote Cloudflare Workers Streamable HTTP endpoint).

---

## Deliverable Templates, Launch Kit & Licensing
- [**Live Interactive Legal Corpus Explorer (Zero Data Retention)**](https://a-vip.github.io/lex-machina/)
- [**Agensi, MCP Registry, Glama, Smithery & Enterprise ZDR Launch Kit**](AGENSI_LAUNCH_KIT.md)
- [**Formal Legal Opinion & Bitemporal Compliance Memorandum (FIRAC + ABA 512 Certificate)**](templates/legal_memorandum_template.md)
- [**Executive Board Briefing (2026–2028 Enforceability Timeline)**](templates/executive_briefing_template.md)
- **Dual License ([`LICENSE`](LICENSE))**: Free under **CC BY-NC 4.0** for academic researchers, universities, and NGOs; **Commercial Enterprise License** required for law firm client advisory and commercial deployments (`licensing@lex-machina.org`).
