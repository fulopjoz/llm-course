# Dataset notes

## Source

This course is designed around Open Food Facts, a public food-products database. Students should use public product-level fields only.

The intended workflow is:

1. Run `../scripts/fetch_openfoodfacts_sample.py` to download a small fresh sample from Open Food Facts.
2. Save the result as `sample_food_products.csv`.
3. Use the CSV in a spreadsheet or in the optional Python analysis.

## Why this dataset

Open Food Facts works well for mixed-specialization students because food-product data connects several domains:

- chemistry: salt, sugar, fat, nutrition fields;
- biology/health: nutrition quality and dietary interpretation;
- business/marketing: product categories, brands, consumer products;
- data/IT: missing values, inconsistent categories, APIs, CSV files;
- project management: turning messy evidence into a defensible decision.

## Privacy and ethics

Do not use personal data in this activity.

Use only public product-level data. Do not upload private research data, patient data, unpublished lab data, company data, or personal information into public AI tools.

## Recommended classroom sample size

For the no-code path, use about 30-80 products. That is small enough for manual inspection but large enough to show missing values and category differences.

For the optional technical path, 200-500 products is fine.

## Minimum fields

The course expects these columns when possible:

- code
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

## Important limitation

Open Food Facts is crowdsourced. Missing values, inconsistent product names, inconsistent categories, and uneven country coverage are part of the learning exercise. Students must not treat the dataset as a perfect nutrition database.
