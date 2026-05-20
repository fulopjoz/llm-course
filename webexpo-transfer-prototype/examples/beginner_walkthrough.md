# Beginner walkthrough

This walkthrough simulates a student with no coding background.

Goal: complete the activity with only a spreadsheet and one AI chat tool.

## Step 1: open the dataset

Open:

```text
webexpo-transfer-prototype/data/sample_food_products.csv
```

Use Excel, Google Sheets, or LibreOffice Calc.

Do not use AI yet.

## Step 2: inspect the columns

Look at the header row.

You should see columns such as:

- product_name
- brands
- categories
- countries
- nutriscore_grade
- energy_kcal_100g
- sugars_100g
- salt_100g
- saturated_fat_100g
- proteins_100g
- ingredients_text

Student note example:

```text
The dataset has product names, categories, countries, nutrition values, and ingredients.
The values seem to be per 100 g or 100 ml.
The products are mixed: drinks, snacks, dairy, sauces, spreads, and others.
```

## Step 3: write a project question

Beginner version:

```text
Which category looks less healthy?
```

Improved version:

```text
In this small sample, which product categories show higher sugar, salt, or saturated-fat values, and what limitations should we mention before making a project recommendation?
```

Use the improved version.

## Step 4: ask AI for risks before analysis

Paste this into ChatGPT, Gemini, Claude, or another AI assistant:

```text
I am a student in a Technology Skills for Project Managers course.
I am using a small public food-products CSV dataset.
The columns are product_name, brands, categories, countries, nutriscore_grade, energy_kcal_100g, sugars_100g, salt_100g, saturated_fat_100g, proteins_100g, ingredients_text.

Before I analyze the rows, what data-quality risks and comparison problems should I watch for?
Do not make medical claims. Focus on project decision-making and validation.
```

Expected useful AI points:

- product categories may be inconsistent;
- sample size may be small;
- drinks and solid foods may not be directly comparable;
- nutrition fields may be missing or use different assumptions;
- conclusions should be cautious.

## Step 5: paste a small sample to AI

Select 10-15 rows from the spreadsheet and paste them into the AI tool.

Use this prompt:

```text
Here are sample rows from the dataset: [paste rows].

Summarize visible patterns, but separate:
1. facts directly visible in the rows,
2. possible hypotheses,
3. assumptions,
4. things I must verify manually.

Do not invent missing values. Do not make medical claims.
```

## Step 6: check one AI claim manually

Suppose AI says:

```text
Snacks appear to have high sugar and saturated fat.
```

Check the spreadsheet manually.

Visible examples:

- Mars Bar: sugar 59.5, saturated fat 8.1.
- Ferrero Rocher: sugar 39.9, saturated fat 14.1.
- Kinder Chocolate: sugar 53.5, saturated fat 22.6.
- Milka Alpine Milk: sugar 58, saturated fat 18.5.

Student validation note:

```text
This claim is partly supported by visible rows in the sample. However, the sample is small and contains only a few snack products, so I should write "in this sample" and avoid general claims about all snacks.
```

## Step 7: rewrite cautiously

Too strong:

```text
Snacks are unhealthy.
```

Better:

```text
In this small sample, several snack products show high sugar and saturated-fat values compared with categories such as beverages or dairy. This is only a first screening and cannot be generalized without a larger, more balanced sample.
```

## Step 8: prepare the decision brief

Use this structure:

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

## Step 9: record AI use

Example:

```text
AI tool used: ChatGPT/Gemini/Claude.
I asked it to identify data-quality risks and visible patterns.
I manually checked product rows, sugar values, saturated-fat values, and category names.
I changed the wording to avoid broad health claims.
The remaining limitation is that the sample is small and mixed.
```

## Step 10: final beginner output

A good beginner result does not need complex statistics. It should show:

- a clear question;
- manual spreadsheet inspection;
- careful AI use;
- validation;
- cautious wording;
- a realistic next step.
