# WebExpo 2026 transfer prototype

Working title: **AI for student projects: from messy information to reliable decisions**

This is a lecturer-reviewable prototype for a possible contribution back to the UCT Prague Technology Skills for Project Managers class after attending WebExpo 2026.

The goal is not to teach bioinformatics only. The goal is to translate AI/data lessons from WebExpo into a practical workflow that students from different specializations can use in project work.

## Audience

Mixed-specialization students: project management, business, chemistry, science, IT, design, economics, bioinformatics, and other backgrounds.

The activity has two paths:

- **No-code path:** spreadsheet + AI assistant + validation checklist.
- **Optional technical path:** small Python script + AI coding assistant for students who code.

## Core workflow

1. Define the project question before using AI.
2. Prepare context: data source, assumptions, constraints, and expected output.
3. Use AI to structure messy information, summarize patterns, or draft a decision brief.
4. Validate the output manually.
5. Convert the result into a project decision brief.
6. Document how AI was used.

## Prototype dataset

Recommended default: **Open Food Facts**.

Why this dataset works for a mixed class:

- It is real-world and public.
- It is understandable without specialist knowledge.
- It connects nutrition, chemistry, biology, consumer products, marketing, data quality, and decision-making.
- It is messy enough to show why AI output must be validated.
- It supports both no-code and technical analysis.

Example question:

> Which product category appears less healthy based on available nutrition fields, and how confident can we be given missing or inconsistent data?

Possible fields for a small teaching sample:

- product_name
- categories
- countries
- nutriscore_grade
- energy-kcal_100g
- sugars_100g
- salt_100g
- saturated-fat_100g
- proteins_100g
- ingredients_text

Backup dataset options:

- **World Bank indicators:** useful for policy, economics, and management examples.
- **Our World in Data energy/climate data:** useful for sustainability and analytics-noise examples.

## Proposed 35-minute class activity

### 0-5 min: framing

Message: AI is not the deliverable. The deliverable is a defensible project decision.

Students see the workflow:

> question -> context -> AI help -> validation -> decision brief

### 5-12 min: real-world data demo

Use a small Open Food Facts sample. Students inspect basic columns and missing values.

No-code task:

Ask an AI tool to identify likely product groups, missing-data problems, and first hypotheses.

### 12-20 min: validation layer

Students check:

- Did the AI invent values?
- Did it ignore missing data?
- Did it compare categories unfairly?
- Did it overstate certainty?
- Did it confuse correlation, ranking, and causation?
- Is the conclusion useful for a project decision?

### 20-28 min: project decision brief

Students turn the output into a short decision brief:

- objective;
- data used;
- AI help used;
- findings;
- limitations;
- recommendation;
- next action.

### 28-35 min: optional technical extension

Students who code use Codex, Gemini Code Assist, GitHub Copilot, Cursor, or another coding assistant to create or review a small Python script that cleans the data and produces a summary table.

Non-coders improve the prompt, validation checklist, or decision brief.

## Student-facing prompts

### Prompt 1: clarify the question

```text
We are working on a student project using this dataset description and these columns: [paste columns].
Our goal is: [paste goal].
Before analyzing, identify:
1. the main decision we need to support,
2. what the data can and cannot answer,
3. missing context,
4. risks if we over-trust the AI output.
```

### Prompt 2: summarize messy data

```text
Here is a sample of product data: [paste rows].
Summarize visible patterns, but separate:
- facts directly visible in the data,
- assumptions,
- possible explanations,
- things that require verification.
Do not invent missing values.
```

### Prompt 3: validation reviewer

```text
Act as a critical reviewer of this AI-assisted analysis: [paste analysis].
Find unsupported claims, missing assumptions, data quality problems, possible bias, and places where a human should verify the result.
```

### Prompt 4: project brief

```text
Turn the validated findings into a one-page project decision brief with:
objective, data source, method, findings, limitations, recommendation, and next action.
Use language understandable to non-technical teammates.
```

### Prompt 5: optional technical path

```text
Review this small Python analysis script and suggest improvements for readability, missing-value handling, reproducibility, and documentation. Do not change the scientific interpretation unless the data supports it.
```

## Tool options

| Use case | Low-cost/default options | Notes |
|---|---|---|
| General no-code AI help | ChatGPT Free, Gemini Free | Good for structuring notes, prompts, summaries, and project briefs. |
| Source-grounded work | NotebookLM | Useful when students upload a controlled set of sources. |
| Quick sourced research | Perplexity Free, ChatGPT/Gemini with web access where available | Use for orientation, not final truth. |
| Spreadsheet work | Excel, Google Sheets, LibreOffice Calc | Good for non-coders. |
| Coding assistant | Codex in ChatGPT, Gemini Code Assist, GitHub Copilot Free | Good for small scripts, README generation, and code review. |
| Advanced coding assistant | Claude Code, Cursor, Copilot Pro | Stronger for real codebases, but not required for the basic lesson. |

## Connection to WebExpo

This prototype connects to WebExpo topics around:

- AI and messy data;
- reducing analytics noise;
- preparing projects/codebases for AI agents;
- AI in product/project management;
- evidence-led decisions rather than AI hype.

If selected for the ticket, the conference goal would be to collect practical lessons from these topics and refine this prototype into a short hands-on class activity and checklist.

## Application-safe note

This repository content is planning material only. The final WebExpo application should not be copied from AI-generated text. It should be recorded as a natural 2-minute video in the applicant's own words.
