# Lex Machina Pro v2.1 — Agensi, MCP Registry, Smithery, Glama & Enterprise Launch Kit

This document provides ready-to-use commercial distribution materials, registry submission commands, and the AmLaw 100 / Magic Circle IT Security procurement one-pager.

---

## 1. Ready-to-Send Listing Copy for `agensi.io`

- **Title**: `Lex Machina Pro — Institutional AI, Cyber & International Law Suite (EU AI Act 2026 + CRA/NIS2/DORA + IHL Art. 36)`
- **Tagline**: *Bitemporal statutory auditing, concordance-aware institutional `git blame`, and deterministic ABA Formal Opinion 512 citation verification backed by a live 120-case benchmark.*
- **Why AI Agents Pass It Through Quality Gating**:
  1. Prevents fatal 2025–2026 statutory errors frontier models make out of the box (EU Digital Omnibus `Regulation (EU) 2026/1744` high-risk postponements to Dec 2027 / Aug 2028; Jan 20, 2025 revocation of US EO 14110; Sept 11, 2026 CRA ENISA vulnerability reporting; Sept 1, 2025 China `GB 45438-2025` labeling; Texas TRAIGA Jan 1, 2026).
  2. Pairs 5 concise `agentskills.io`-compliant `SKILL.md` files (with explicit positive and negative triggers) with a **deterministic `PostToolUse` citation verifier hook** (`scripts/verify_memo_citations.py`).
  3. Connects to the full-text SHA-256-hashed **`a-vip/lex-machina`** MCP server (1,400+ live verbatim primary provisions from EUR-Lex CELLAR, UN/CoE/NIST PDFs, and Geneva Conventions/AP I) verified continuously by a **120-case open benchmark (`LexMachina-Eval`)**.
- **Interactive Live Demo URL**: `https://a-vip.github.io/lex-machina/`
- **GitHub Skills Repository**: `https://github.com/a-vip/lex-machina-skills`
- **GitHub Corpus & MCP Engine**: `https://github.com/a-vip/lex-machina`

---

## 2. Official Ecosystem Registry Submission Checklist

| Ecosystem | Manifest Already Included | Submission / Verification Action |
| :--- | :--- | :--- |
| **Agensi (`agensi.io`)** | `skills/*/SKILL.md` (`agentskills.io`) + `marketplace.json` | Submit `https://github.com/a-vip/lex-machina-skills` to `agensi.io` creator portal |
| **Claude Code Marketplace** | `.claude-plugin/plugin.json` + `.claude-plugin/marketplace.json` + `.mcp.json` + `hooks/hooks.json` | Users install via `/plugin marketplace add a-vip/lex-machina-skills` → `/plugin install lex-machina@lex-machina-marketplace` |
| **Official MCP Registry** | `lex-machina/server.json` (`io.github.a-vip/lex-machina`) | Run `mcp-publisher publish` in `a-vip/lex-machina` using GitHub OAuth |
| **Glama (`glama.ai`)** | `lex-machina/glama.json` (`maintainers: ["a-vip"]`) | Submit `https://github.com/a-vip/lex-machina` on `glama.ai/mcp/servers` (ownership auto-verified via `glama.json`) |
| **Smithery (`smithery.ai`)** | `lex-machina/smithery.yaml` | Connect `a-vip/lex-machina` on `smithery.ai` for 1-click CLI installation |
| **Cloudflare Edge Streamable HTTP** | `lex-machina/cloudflare_worker/` + `04-deploy-edge-mcp.yml` | Add `CLOUDFLARE_API_TOKEN` & `CLOUDFLARE_ACCOUNT_ID` secrets in `a-vip/lex-machina` and trigger `04-deploy-edge-mcp.yml` |

---

## 3. AmLaw 100 / Magic Circle Procurement & Security One-Pager (ABA Formal Opinion 512)

| Ethics / Security Control | Lex Machina Pro Architecture |
| :--- | :--- |
| **Model Rule 1.6 (Confidentiality / Zero Data Retention)** | **100% Stateless & Zero Data Retention (ZDR)**. Neither the local `uvx` stdio server, the Cloudflare Workers Edge MCP (`observability.enabled: false`), nor the static GitHub Pages Explorer stores, logs, or trains on client prompts, case facts, or draft memoranda. |
| **Model Rule 1.1 & 3.3 (Competence & Candor / Zero Fabrication)** | All statutory lookups execute against primary-source EUR-Lex CELLAR Akoma Ntoso XHTML, Consilium/UN/CoE/NIST PDFs, and Geneva Conventions texts bound to **SHA-256 digests**. Missing clauses return `PROVISION NOT IN CORPUS`. `verify_citations` + `PostToolUse` hooks deterministically block out-of-range articles, misquotes, and revoked statutes before attorney delivery. |
| **Model Rule 5.1 & 5.3 (Supervisory Auditability)** | Every generated memorandum embeds a standardized **ABA Formal Opinion 512 Verification Audit Certificate**, bitemporal enforceability dates, SHA-256 primary-source hashes, and an explicit Human-in-the-Loop attorney sign-off block. |
| **Independent Empirical Benchmarking** | Continuously tested on every corpus rebuild by the open, preregistered **120-case `LexMachina-Eval` suite** (published live at `eval-scorecard.json` on `refs/heads/corpus`). |

---

## 4. Recommended Monetization Tiers

1. **Community / Academic (Free — CC BY-NC 4.0)**: Public GitHub corpus (`a-vip/lex-machina`), open skills, and self-hosted `uvx` MCP. Builds institutional trust, law-school citations, and inbound organic traffic.
2. **Pro Solo / Boutique Legal Practitioner (\$39/mo via `agensi.io` / Edge API Key)**: Hosted Zero-Data-Retention Cloudflare Workers Streamable HTTP endpoint (`ENTERPRISE_API_KEY` Bearer token), zero-install Claude/Cursor/ChatGPT connection, weekly automated corpus updates.
3. **Enterprise Law Firm / General Counsel (\$199–\$499/mo per practice group)**: Commercial client-billable license (`LICENSE`), dedicated private corpus branch syncing firm-specific jurisdictions (e.g., UK/Singapore/Brazil/sectoral FDA/FINRA), custom FIRAC templates, and SLA support.
