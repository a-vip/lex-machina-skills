# Lex Machina Pro v3.0 — Planetary AI, Cyber, IHL & Case Law Agent Skills Suite

[![Validate Skills & Verifier Hook](https://github.com/a-vip/lex-machina-skills/actions/workflows/validate-skills.yml/badge.svg)](https://github.com/a-vip/lex-machina-skills/actions/workflows/validate-skills.yml)
[![Standard: agentskills.io](https://img.shields.io/badge/Spec-agentskills.io_v1-blue.svg)](https://agentskills.io)
[![Claude Code Plugin](https://img.shields.io/badge/Claude_Code-Native_Plugin-purple.svg)](.claude-plugin/plugin.json)
[![Agensi Compatible](https://img.shields.io/badge/Marketplace-agensi.io-teal.svg)](marketplace.json)
[![Engine: lex-machina v3.0](https://img.shields.io/badge/Corpus_Engine-a--vip%2Flex--machina-orange.svg)](https://github.com/a-vip/lex-machina)
[![ABA Formal Opinion 512](https://img.shields.io/badge/Ethics-ABA_Opinion_512_Guardrails-brightgreen.svg)](scripts/verify_memo_citations.py)

> **The only AI legal skill suite on Earth backed by 27 SHA-256-provenanced instruments across 5 continents, binding CJEU & ICJ case law, complete Geneva Conventions I–IV & AP I–II, bitemporal 2026 enforceability logic, concordance-aware token-level `git blame`, a deterministic ABA Formal Opinion 512 citation-verification hook, and a 150-case open empirical benchmark.**

---

## Why No Competitor on Earth Has Built This — And Why It Outperforms Every Alternative

Empirical evaluations by **Stanford RegLab** (*Journal of Empirical Legal Studies* 2025; *Benchmarking Legal RAG* 2026; *PNAS* 2026) revealed that even elite commercial legal AI platforms (**Lexis+ AI ~17%**, **Westlaw AI ~33%**) suffer severe **misgrounding** and score only **58%–64%** on multi-jurisdictional statutory surveys. Meanwhile, **SkillsBench (2026)** proved that curated, modular `agentskills.io` skills paired with deterministic verification scripts drive major accuracy gains over baseline models, whereas static prose prompts fail on edge cases.

**What makes `lex-machina-skills` v3.0 categorically superior to every legal skill, prompt pack, or MCP wrapper on the planet:**

1. **Catches Every 2025–2026 Planetary Statutory Trap**:
   - **EU AI Act Post-Digital Omnibus (`2026/1744`) + Official 2025 EC Guidelines PDFs**: Annex III deferred to **Dec 2, 2027**, Annex I to **Aug 2, 2028**; Art. 5 NCII/CSAM bans & Art. 50(2) legacy cutoff **Dec 2, 2026**.
   - **US Pivot Post-EO 14110**: Blocks stale citations to **revoked Executive Order 14110** (revoked Jan 20, 2025) and grounds US advice in verbatim enrolled **Texas TRAIGA (`HB 149`)**, **Colorado `SB 24-205` / `SB 26-189`**, **California `AB 2013` & `SB 53` (TFAIA)**, and NIST AI RMF.
   - **Global 2026 Regimes**: **China CAC verbatim Chinese statutes** (`GB 45438-2025`), **South Korea AI Basic Act** (effective Jan 22, 2026), **Japan AI Promotion Act** (effective Sept 1, 2025), **UK DUAA 2025 & AISI**, **Singapore IMDA Agentic AI Framework (2026)**, **Brazil PL 2338/2023** (blocks treating pending bill as enacted law!), and **ISO/IEC 42001:2023**.
   - **Cyber Law Pillar**: EU CRA (`2024/2847`, Art. 14 live Sept 11, 2026), NIS2, DORA (*lex specialis*), Budapest (`ETS 185`/`CETS 224`), and UN Hanoi Cybercrime Convention (full 68 arts, 40-ratification gate).
2. **Binding Judicial Precedent Skill (`cjeu-icj-precedent-counsel`)**:
   - Grounds litigation and advisory briefs directly in verbatim EUR-Lex CELLAR & UN ODS rulings: **CJEU *SCHUFA* (`C-634/21`)**, ***Schrems II* (`C-311/18`)**, ***Meta v Bundeskartellamt* (`C-252/21`)**, ***La Quadrature du Net* (`C-511/18`)**, and **ICJ *Nuclear Weapons 1996* (`A/51/218`)**.
3. **Deterministic Hard Guardrail (`PostToolUse` Hook + `verify_citations`)**:
   - Zero-dependency verifier ([`scripts/verify_memo_citations.py`](scripts/verify_memo_citations.py)) wired into Claude Code [`hooks/hooks.json`](hooks/hooks.json) rejecting fabricated article citations across 10 statutes/treaties, revoked EO 14110 claims, pre-Omnibus Annex III dates, and Brazil PL 2338 premature-enactment claims.

---

## The Six Institutional Skills (`skills/`)

| # | Skill | Domain & 2026 Authority | Core Differentiator |
| :- | :--- | :--- | :--- |
| 1 | [**`eu-ai-act-auditor`**](skills/eu-ai-act-auditor/SKILL.md) | EU AI Act (`2024/1689`) + **Digital Omnibus (`2026/1744`)** + 2025 EC Guidelines PDFs | Bitemporal `check_applicability` gate + Art. 6(3) profiling override + verified Art. 73 clocks |
| 2 | [**`legislative-intent-detective`**](skills/legislative-intent-detective/SKILL.md) | CJEU Teleological & VCLT *Travaux Préparatoires* | 4-column renumbering concordance + token-level institutional `git blame` + linked recitals |
| 3 | [**`ihl-weapons-review-sentinel`**](skills/ihl-weapons-review-sentinel/SKILL.md) | **Geneva Conventions I–IV (1949), AP I & AP II (1977), ICJ 1996 & UN CCW LAWS (2019–2026)** | 5-pillar weapons review + Martens Clause ICJ precedent + NIAC AP II + ML retraining mandate |
| 4 | [**`transatlantic-regulatory-crosswalk`**](skills/transatlantic-regulatory-crosswalk/SKILL.md) | **Planetary 9-Jurisdiction Crosswalk (EU / US / China / UK / Korea / Japan / Brazil / Singapore / ISO 42001)** | Build-once ISO 42001/NIST controls + blocks EO 14110 & Brazil PL 2338 traps |
| 5 | [**`cyber-treaty-compliance-auditor`**](skills/cyber-treaty-compliance-auditor/SKILL.md) | **EU CRA (`2024/2847`), NIS2, DORA, UN Hanoi Cybercrime & Budapest Conventions** | Harmonizes CRA ENISA clocks, DORA *lex specialis*, AI Act Art. 15 interlock & treaty risk |
| 6 | [**`cjeu-icj-precedent-counsel`**](skills/cjeu-icj-precedent-counsel/SKILL.md) | **CJEU (*SCHUFA*, *Schrems II*, *Meta*, *La Quadrature du Net*) & ICJ (*Nuclear Weapons 1996*)** | Verbatim CELLAR/UN Operative Part grounding wired into statutory citation graphs |

---

## 1-Click Installation Across Every Major AI Agent Platform

### 1. Claude Code (Native Plugin Marketplace — Recommended)
```bash
/plugin marketplace add a-vip/lex-machina-skills
/plugin install lex-machina@lex-machina-marketplace
```
Installs all 6 skills, the `lex-machina` MCP server (`.mcp.json`), and the automatic ABA Formal Opinion 512 `PostToolUse` citation verifier hook (`hooks/hooks.json`).

### 2. Agensi (`agensi.io`) & Cursor / Windsurf / Copilot
Every skill under `skills/*/SKILL.md` strictly conforms to **`agentskills.io`**, with explicit positive and negative (`Do NOT use`) triggers and deterministic verification scripts.

---

## Deliverable Templates, Launch Kit & Licensing
- [**Live Interactive Legal Corpus Explorer (Zero Data Retention)**](https://a-vip.github.io/lex-machina/)
- [**Agensi, MCP Registry, Glama, Smithery & Enterprise ZDR Launch Kit**](AGENSI_LAUNCH_KIT.md)
- [**Formal Legal Opinion & Bitemporal Compliance Memorandum (FIRAC + ABA 512 Certificate)**](templates/legal_memorandum_template.md)
- [**Executive Board Briefing (2026–2028 Enforceability Timeline)**](templates/executive_briefing_template.md)
- **Dual License ([`LICENSE`](LICENSE))**: Free under **CC BY-NC 4.0** for academic researchers, universities, and NGOs; **Commercial Enterprise License** required for law firm client advisory and commercial deployments (`licensing@lex-machina.org`).
