# 02 - Tool setup

## Goal of this module

Choose tools that match your skill level. You do not need expensive tools, GitHub, Python, or programming experience to complete the required course activity.

## Minimum setup for everyone

Use this if you are a beginner or non-technical student.

1. Spreadsheet app:
   - Google Sheets;
   - Microsoft Excel;
   - LibreOffice Calc.
2. One AI chat assistant:
   - ChatGPT;
   - Gemini;
   - Claude;
   - or another assistant available to you.
3. Course dataset:
   - `data/sample_food_products.csv`.

This is enough for the required activity.

## Optional tools

These tools can help, but they are not required.

| Tool | Use in this course | Required? | Beginner suitability |
|---|---|---:|---|
| ChatGPT / Gemini / Claude web chat | Ask questions, structure analysis, draft checklist, improve wording | Choose one | High |
| Excel / Google Sheets / LibreOffice | Open CSV, filter rows, check values manually | Yes | High |
| NotebookLM | Ask questions over uploaded course files or notes | No | Medium-high |
| Perplexity / browser search | Quick sourced orientation | No | Medium |
| Codex | Explain or review the optional Python script | No | Medium for technical students |
| Gemini Code Assist | Explain or review code | No | Medium for technical students |
| GitHub Copilot | Code suggestions in an editor | No | Medium; requires setup/account |
| Cursor | AI coding editor | No | Medium; mainly for coders |
| Claude Code | Advanced terminal coding agent | No | Low for beginners; advanced only |
| GitHub | Hosting and version control | No | Not needed for the main activity |

## Recommended setup by student type

### Student with no coding background

Use:

- Google Sheets or Excel;
- ChatGPT, Gemini, or Claude.

Do not start with GitHub, Python, Codex, Claude Code, Copilot, or Cursor.

### Student who wants stronger source control

Use:

- Spreadsheet;
- NotebookLM;
- the course files and dataset notes.

This is useful if you want the AI tool to answer from a controlled set of uploaded materials instead of relying on general web knowledge.

### Student with some coding experience

Use:

- Python;
- pandas;
- VS Code or another editor;
- Codex, Gemini Code Assist, GitHub Copilot, Cursor, or Claude Code if available.

Use these only for the optional technical path.

## Tool choice by task

| Task | Beginner tool | Optional technical tool | Human check required |
|---|---|---|---|
| Inspect data | Spreadsheet | pandas | Check column names and missing values manually |
| Generate first hypotheses | ChatGPT/Gemini/Claude | Same | Check against data rows |
| Summarize messy notes | ChatGPT/Gemini/Claude | Same | Check if the summary invented claims |
| Work with uploaded sources | NotebookLM | Local files + coding assistant | Check source coverage |
| Write a decision brief | ChatGPT/Gemini/Claude | Same | Rewrite in your own words |
| Clean or analyze CSV | Spreadsheet filters | Python + pandas | Check calculations |
| Review code | Not needed | Codex/Gemini Code Assist/Copilot/Cursor/Claude Code | Run the script and inspect output |

## Suggested LLM use

Use AI for:

- clarifying the question;
- listing assumptions;
- explaining unfamiliar columns;
- summarizing visible patterns;
- drafting a decision brief structure;
- finding possible risks and missing information;
- improving readability;
- asking what to verify manually.

Do not use AI as the only authority for:

- final numbers;
- medical or health claims;
- source verification;
- private or sensitive data;
- final interpretation without human review.

## Minimal safe prompt pattern

Use this structure:

```text
Context: [what the project is about]
Data: [what columns or rows you are using]
Task: [what you want AI to do]
Constraints: [do not invent values; separate facts from assumptions]
Output format: [table, checklist, brief, questions]
```

Example:

```text
Context: We are students analyzing a small public food-products dataset.
Data: The columns are product_name, categories, nutriscore_grade, sugars_100g, salt_100g, saturated_fat_100g, proteins_100g.
Task: Identify visible patterns and possible data-quality problems.
Constraints: Do not invent values. Separate facts from assumptions. Mention missing data or small sample size.
Output format: Short bullet list and a validation checklist.
```

## How to use coding assistants safely

Coding assistants are optional. They are useful for explaining or improving the Python script, but they should not replace understanding.

Good prompt:

```text
Explain this script to a beginner and suggest three simple validation checks. Do not add advanced features.
```

Bad prompt:

```text
Do the whole assignment for me.
```

## Privacy rule

Never upload private or sensitive data to a public AI tool unless you have explicit permission and understand the policy of the tool.

For this course, use only the provided public sample dataset.
