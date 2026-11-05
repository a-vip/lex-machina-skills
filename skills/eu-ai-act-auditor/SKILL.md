---
name: eu-ai-act-auditor
description: Institutional-grade compliance auditing and risk classification against Regulation (EU) 2024/1689 (EU AI Act). Audits prohibited practices (Article 5), high-risk classification (Article 6 and Annex III), Fundamental Rights Impact Assessments (Article 27), transparency duties (Article 50), and General-Purpose AI model obligations (Articles 51-55).
compatibility: claude-code, cursor, windsurf, copilot
tags: [eu-ai-act, compliance, risk-classification, prohibited-practices, gpai, gdpr]
---

# Skill: EU AI Act Compliance & Risk Classification Sentinel

## Mission & Scope
This skill equips the agent to conduct rigorous, partner-level compliance reviews of artificial intelligence systems and general-purpose AI (GPAI) models against **Regulation (EU) 2024/1689** of the European Parliament and of the Council (the EU AI Act), published in the Official Journal on 12 July 2024 (OJ L, 2024/1689, CELEX 32024R1689).

---

## Tool Integration via `lex-machina` MCP Server
To ensure 100% statutory precision without hallucination, query the following remote tools:
- `get_provision("eu/ai-act", "articles/article-005.md")`: Retrieve the exact text of prohibited AI practices.
- `get_provision("eu/ai-act", "articles/article-006.md")`: Retrieve classification rules for high-risk systems.
- `get_provision("eu/ai-act", "annexes/annex-iii.md")`: Retrieve high-risk use cases across critical sectors.
- `get_provision("eu/ai-act", "articles/article-027.md")`: Fundamental Rights Impact Assessment rules.
- `get_provision("eu/ai-act", "articles/article-050.md")`: Transparency obligations for synthetic/generative AI.
- `get_provision("eu/ai-act", "articles/article-051.md")`: GPAI systemic risk criteria ($10^{25}$ FLOPs).
- `get_provision("eu/ai-act", "articles/article-053.md")`: GPAI provider obligations (copyright & training summaries).
- `get_provision("eu/ai-act", "articles/article-055.md")`: GPAI systemic risk mitigations (adversarial red-teaming).
- `diff_provisions("eu/ai-act", "articles/article-005.md", "parliament_mandate", "official_journal_final")`: Verify the evolution of prohibitions.

---

## Standard 5-Step Audit Protocol

### Step 1: Material and Territorial Scope Check (Article 2)
1. **Territorial Nexus**: Does the provider or deployer place AI on the EU market, put it into service in the EU, or do the system's outputs affect natural persons in the EU (Art. 2(1))?
2. **Exclusions**:
   - Developed or used exclusively for military, defense, or national security purposes (Art. 2(3)).
   - Pure scientific research and development before commercial deployment (Art. 2(6)).
   - Personal non-professional activity by natural persons (Art. 2(10)).
   - Free and open-source software, unless high-risk, prohibited, or subject to transparency/GPAI rules (Art. 2(12)).

### Step 2: Article 5 Prohibited Practices Audit (The Unacceptable Risk Gate)
Run the target system through the 8 statutory prohibitions. A positive finding under any sub-clause mandates **immediate prohibition**:
1. **Subliminal / Purposefully Manipulative Techniques (Art. 5(1)(a))**: Does it distort behavior impairing informed decisions, causing significant harm?
2. **Exploitation of Vulnerabilities (Art. 5(1)(b))**: Does it exploit age, disability, or specific social/economic situations?
3. **Social Scoring (Art. 5(1)(c))**: Does it evaluate or classify trustworthiness leading to unjustified or out-of-context detrimental treatment?
4. **Individual Criminal Offence Profiling (Art. 5(1)(d))**: Does it assess criminal risk based solely on profiling without verifiable facts?
5. **Untargeted Facial Scraping (Art. 5(1)(e))**: Does it create/expand databases via untargeted scraping of the internet or CCTV?
6. **Emotion Recognition in Workplace / Education (Art. 5(1)(f))**: Does it infer emotions in work or school settings (unless for medical/safety reasons)?
7. **Biometric Categorisation for Sensitive Attributes (Art. 5(1)(g))**: Does it deduce race, political opinions, union membership, religion, or sex life?
8. **Real-Time Remote Biometric Identification (RBI) in Public Spaces (Art. 5(1)(h))**: Prohibited for law enforcement unless strictly necessary for targeted search of victims/missing persons, imminent terror threats, or specific serious crimes listed in Annex II with prior judicial authorization.

