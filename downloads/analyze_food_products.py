import pandas as pd

INPUT_FILE = 'sample_food_products.csv'
OUTPUT_FILE = 'category_summary.csv'

NUTRITION_COLUMNS = [
    'energy_kcal_100g',
    'sugars_100g',
    'salt_100g',
    'saturated_fat_100g',
    'proteins_100g',
]


def broad_category(value):
    if not isinstance(value, str) or not value.strip():
        return 'Unknown'
    return value.split(';')[0].strip() or 'Unknown'


def main():
    df = pd.read_csv(INPUT_FILE)
    for column in NUTRITION_COLUMNS:
        df[column] = pd.to_numeric(df[column], errors='coerce')

    df['broad_category'] = df['categories'].apply(broad_category)

    summary = (
        df.groupby('broad_category')
        .agg(
            product_count=('product_name', 'count'),
            avg_energy_kcal_100g=('energy_kcal_100g', 'mean'),
            avg_sugars_100g=('sugars_100g', 'mean'),
            avg_salt_100g=('salt_100g', 'mean'),
            avg_saturated_fat_100g=('saturated_fat_100g', 'mean'),
            avg_proteins_100g=('proteins_100g', 'mean'),
        )
        .reset_index()
    )

    summary = summary.round(2)
    summary.to_csv(OUTPUT_FILE, index=False)

    print('Wrote', OUTPUT_FILE)
    print('Manual checks: sample size, category comparability, missing values, and overbroad AI claims.')


if __name__ == '__main__':
    main()
