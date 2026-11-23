# Lex Machina Pro v3.0 — Agensi, MCP Registry, Smithery, Glama & Enterprise Launch Kit

This document provides ready-to-use commercial distribution materials, verified live endpoints, registry submission steps, and the AmLaw 100 / Magic Circle IT Security procurement one-pager.

---

## Live Production Endpoints (Verified `HTTP 200` · Zero Data Retention)
- **Live Remote Streamable HTTP MCP Endpoint**: `https://lex-machina.aviperera0.workers.dev/mcp`
- **Live Edge Health Check**: `https://lex-machina.aviperera0.workers.dev/health`
- **Live Interactive Zero-Data-Retention Explorer**: `https://a-vip.github.io/lex-machina/`
- **Live 150-Case Benchmark Scorecard (`150/150 = 100.0%`)**: `https://raw.githubusercontent.com/a-vip/lex-machina/corpus/eval-scorecard.json`
- **GitHub Skills Repository**: `https://github.com/a-vip/lex-machina-skills`
- **GitHub Corpus & MCP Engine**: `https://github.com/a-vip/lex-machina`

---

## 1. Ready-to-Send Listing Copy for `agensi.io`

- **Title**: `Lex Machina Pro v3.0 — Planetary AI, Cyber, IHL & Case Law Agent Suite (27 Instruments · 150/150 Verified)`
- **Tagline**: *Bitemporal 2026 statutory auditing, binding CJEU/ICJ case law, concordance-aware token-level `git blame`, and deterministic ABA Formal Opinion 512 citation verification backed by a live 150/150 (100%) benchmark.*
- **Why AI Agents Pass It Through Quality Gating**:
  1. Prevents fatal 2025–2026 statutory errors frontier models make out of the box (EU Digital Omnibus `Regulation (EU) 2026/1744` high-risk postponements to Dec 2027 / Aug 2028; Jan 20, 2025 revocation of US EO 14110; Sept 11, 2026 CRA ENISA vulnerability reporting; Sept 1, 2025 China `GB 45438-2025` labeling; Texas TRAIGA Jan 1, 2026; South Korea AI Basic Act Jan 22, 2026; Japan AI Promotion Act Sept 1, 2025; Brazil `PL 2338/2023` pending-enactment trap).
  2. Pairs **6 concise `agentskills.io`-compliant `SKILL.md` files** (including binding **CJEU & ICJ Judicial Precedent Counsel** and **Planetary 9-Jurisdiction Crosswalk**, each with explicit positive and negative triggers) with a **deterministic `PostToolUse` citation verifier hook** (`scripts/verify_memo_citations.py`).
  3. Connects zero-install to the **live Cloudflare Edge MCP server** (`https://lex-machina.aviperera0.workers.dev/mcp`) backed by **1,831 indexed provisions** across **27 instruments** (**48/58 full verbatim primary stages**, SHA-256 hashed) verified continuously at **150 / 150 (100.0%)** by `LexMachina-Eval v3.0`.

---

## 2. Official Ecosystem Registry Submission Checklist

| Ecosystem | Manifest Already Included | Submission / Verification Action |
| :--- | :--- | :--- |
| **Cloudflare Edge Streamable HTTP** | Root `wrangler.jsonc` + `cloudflare_worker/` | **LIVE** at `https://lex-machina.aviperera0.workers.dev/mcp` (auto-deploys on `main` via Cloudflare Workers Builds) |
| **Agensi (`agensi.io`)** | `skills/*/SKILL.md` (`agentskills.io`) + `marketplace.json` | Submit `https://github.com/a-vip/lex-machina-skills` to `agensi.io` creator portal |
| **Claude Code Marketplace** | `.claude-plugin/plugin.json` + `.claude-plugin/marketplace.json` + `.mcp.json` + `hooks/hooks.json` | Users install via `/plugin marketplace add a-vip/lex-machina-skills` → `/plugin install lex-machina@lex-machina-marketplace` |
| **Official MCP Registry** | `lex-machina/server.json` (`io.github.a-vip/lex-machina`) | Publish `lex-machina-mcp` to PyPI (optional if using remote-only) and run `mcp-publisher publish` in `a-vip/lex-machina` via GitHub OAuth |
| **Glama (`glama.ai`)** | `lex-machina/glama.json` (`maintainers: ["a-vip"]`) | Submit `https://github.com/a-vip/lex-machina` on `glama.ai/mcp/servers` (ownership auto-verified via `glama.json`) |
| **Smithery (`smithery.ai`)** | `lex-machina/smithery.yaml` | Connect `a-vip/lex-machina` or `https://lex-machina.aviperera0.workers.dev/mcp` on `smithery.ai` |

---

## 3. AmLaw 100 / Magic Circle Procurement & Security One-Pager (ABA Formal Opinion 512)

| Ethics / Security Control | Lex Machina Pro v3.0 Architecture |
| :--- | :--- |
| **Model Rule 1.6 (Confidentiality / Zero Data Retention)** | **100% Stateless & Zero Data Retention (ZDR)**. Neither the live Cloudflare Edge MCP (`observability.enabled: false`, `X-Zero-Data-Retention: true`), the local `uvx` stdio server, nor the client-side GitHub Pages Explorer stores, logs, or trains on client prompts, case facts, or draft memoranda. |
| **Model Rule 1.1 & 3.3 (Competence & Candor / Zero Fabrication)** | Grounded in primary-source EUR-Lex CELLAR Akoma Ntoso XHTML, CJEU Formex XHTML, EC 2025 PDFs, UN ODS Symbol API PDFs, Texas enrolled HTML, PRC CAC official HTML, UK GOV.UK publications, and complete Geneva Conventions I–IV & AP I–II bound to **SHA-256 digests**. Missing clauses return `PROVISION NOT IN CORPUS`. `verify_citations` + `PostToolUse` hooks deterministically block fabricated articles, misquotes, revoked EO 14110, and premature Brazil PL 2338 claims. |
| **Model Rule 5.1 & 5.3 (Supervisory Auditability)** | Every generated memorandum embeds a standardized **ABA Formal Opinion 512 Verification Audit Certificate**, bitemporal enforceability dates, SHA-256 primary-source hashes, and an explicit Human-in-the-Loop attorney sign-off block. |
| **Independent Empirical Benchmarking** | Continuously verified on every corpus rebuild at **150 / 150 (100.0%)** by the open, preregistered **`LexMachina-Eval v3.0`** suite published live at `eval-scorecard.json` on `refs/heads/corpus` and accessible via `lex://eval-scorecard`. |

---

## 4. Recommended Monetization Tiers

1. **Community / Academic (Free — CC BY-NC 4.0)**: Public GitHub corpus (`a-vip/lex-machina`), open skills, and public community MCP endpoint. Builds institutional trust, law-school citations, and inbound organic traffic.
2. **Pro Solo / Boutique Legal Practitioner (\$39/mo via `agensi.io` / Edge API Key)**: Dedicated Zero-Data-Retention Cloudflare Workers Streamable HTTP endpoint (`ENTERPRISE_API_KEY` Bearer token), zero-install Claude/Cursor/ChatGPT connection, weekly automated corpus updates.
3. **Enterprise Law Firm / General Counsel (\$199–\$499/mo per practice group)**: Commercial client-billable license (`LICENSE`), dedicated private corpus branch syncing firm-specific jurisdictions and sectoral regulators, custom FIRAC templates, and SLA support.
