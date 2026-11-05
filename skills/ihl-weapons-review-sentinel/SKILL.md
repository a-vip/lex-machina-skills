---
name: ihl-weapons-review-sentinel
description: International Humanitarian Law (IHL) and military AI legal review sentinel. Operationalizes Article 36 of Additional Protocol I to the 1949 Geneva Conventions, customary IHL rules (distinction, proportionality, precautions in attack), and UN CCW GGE Guiding Principles on Lethal Autonomous Weapons Systems (LAWS).
compatibility: claude-code, cursor, windsurf, copilot
tags: [ihl, geneva-conventions, article-36-weapons-review, laws, autonomous-weapons, ccw-gge, customary-ihl]
---

# Skill: IHL & Military AI Legal Review Sentinel (Article 36 AP I)

## Operational Scope & Doctrinal Authority
Under **Article 36 of Protocol Additional I (AP I) to the Geneva Conventions of 12 August 1949**:
> *"In the study, development, acquisition or adoption of a new weapon, means or method of warfare, a High Contracting Party is under an obligation to determine whether its employment would, in some or all circumstances, be prohibited by this Protocol or by any other rule of international law applicable to the High Contracting Party."*

This skill equips legal advisors, defense policy analysts, and multilateral delegations to conduct systematic legal reviews of autonomous weapons systems (LAWS), algorithmic targeting suites, autonomous drone swarms, and AI-enabled battle management systems.

---

## Tool Integration via `lex-machina` MCP Server

- `get_provision("ihl/geneva-conventions", "articles/article-035.md")`: Basic rules on methods and means of warfare (superfluous injury / unnecessary suffering).
- `get_provision("ihl/geneva-conventions", "articles/article-036.md")`: Mandatory legal weapons review requirement.
- `get_provision("ihl/geneva-conventions", "articles/article-048.md")`: Basic rule of distinction.
- `get_provision("ihl/geneva-conventions", "articles/article-051.md")`: Prohibition of indiscriminate attacks and proportionality test.
- `get_provision("ihl/geneva-conventions", "articles/article-057.md")`: Precautions in attack and mandatory cancellation of strikes.
- `get_provision("un/ccw-laws", "articles/article-001.md", as_of="guiding_principles_2019")`: 11 Guiding Principles on LAWS.
- `get_provision("un/ccw-laws", "articles/article-002.md", as_of="rolling_text_report_2023")`: CCW GGE consensus report & two-tier normative prohibition framework.

---

## Standard 5-Pillar Legal Weapons Review Protocol

### Pillar 1: Superfluous Injury & Unnecessary Suffering (AP I Article 35(2))
- Does the system employ means or methods of warfare of a nature to cause superfluous injury or unnecessary suffering?
- Does it utilize prohibited mechanisms (e.g., exploding bullets, blinding lasers, non-detectable fragments)?

### Pillar 2: The Principle of Distinction (AP I Articles 48 & 51(4))
- **Positive Verification**: Can the system reliably distinguish between combatants / military objectives and civilians / civilian objects in its intended operational environment?
- **Indiscriminate by Nature (Art. 51(4)(b)–(c))**: Is the system incapable of being directed at a specific military objective, or do its algorithmic effects fail to be limited as required by IHL?
- **Sensor & Dataset Integrity**: Are computer vision / acoustic / RF sensors resilient against spoofing, adversarial perturbations, weather obscuration, and false positives in civilian-dense areas?

### Pillar 3: Proportionality and Incidental Loss Evaluation (AP I Article 51(5)(b))
- Can human commanders reasonably assess and anticipate incidental loss of civilian life, injury to civilians, and damage to civilian objects?
- Does the system allow human operators to determine whether incidental harms are excessive in relation to the concrete and direct military advantage anticipated?
- **Automation Bias Safeguards**: Are human operators provided sufficient decision time, interface explainability, and situational awareness to avoid rubber-stamping algorithmic targeting recommendations?

### Pillar 4: Feasible Precautions in Attack (AP I Article 57)
- Does the system enable human operators to do everything feasible to verify that objectives are not civilian (Art. 57(2)(a)(i))?
- Does the system maintain an accessible, real-time abort, suspend, or cancel mechanism if an objective ceases to be a valid military target (Art. 57(2)(b))?
- Are fail-safe, self-destruct, self-deactivation, or return-to-base routines guaranteed if communications are severed?

### Pillar 5: CCW GGE Two-Tier Normative Compliance (CCW/GGE.1/2023/2)
- **Tier 1 (Prohibited Weapons Systems)**:
  - Systems that cannot be used in compliance with IHL must be prohibited from development, acquisition, and use.
  - Systems where force is applied without any meaningful human control or understandability are prohibited.
- **Tier 2 (Regulated Weapons Systems)**:
  - Explicit limits on the types of targets (e.g., material only vs. personnel).
  - Explicit limits on temporal duration, geographic area, and operational scope.
  - Guaranteed human-machine interaction, understandability, and audit trails.

---

## Deliverable Format
Generate a formal **Article 36 National Legal Weapons Review Memorandum** stating:
1. Operational Parameters & Target Profile
2. IHL Compliance Findings (Distinction, Proportionality, Precautions)
3. Human-Machine Interaction Assessment (Meaningful Human Control)
4. Legal Determination: Approved without reservation / Approved with operational restrictions / Prohibited under International Law.
