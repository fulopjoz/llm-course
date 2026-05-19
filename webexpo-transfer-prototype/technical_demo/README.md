# Optional technical demo

This folder contains a small Python demo for students who want to try a coding-assisted version of the activity.

The main script is:

```text
analyze_food_products.py
```

## What it does

The script reads:

```text
../data/sample_food_products.csv
```

It creates:

```text
output/category_summary.csv
```

The output summarizes product counts and average nutrition fields by broad product category.

## Requirements

Install Python 3 and pandas.

```bash
pip install pandas
```

## Run

From the repository root:

```bash
python webexpo-transfer-prototype/technical_demo/analyze_food_products.py
```

## Use with an AI coding assistant

Recommended prompt:

```text
I am a beginner student. Explain this script line by line.
Then suggest 3 small improvements for readability and validation.
Do not make the script more complex than necessary.
```

Another useful prompt:

```text
Review the output table. What manual checks should I perform before using it in a project decision brief?
```

## Important limitation

The script calculates simple averages. It does not prove that one category is healthy or unhealthy. The output is only a first screening that must be interpreted carefully.
