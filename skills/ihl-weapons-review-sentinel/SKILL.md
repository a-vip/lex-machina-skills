---
name: ihl-weapons-review-sentinel
description: Conducts formal International Humanitarian Law (IHL) Article 36 Additional Protocol I legal reviews of new weapons, military AI, and autonomous weapons systems (LAWS) using the 1949 Geneva Conventions, 1977 Additional Protocols, and UN CCW GGE 2019-2026 frameworks. Use when reviewing autonomous targeting systems, military AI ethics, drone swarms, or CCW diplomatic proposals. Do NOT use for civilian commercial SaaS compliance under the EU AI Act (excluded by Article 2(3)).
license: CC-BY-NC-4.0 OR Commercial-Enterprise
compatibility: Requires lex-machina MCP server v2.0. Works in Claude Code, Cursor, Windsurf, Copilot, and Agensi.
metadata:
  author: Avi Perera / Lex Machina Consortium
  version: "2.0.0"
  domain: international-humanitarian-law
  jurisdiction: ihl-un
---

# IHL & Military AI Legal Weapons Review Sentinel (Article 36 AP I — v2.0)

## Operational Scope & 2026 Diplomatic Context
Operationalizes **Article 36 of Additional Protocol I (1977)** to the 1949 Geneva Conventions alongside customary IHL rules and the **UN CCW Group of Governmental Experts on LAWS** (2019 11 Guiding Principles, 2023 Two-Tier Consensus Report, and the **2024-2026 GGE mandate / CCW Seventh Review Conference outcome**, which codified operational characteristics of LAWS while deferring a binding treaty mandate amid major-power divisions).

---

## Mandatory `lex-machina` MCP Execution Sequence
1. **Fetch Binding IHL Treaty Provisions**: Call `get_provision("ihl/geneva-conventions", ...)` for `articles/article-001.md` (Common Art. 1 / Martens Clause), `article-035.md` (Basic Rules), `article-036.md` (New Weapons Review), `article-048.md` (Distinction), `article-051.md` (Indiscriminate Attacks & Proportionality), `article-057.md` (Precautions & Strike Cancellation), and `article-085.md` / `article-147.md` (Grave Breaches).
2. **Fetch UN CCW GGE Normative Evolution**: Call `get_provision("un/ccw-laws", ...)` across `guiding_principles_2019`, `rolling_text_report_2023`, and `seventh_review_conference_2026`.
3. **Demarcate Dual-Use Boundary**: Where a military system repurposes commercial GPAI/dual-use models, call `get_provision("eu/ai-act", "articles/article-002.md")` to delineate the Article 2(3) exclusive military exclusion vs. dual-use commercial supply-chain obligations.
4. **Verify All Citations**: Run `verify_citations(draft_text)` prior to delivery.

---

## 5-Pillar Legal Weapons Review Protocol (Consult `references/article_36_review_protocol.md`)
1. **Superfluous Injury & Martens Clause (AP I Art. 35 & Art. 1(2))**: Screen for prohibited payloads or inherently excessive suffering.
2. **Distinction & Sensor Integrity (AP I Arts. 48 & 51(4))**: Assess whether algorithmic targeting can distinguish combatants/military objectives from civilians and persons *hors de combat* under spoofing, adversarial camouflage, and degraded environments.
3. **Proportionality & Automation Bias (AP I Art. 51(5)(b))**: Evaluate whether human commanders possess sufficient explainability, time, and collateral damage estimation (CDE) visibility to judge proportionality without rubber-stamping ML outputs.
4. **Feasible Precautions & Positive Abort (AP I Art. 57(2)(a)-(b))**: Verify real-time strike cancellation/suspension, communications-denied fail-safes, and temporal/geographic bounding.
5. **CCW GGE Two-Tier & Lifecycle Retraining Review (CCW/GGE.1/2023/2 & 2026)**: Confirm Tier-1 prohibition screening, Tier-2 operational constraints, retained human command responsibility (Principle (b)), and mandatory **re-review whenever ML weights are significantly retrained**.

---

## Determination & Abstention Guardrails
- Conclude with an explicit legal determination: `APPROVED`, `APPROVED WITH BINDING OPERATIONAL RESTRICTIONS`, or `PROHIBITED UNDER IHL`.
- Never fabricate ICRC commentary citations or treaty articles; flag missing corpus text as `PROVISION NOT IN CORPUS`.
