"""Optional technical demo for the WebExpo transfer prototype.

This script analyzes a small public food-products CSV sample and writes a
category-level summary table. It is intentionally simple so students can inspect,
modify, and validate it.

Run from the repository root:

    python webexpo-transfer-prototype/technical_demo/analyze_food_products.py
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "sample_food_products.csv"
OUTPUT_DIR = ROOT / "technical_demo" / "output"
OUTPUT_PATH = OUTPUT_DIR / "category_summary.csv"

NUTRITION_COLUMNS = [
    "energy_kcal_100g",
    "sugars_100g",
    "salt_100g",
    "saturated_fat_100g",
    "proteins_100g",
]


def broad_category(category_text: str) -> str:
    """Return a simple broad category from a messy category string."""
    if not isinstance(category_text, str) or not category_text.strip():
        return "Unknown"

    first = category_text.split(";")[0].strip()
    return first or "Unknown"


def load_data(path: Path) -> pd.DataFrame:
    """Load the CSV and coerce expected numeric columns."""
    if not path.exists():
        raise FileNotFoundError(f"Dataset not found: {path}")

    df = pd.read_csv(path)

    for column in NUTRITION_COLUMNS:
        if column in df.columns:
            df[column] = pd.to_numeric(df[column], errors="coerce")
        else:
            raise ValueError(f"Expected column missing: {column}")

    df["broad_category"] = df["categories"].apply(broad_category)
    return df


def summarize_by_category(df: pd.DataFrame) -> pd.DataFrame:
    """Create a category-level summary using simple means and counts."""
    summary = (
        df.groupby("broad_category", dropna=False)
        .agg(
            product_count=("product_name", "count"),
            avg_energy_kcal_100g=("energy_kcal_100g", "mean"),
            avg_sugars_100g=("sugars_100g", "mean"),
            avg_salt_100g=("salt_100g", "mean"),
            avg_saturated_fat_100g=("saturated_fat_100g", "mean"),
            avg_proteins_100g=("proteins_100g", "mean"),
        )
        .reset_index()
        .sort_values(["product_count", "broad_category"], ascending=[False, True])
    )

    numeric_columns = [column for column in summary.columns if column.startswith("avg_")]
    summary[numeric_columns] = summary[numeric_columns].round(2)
    return summary


def print_validation_prompts(df: pd.DataFrame, summary: pd.DataFrame) -> None:
    """Print checks students should perform after running the script."""
    print("Dataset loaded")
    print(f"Rows: {len(df)}")
    print(f"Columns: {len(df.columns)}")
    print("\nBroad categories:")
    print(df["broad_category"].value_counts().to_string())

    print("\nMissing values per nutrition column:")
    print(df[NUTRITION_COLUMNS].isna().sum().to_string())

    print("\nCategory summary preview:")
    print(summary.head(10).to_string(index=False))

    print("\nManual validation questions:")
    print("1. Are the largest categories represented by enough products?")
    print("2. Are drinks and solid foods being compared too broadly?")
    print("3. Do high average values come from one extreme product?")
    print("4. Does the output support a cautious project decision, or only a first screening?")


def main() -> None:
    df = load_data(DATA_PATH)
    summary = summarize_by_category(df)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    summary.to_csv(OUTPUT_PATH, index=False)

    print_validation_prompts(df, summary)
    print(f"\nWrote summary table to: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
