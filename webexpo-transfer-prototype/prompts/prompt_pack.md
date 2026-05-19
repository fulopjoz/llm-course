# Prompt pack

Use these prompts as learning scaffolds. Do not submit raw AI output as your final work.

## 1. Clarify the project question

```text
I am a student analyzing a small public food-products dataset.
The columns are: product_name, brands, categories, countries, nutriscore_grade, energy_kcal_100g, sugars_100g, salt_100g, saturated_fat_100g, proteins_100g, ingredients_text.

My draft question is: [write your question].

Help me improve the question so it supports a realistic project decision.
Also list what this dataset can answer, what it cannot answer, and what assumptions I should avoid.
```

## 2. Inspect possible data-quality risks

```text
Before I analyze the rows, list data-quality risks for a food-products dataset with nutrition values.
Focus on missing values, inconsistent categories, small sample size, mixed product types, country coverage, and units.
Return a short checklist I can use while inspecting the spreadsheet.
```

## 3. Summarize visible patterns

```text
Here are rows from my dataset: [paste 10-30 rows].

Summarize visible patterns, but separate:
1. facts directly visible in the rows,
2. possible hypotheses,
3. assumptions,
4. things I must verify manually.

Do not invent missing values. Do not make medical claims.
```

## 4. Critical reviewer

```text
Act as a critical reviewer of this analysis: [paste analysis].

Find:
- unsupported claims,
- claims that are too broad,
- missing assumptions,
- possible data-quality problems,
- places where a human should check the spreadsheet.

Rewrite the analysis using cautious project language.
```

## 5. Prepare a decision brief template

```text
I need to write a one-page project decision brief for a mixed student team.
The project uses a small food-products dataset.

Create a fill-in template with these sections:
objective, data used, method, findings, limitations, recommendation, next action, and AI-use log.

Do not write the final answer for me. Give me questions I should answer in each section.
```

## 6. Explain technical output to non-technical teammates

```text
Rewrite this technical summary for a mixed team of students from management, chemistry, IT, design, and bioinformatics: [paste summary].

Keep the meaning, reduce jargon, and preserve uncertainty.
```

## 7. Optional coding assistant prompt

```text
I am using this Python script for a beginner course: [paste code].

Please:
1. explain the script step by step,
2. identify possible bugs or unclear parts,
3. suggest simple validation checks,
4. avoid adding advanced features unless necessary.
```

## 8. AI-use log prompt

```text
Based on this work session, help me draft an AI-use log.
Include:
- tool used,
- what I asked AI to do,
- what I checked manually,
- what I changed after validation,
- what limitations remain.

Use concise bullet points. I will rewrite them in my own words.
```
