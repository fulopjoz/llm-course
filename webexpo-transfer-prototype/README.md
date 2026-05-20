# WebExpo 2026 transfer prototype

Working title: **AI for student projects: from messy information to reliable decisions**

This is a lecturer-reviewable prototype for a possible contribution back to the UCT Prague Technology Skills for Project Managers class after attending WebExpo 2026.

The goal is not to teach bioinformatics only. The goal is to translate AI/data lessons from WebExpo into a practical workflow that students from different specializations can use in project work.

## Start here

Begin with:

```text
START_HERE.md
```

The default student route is **no-code**.

Students do not need GitHub, Python, Claude Code, Codex, Copilot, Cursor, or paid tools to complete the main activity. GitHub is used here only to host the prototype and make it easy to review. In a real class, the same files can be shared through Teams, a ZIP file, or a course folder.

Minimum student tools:

1. Excel, Google Sheets, or LibreOffice Calc.
2. One AI chat assistant such as ChatGPT, Gemini, or Claude.
3. The provided CSV file.

## Audience

Mixed-specialization students: project management, business, chemistry, science, IT, design, economics, bioinformatics, and other backgrounds.

The activity has two routes:

- **Required no-code route:** spreadsheet + AI assistant + validation checklist.
- **Optional technical route:** small Python script + AI coding assistant for students who already code or want to try.

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

Fields used in the teaching sample:

- product_name
- categories
- countries
- nutriscore_grade
- energy_kcal_100g
- sugars_100g
- salt_100g
- saturated_fat_100g
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

Use a small Open Food Facts-style sample. Students inspect basic columns and missing values in a spreadsheet.

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

Students who code can use Codex, Gemini Code Assist, GitHub Copilot, Cursor, Claude Code, or another coding assistant to explain or review a small Python script that produces a summary table.

Non-coders improve the prompt, validation checklist, or decision brief.

## Student-facing prompts

Use `prompts/prompt_pack.md` for the full prompt set.

Core prompt pattern:

```text
Context: I am a student using a small public food-products dataset.
Task: Help me identify visible patterns and data-quality risks.
Constraints: Do not invent values. Separate facts from assumptions. Do not make medical claims.
Output: Give me a short list of patterns and a validation checklist.
```

## Tool options

| Use case | Low-cost/default options | Required? | Notes |
|---|---|---:|---|
| Spreadsheet inspection | Excel, Google Sheets, LibreOffice Calc | Yes | Main tool for checking data manually. |
| General no-code AI help | ChatGPT, Gemini, Claude | Yes, choose one | Good for structuring notes, prompts, summaries, and project briefs. |
| Source-grounded work | NotebookLM | Optional | Useful when students upload a controlled set of course files. |
| Quick sourced research | Perplexity or browser search | Optional | Use for orientation, not final truth. |
| Coding assistant | Codex, Gemini Code Assist, GitHub Copilot, Cursor | Optional technical | Good for explaining or reviewing the optional Python script. |
| Advanced coding assistant | Claude Code | Advanced optional | Powerful for code projects, but not needed for the main activity. |
| GitHub | Repository hosting | Not required for students | Used here only to host the prototype. |

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
