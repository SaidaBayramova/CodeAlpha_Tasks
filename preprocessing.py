"""
preprocessing.py
-----------------
Task 1: Data Cleaning & Preprocessing

Reads the raw scraped data, cleans it, and writes a tidy version ready
for analysis.

Usage:
    python preprocessing.py

Input:
    data/raw_data.csv

Output:
    data/cleaned_data.csv
"""

import pandas as pd
import numpy as np

RAW_PATH = "data/raw_data.csv"
CLEAN_PATH = "data/cleaned_data.csv"


def load_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    print(f"Loaded {len(df)} raw rows from {path}")
    return df


def clean_price(df: pd.DataFrame) -> pd.DataFrame:
    """Convert the price column from text (e.g. '51.77') to float."""
    df["price"] = (
        df["price"]
        .astype(str)
        .str.replace("£", "", regex=False)
        .str.replace("Â", "", regex=False)
        .str.strip()
    )
    df["price"] = pd.to_numeric(df["price"], errors="coerce")
    return df


def clean_availability(df: pd.DataFrame) -> pd.DataFrame:
    """Turn free-text availability into a boolean 'in_stock' flag."""
    df["availability"] = df["availability"].astype(str).str.strip()
    df["in_stock"] = df["availability"].str.contains("In stock", case=False, na=False)
    return df


def clean_text_fields(df: pd.DataFrame) -> pd.DataFrame:
    for col in ["title", "category"]:
        if col in df.columns:
            df[col] = df[col].astype(str).str.strip()
    return df


def handle_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    before = len(df)

    # Drop rows with no title (unusable record)
    df = df.dropna(subset=["title"])

    # Fill missing ratings with the median rating
    if df["rating"].isna().any():
        median_rating = df["rating"].median()
        df["rating"] = df["rating"].fillna(median_rating)

    # Fill missing prices with the median price per category
    if df["price"].isna().any():
        df["price"] = df.groupby("category")["price"].transform(
            lambda s: s.fillna(s.median())
        )
        df["price"] = df["price"].fillna(df["price"].median())

    # Fill missing category with 'Unknown'
    df["category"] = df["category"].fillna("Unknown")

    after = len(df)
    print(f"Handled missing values: {before - after} unusable rows dropped")
    return df


def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    before = len(df)
    df = df.drop_duplicates(subset=["title", "category"], keep="first")
    after = len(df)
    print(f"Removed {before - after} duplicate rows")
    return df


def convert_types(df: pd.DataFrame) -> pd.DataFrame:
    df["rating"] = df["rating"].astype(int)
    df["price"] = df["price"].astype(float).round(2)
    df["in_stock"] = df["in_stock"].astype(bool)
    df["category"] = df["category"].astype("category")
    return df


def run_pipeline(raw_path: str = RAW_PATH, clean_path: str = CLEAN_PATH) -> pd.DataFrame:
    df = load_data(raw_path)
    df = clean_text_fields(df)
    df = clean_price(df)
    df = clean_availability(df)
    df = remove_duplicates(df)
    df = handle_missing_values(df)
    df = convert_types(df)

    df = df[["title", "category", "price", "rating", "in_stock"]]
    df.to_csv(clean_path, index=False)
    print(f"Saved {len(df)} cleaned rows to {clean_path}")
    return df


if __name__ == "__main__":
    run_pipeline()
