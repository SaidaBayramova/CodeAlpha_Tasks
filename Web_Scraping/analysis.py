"""
analysis.py
-----------
Task 1: Exploratory Data Analysis (EDA)

Loads the cleaned dataset and answers a set of analytical questions
about it, printing a readable summary report to the console.

Usage:
    python analysis.py

Input:
    data/cleaned_data.csv
"""

import pandas as pd

CLEAN_PATH = "data/cleaned_data.csv"


def load_clean_data(path: str = CLEAN_PATH) -> pd.DataFrame:
    df = pd.read_csv(path)
    return df


def dataset_overview(df: pd.DataFrame) -> None:
    print("=" * 60)
    print("DATASET OVERVIEW")
    print("=" * 60)
    print(f"Rows: {df.shape[0]}   Columns: {df.shape[1]}")
    print("\nColumn types:")
    print(df.dtypes)
    print("\nFirst 5 rows:")
    print(df.head())


def summary_statistics(df: pd.DataFrame) -> None:
    print("\n" + "=" * 60)
    print("SUMMARY STATISTICS")
    print("=" * 60)
    print(df[["price", "rating"]].describe())


def key_questions(df: pd.DataFrame) -> None:
    print("\n" + "=" * 60)
    print("KEY ANALYTICAL QUESTIONS")
    print("=" * 60)

    # 1. How many books per category?
    print("\n1) Number of books per category:")
    print(df["category"].value_counts())

    # 2. Which category has the highest average price?
    avg_price_by_cat = df.groupby("category")["price"].mean().sort_values(ascending=False)
    print("\n2) Average price by category (highest first):")
    print(avg_price_by_cat)

    # 3. What share of books are in stock?
    in_stock_pct = df["in_stock"].mean() * 100
    print(f"\n3) Share of books currently in stock: {in_stock_pct:.1f}%")

    # 4. Is there a relationship between rating and price?
    correlation = df["price"].corr(df["rating"])
    print(f"\n4) Correlation between price and rating: {correlation:.3f}")

    # 5. Which category has the best average rating?
    avg_rating_by_cat = df.groupby("category")["rating"].mean().sort_values(ascending=False)
    print("\n5) Average rating by category (highest first):")
    print(avg_rating_by_cat)

    # 6. Cheapest and most expensive book
    cheapest = df.loc[df["price"].idxmin()]
    priciest = df.loc[df["price"].idxmax()]
    print(f"\n6) Cheapest book: '{cheapest['title']}' (${cheapest['price']})")
    print(f"   Most expensive book: '{priciest['title']}' (${priciest['price']})")


def detect_anomalies(df: pd.DataFrame) -> None:
    print("\n" + "=" * 60)
    print("ANOMALY CHECK")
    print("=" * 60)
    q1 = df["price"].quantile(0.25)
    q3 = df["price"].quantile(0.75)
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr

    outliers = df[(df["price"] < lower_bound) | (df["price"] > upper_bound)]
    print(f"Price outliers (outside [{lower_bound:.2f}, {upper_bound:.2f}]): {len(outliers)}")
    if not outliers.empty:
        print(outliers[["title", "category", "price"]])


def run_analysis(path: str = CLEAN_PATH) -> pd.DataFrame:
    df = load_clean_data(path)
    dataset_overview(df)
    summary_statistics(df)
    key_questions(df)
    detect_anomalies(df)
    return df


if __name__ == "__main__":
    run_analysis()
