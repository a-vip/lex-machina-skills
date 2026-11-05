---
name: legislative-intent-detective
description: CJEU teleological and contextual statutory interpretation engine. Traces provisions across Commission proposals, Council general approaches, Parliament mandates, trilogue agreements, and Official Journal enactments with institutional git-blame attribution to reconstruct legislative intent (travaux préparatoires).
compatibility: claude-code, cursor, windsurf, copilot
tags: [travaux-preparatoires, legislative-intent, cjeu, statutory-interpretation, redline-diff, trilogue-blame]
---

# Skill: Travaux Préparatoires & Legislative Intent Detective

## Purpose & Doctrinal Background
In EU law and international treaty disputes, resolving statutory ambiguity requires looking beyond the literal wording to the **legislative history (*travaux préparatoires*)** and **teleological purpose (the *effet utile* of the measure)**. 

Under established Court of Justice of the European Union (CJEU) jurisprudence (e.g., *Cilfit*, Case 283/81; *Inuit Tapiriit Kanatami*, C-583/11 P), every provision of EU law must be interpreted in light of:
1. Its **grammatical wording** across official language versions;
2. Its **legislative context** (recitals and surrounding provisions);
3. The **historical development of the negotiations** (which institution introduced a phrase, what alternatives were rejected, and what compromise was sealed in Trilogue); and
4. Its **overarching regulatory objective** (*telos*).

This skill leverages the deterministic institutional Git commits in `lex-machina` to provide definitive, citation-backed statutory interpretation.

---

## Tool Integration via `lex-machina` MCP Server

1. **Querying Version Stages**:
   - `get_provision("eu/ai-act", "articles/article-005.md", as_of="commission_proposal")`: Check what the Commission originally proposed.
   - `get_provision("eu/ai-act", "articles/article-005.md", as_of="parliament_mandate")`: Identify European Parliament amendments.
   - `get_provision("eu/ai-act", "articles/article-005.md", as_of="council_general_approach")`: Identify Council security/defense carve-outs.
   - `get_provision("eu/ai-act", "articles/article-005.md", as_of="official_journal_final")`: Inspect final lawyer-linguist text.

2. **Unified Redline Diffs**:
   - `diff_provisions("eu/ai-act", "articles/article-005.md", "commission_proposal", "parliament_mandate")`: Highlight Parliament's aggressive expansion of prohibitions.
   - `diff_provisions("eu/ai-act", "articles/article-005.md", "parliament_mandate", "trilogue_provisional_agreement")`: Reveal Trilogue concessions.

3. **Institutional Authorship Attribution**:
   - `blame_provision("eu/ai-act", "articles/article-005.md")`: Identify line-by-line which institution (`commission@europa.eu`, `parliament@europa.eu`, `council@consilium.europa.eu`, `trilogue@europa.eu`) authored each sentence or exception.

---

## 4-Step Analytical Workflow

### Step 1: Baseline Legislative Tracing
Identify the focal provision and pull the statutory text across all 5 chronological stages:
- Stage 1: European Commission Proposal (`COM(2021) 206 final`, 21 April 2021)
- Stage 2: Council of the EU General Approach (`14954/22`, 6 December 2022)
- Stage 3: European Parliament Negotiating Mandate (`P9_TA(2023)0236`, 14 June 2023)
- Stage 4: Provisional Trilogue Agreement (`5662/24`, 26 January 2024)
- Stage 5: Final Official Journal Publication (`OJ L, 2024/1689`, 12 July 2024)

### Step 2: Redline Differential & Blame Analysis
Compute the delta between:
- **Proposal vs. Mandate**: Did Parliament seek a categorical ban or higher burden of proof?
- **Mandate vs. General Approach**: Where did Parliament and Council directly conflict?
- **Trilogue Compromise vs. Final Text**: How was the impasse resolved? What precise conditional language or derogation was drafted in the political trilogue?

### Step 3: Recital & Teleological Grounding
Correlate the operative article with its corresponding preamble recitals:
- For Article 5(1)(h) (Real-Time RBI) $\rightarrow$ Consult Recital 18.
- For Article 51/55 (General-Purpose AI Systemic Risk) $\rightarrow$ Consult Recital 111.
- For Article 27 (FRIA) $\rightarrow$ Consult Recital 96.
Explain how the recital clarifies the intent of the co-legislators regarding ambiguous terms (e.g., "reasonably foreseeable misuse", "materially distorting behaviour").

### Step 4: Synthesize the Doctrinal Memorandum
Structure the findings into a **Legislative History & Statutory Interpretation Opinion**:
1. **Ambiguity Identified**: Plain text reading and contested interpretations.
2. **Evolution Table**: Chronological text comparison table highlighting exact wording additions (`+`) and deletions (`-`).
3. **Institutional Attribution**: Which co-legislator introduced the disputed language and why (citing parliamentary committee reports or Council explanatory notes).
4. **Authoritative Conclusion**: The definitive interpretation most likely to be upheld by the Court of Justice of the European Union.
