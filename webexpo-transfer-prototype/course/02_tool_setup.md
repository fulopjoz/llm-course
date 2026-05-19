# 02 - Tool setup

## Goal of this module

Choose tools that match your skill level. You do not need expensive tools or programming experience to complete the course.

## Recommended default setup for beginners

Use this if you are a non-technical student or you want the simplest path.

1. Spreadsheet app:
   - Google Sheets, Microsoft Excel, or LibreOffice Calc.
2. AI assistant:
   - ChatGPT Free/Go/Plus, Gemini, Claude, or another assistant you already have access to.
3. Optional source-grounded tool:
   - NotebookLM if you want to upload the dataset notes and ask questions only about those sources.
4. Web browser:
   - for checking sources and tool documentation.

## Optional technical setup

Use this only if you want to try the coding track.

1. Python 3.
2. pandas.
3. VS Code or another code editor.
4. One coding assistant:
   - Codex in ChatGPT;
   - Gemini Code Assist;
   - GitHub Copilot Free;
   - Cursor;
   - Claude Code if you already have access.

## Tool choice by task

| Task | Beginner tool | Technical tool | Human check required |
|---|---|---|---|
| Inspect data | Spreadsheet | pandas | Check column names and missing values manually |
| Generate first hypotheses | ChatGPT/Gemini/Claude | Same | Check against data rows |
| Summarize messy notes | ChatGPT/Gemini/Claude | Same | Check if the summary invented claims |
| Work with uploaded sources | NotebookLM | NotebookLM or local files | Check source coverage |
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
- improving readability.

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

## Privacy rule

Never upload private or sensitive data to a public AI tool unless you have explicit permission and understand the policy of the tool.

For this course, use only the provided public sample dataset.
