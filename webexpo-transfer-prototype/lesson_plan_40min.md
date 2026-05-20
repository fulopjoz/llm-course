# 40-minute lesson plan

## Title

AI for student projects: from messy information to reliable decisions

## Audience

Mixed-specialization students in Technology Skills for Project Managers.

No coding background required.

## Learning outcomes

By the end, students can:

1. define a project question before using AI;
2. inspect a small real-world dataset;
3. use AI to structure analysis;
4. validate AI output manually;
5. write a short decision brief;
6. record how AI was used.

## Required tools

- Spreadsheet app: Excel, Google Sheets, or LibreOffice Calc.
- One AI chat assistant: ChatGPT, Gemini, Claude, or similar.
- CSV file: `data/sample_food_products.csv`.

## Optional tools

- NotebookLM for source-grounded Q&A.
- Python + pandas for technical students.
- Codex, Gemini Code Assist, GitHub Copilot, Cursor, or Claude Code for optional code explanation/review.

## Timeline

### 0-5 min: framing

Explain the goal:

> AI is not the deliverable. The deliverable is a defensible project decision.

Show the workflow:

```text
question -> inspect data -> ask AI -> validate -> decision brief
```

### 5-10 min: open the dataset

Students open `data/sample_food_products.csv` in a spreadsheet.

Ask them to identify:

- number of rows;
- product categories;
- nutrition columns;
- possible comparison problems.

### 10-18 min: first AI prompt

Students use one AI chat tool.

Prompt:

```text
I am a student using a small public food-products dataset.
The columns are product_name, brands, categories, countries, nutriscore_grade, energy_kcal_100g, sugars_100g, salt_100g, saturated_fat_100g, proteins_100g, ingredients_text.

Before I analyze the rows, what data-quality risks and comparison problems should I watch for?
Do not make medical claims. Focus on project decision-making and validation.
```

Then students paste 10-15 rows and ask for visible patterns, facts, assumptions, and manual checks.

### 18-25 min: validate one AI claim

Each student or group chooses one AI claim and checks it in the spreadsheet.

Example claim:

> Snacks show high sugar and saturated fat in this sample.

Students check at least three rows manually.

They label the claim as:

- supported;
- plausible but not proven;
- unsupported;
- too broad;
- needs rewrite.

### 25-32 min: write a short decision brief

Students fill in this structure:

```text
Title:
Objective:
Data used:
Method:
Findings:
Limitations:
Recommendation:
AI-use log:
```

The brief can be rough. The goal is structure and caution.

### 32-37 min: optional technical extension

Show the optional Python script:

```text
technical_demo/analyze_food_products.py
```

Explain that technical students can use Codex, Gemini Code Assist, GitHub Copilot, Cursor, or Claude Code to explain or review the script.

Make clear that this is optional.

### 37-40 min: wrap-up

Ask:

- What did AI help with?
- What did AI not solve?
- What did humans need to validate?
- What would be the next step for a real project?

## Output after the lesson

Each student or group should have:

1. a short project question;
2. one AI prompt they used;
3. one manually checked AI claim;
4. three limitations;
5. a draft decision brief.

## Extension to 60 minutes

If more time is available:

- compare two AI tools on the same prompt;
- use NotebookLM with uploaded course files;
- run the Python script;
- create a small visualization;
- improve the decision brief for a non-technical audience.
