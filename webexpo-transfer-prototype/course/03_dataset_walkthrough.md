# 03 - Dataset walkthrough

## Goal of this module

Learn to inspect a dataset before asking AI to analyze it.

The mistake to avoid:

> uploading data into an AI tool and trusting the first answer.

The better workflow:

> inspect first, ask better questions, then validate.

## Step 1: open the data

Open:

```text
webexpo-transfer-prototype/data/sample_food_products.csv
```

Use Excel, Google Sheets, LibreOffice Calc, or a text editor.

## Step 2: identify the columns

The sample includes:

| Column | Meaning |
|---|---|
| code | Product barcode or identifier |
| product_name | Product name |
| brands | Brand name |
| categories | Product category labels |
| countries | Countries where the product appears |
| nutriscore_grade | Nutrition score category, usually a-e |
| energy_kcal_100g | Energy per 100 g or 100 ml |
| sugars_100g | Sugar per 100 g |
| salt_100g | Salt per 100 g |
| saturated_fat_100g | Saturated fat per 100 g |
| proteins_100g | Protein per 100 g |
| ingredients_text | Ingredient text |

## Step 3: inspect the data manually

Before AI, answer these manually:

1. How many rows are there?
2. Which categories appear most often?
3. Which products have high sugar?
4. Which products have high salt?
5. Which products have high saturated fat?
6. Are drinks and solid foods directly comparable?
7. Are all countries represented equally?
8. Are all fields complete?

## Step 4: identify possible comparison problems

The dataset is intentionally mixed. That creates good project-management questions.

Examples:

- Sodas and chocolate bars are very different product types.
- Energy values for drinks and solid foods are not always comparable in the same way.
- Nutri-Score may not exist for every product in a larger real dataset.
- A small sample can overrepresent one country or category.
- Product categories can be inconsistent or too broad.

## Step 5: choose a narrower project question

Bad question:

> Which food is healthy?

Better questions:

> Among the products in this small sample, which categories tend to have higher sugar or salt values?

> Which category would require most caution before making a recommendation, and why?

> What data quality problems would a project manager need to solve before using this for a real product decision?

## Student task

Write three notes before using AI:

```text
1. My project question is:
2. I think the biggest data-quality risk is:
3. I think AI might help with:
```

## Mini-output

At the end of this module, you should have:

- one narrowed project question;
- at least two data-quality concerns;
- one AI task that is safe and useful.