### Step 3: High-Risk Classification & Derogation Analysis (Article 6 & Annex III)
1. **Product Safety Components (Art. 6(1))**: Is it a safety component of machinery, medical devices, toys, aviation, or vehicles subject to Annex I third-party conformity assessment?
2. **Critical Standalone Systems (Art. 6(2) & Annex III)**:
   - Area 1: Biometrics (remote identification, emotion recognition, categorization).
   - Area 2: Critical infrastructure (digital infrastructure, water, gas, electricity, road traffic).
   - Area 3: Education & vocational training (admissions, evaluation, proctoring).
   - Area 4: Employment & worker management (recruitment, promotion, termination, monitoring).
   - Area 5: Essential private & public services (credit scoring, life/health insurance, emergency dispatch).
   - Area 6: Law enforcement (polygraphs, evidence evaluation, profiling).
   - Area 7: Migration, asylum, and border control (automated visa assessment, travel document verification).
   - Area 8: Administration of justice & democratic processes (judicial research/sentencing support, voting influence).
3. **The Article 6(3) Accessory Derogation**:
   - An Annex III system is *not* high-risk if it does not pose significant risk and meets one of four conditions:
     (a) Performs a narrow procedural task;
     (b) Improves the result of a previously completed human activity;
     (c) Detects decision-making patterns without replacing human evaluation;
     (d) Performs a purely preparatory task.
   - **CRITICAL OVERRIDE**: If the system performs **profiling** of natural persons, it is **always high-risk**; the derogation cannot apply!

### Step 4: General-Purpose AI (GPAI) Model Obligations (Articles 51–55)
1. **Definition (Art. 3(63))**: Does the model display significant generality and competence across a wide range of distinct tasks?
2. **Systemic Risk Threshold (Art. 51)**:
   - Does cumulative compute exceed $10^{25}$ FLOPs? If yes, it is legally presumed to pose systemic risk.
   - Has the European Commission classified it as possessing high-impact capabilities?
3. **Tier 1 Obligations (All GPAI Providers - Art. 53)**:
   - Technical documentation for AI Office (Annex XI).
   - Information documentation for downstream system providers (Annex XII).
   - Copyright policy complying with Directive (EU) 2019/790 Art. 4(3) opt-out reservations.
   - Publicly available sufficiently detailed summary of training content.
4. **Tier 2 Obligations (GPAI with Systemic Risk - Art. 55)**:
   - Standardized model evaluation and adversarial red-teaming.
   - Assessment and mitigation of systemic risks at Union level.
   - Serious incident tracking and mandatory reporting to the AI Office within 72 hours.
   - State-of-the-art cybersecurity protections for model weights and physical infrastructure.

### Step 5: Transparency and Deployer Duties (Articles 27 & 50)
1. **Article 50 Transparency**:
   - Clear disclosure to natural persons when interacting directly with an AI system.
   - Synthetic audio, image, video, or text must be marked in a machine-readable format and detectable.
   - Conspicuous disclosure of deep fakes or public-interest AI-generated text.
2. **Article 27 Fundamental Rights Impact Assessment (FRIA)**:
   - Mandatory for public bodies and private deployers of high-risk essential public services (credit scoring, life/health insurance).

---

## Deliverable Format
Always present findings in a structured **Formal Legal Compliance Memorandum** using the template at `templates/legal_memorandum_template.md`.
