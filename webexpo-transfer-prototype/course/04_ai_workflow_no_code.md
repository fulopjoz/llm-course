# 04 - AI workflow for non-coders

## Goal of this module

Use AI as a project assistant, not as an oracle.

You will use an AI assistant to structure a small analysis, then you will check the answer manually.

## Recommended tools

Use one of:

- ChatGPT;
- Gemini;
- Claude;
- NotebookLM, if you upload only the course files and want source-grounded Q&A.

Use a spreadsheet for checking the data.

## Step 1: prepare context

Do not start with:

```text
Analyze this dataset.
```

Start with context:

```text
I am a student in a Technology Skills for Project Managers course.
We are learning how to use AI responsibly with messy real-world data.
The dataset is a small public sample of food products with nutrition fields.
The goal is not medical advice. The goal is to produce a cautious project decision brief.
```

## Step 2: paste the column names

Paste the column names, not the whole dataset first:

```text
Columns:
code, product_name, brands, categories, countries, nutriscore_grade,
energy_kcal_100g, sugars_100g, salt_100g, saturated_fat_100g,
proteins_100g, ingredients_text
```

Ask:

```text
Before seeing the rows, what data-quality risks and comparison problems should I watch for?
```

## Step 3: paste a small sample

Paste 10-15 rows, not necessarily the whole CSV.

Ask:

```text
Here are sample rows from the dataset: [paste rows].
Identify visible patterns, but separate:
1. facts visible in the rows,
2. assumptions,
3. possible hypotheses,
4. what must be checked in the spreadsheet.
Do not invent missing values or make medical claims.
```

## Step 4: ask for a validation checklist

Prompt:

```text
Create a validation checklist for this analysis.
Focus on missing values, unfair comparisons, small sample size, category inconsistency, and unsupported claims.
```

## Step 5: ask for a project decision brief structure

Prompt:

```text
Help me structure a one-page decision brief for a mixed student team.
The brief should include:
objective, data used, AI help used, findings, limitations, recommendation, and next action.
Do not write the final answer for me. Give me a fill-in template and questions I should answer.
```

## Step 6: write in your own words

Use AI output as scaffolding only.

Your final brief must be written by you. It should include your own interpretation and manual checks.

## Common beginner mistakes

### Mistake 1: accepting confident language

AI may write:

> Chocolate products are unhealthy and should be avoided.

Better student version:

> In this small sample, chocolate products show higher sugar and saturated-fat values than several other categories. This does not prove a general health conclusion, because the sample is small and not representative.

### Mistake 2: ignoring category differences

AI may compare soda, cheese, olive oil, soup, and yogurt as if they were the same type of product.

Better student approach:

> I should compare within similar categories or clearly state that the comparison is broad and limited.

### Mistake 3: hiding uncertainty

Bad:

> The data proves which foods are healthy.

Better:

> The data can support a cautious first screening, but a real project would need a larger sample, consistent categories, and clearer nutritional criteria.

## Mini-output

At the end of this module, you should have:

1. One AI-generated list of possible patterns.
2. One validation checklist.
3. Your own notes about what you accepted, rejected, or corrected.
