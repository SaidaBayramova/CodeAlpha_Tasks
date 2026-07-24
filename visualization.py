"""
visualization.py
-----------------
Task 1: Data Visualization

Loads the cleaned dataset and produces a set of charts that highlight
the key insights found during analysis.

Usage:
    python visualization.py

Input:
    data/cleaned_data.csv

Output (saved into charts/):
    price_distribution.png
    avg_price_by_category.png
    rating_counts.png
    price_vs_rating.png
    stock_status.png
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

CLEAN_PATH = "data/cleaned_data.csv"
CHARTS_DIR = "charts"

sns.set_theme(style="whitegrid")


def ensure_charts_dir(path: str = CHARTS_DIR) -> None:
    os.makedirs(path, exist_ok=True)


def plot_price_distribution(df: pd.DataFrame) -> None:
    plt.figure(figsize=(8, 5))
    sns.histplot(df["price"], bins=20, kde=True, color="steelblue")
    plt.title("Distribution of Book Prices")
    plt.xlabel("Price ($)")
    plt.ylabel("Number of Books")
    plt.tight_layout()
    plt.savefig(f"{CHARTS_DIR}/price_distribution.png", dpi=150)
    plt.close()


def plot_avg_price_by_category(df: pd.DataFrame, top_n: int = 10) -> None:
    avg_price = (
        df.groupby("category")["price"].mean().sort_values(ascending=False).head(top_n)
    )
    plt.figure(figsize=(9, 5))
    sns.barplot(x=avg_price.values, y=avg_price.index, hue=avg_price.index,
                palette="viridis", legend=False)
    plt.title(f"Top {top_n} Categories by Average Price")
    plt.xlabel("Average Price ($)")
    plt.ylabel("Category")
    plt.tight_layout()
    plt.savefig(f"{CHARTS_DIR}/avg_price_by_category.png", dpi=150)
    plt.close()


def plot_rating_counts(df: pd.DataFrame) -> None:
    plt.figure(figsize=(7, 5))
    sns.countplot(x="rating", data=df, hue="rating", palette="mako", legend=False)
    plt.title("Number of Books by Star Rating")
    plt.xlabel("Rating (stars)")
    plt.ylabel("Number of Books")
    plt.tight_layout()
    plt.savefig(f"{CHARTS_DIR}/rating_counts.png", dpi=150)
    plt.close()


def plot_price_vs_rating(df: pd.DataFrame) -> None:
    plt.figure(figsize=(7, 5))
    sns.boxplot(x="rating", y="price", hue="rating", data=df, palette="crest", legend=False)
    plt.title("Price Distribution by Star Rating")
    plt.xlabel("Rating (stars)")
    plt.ylabel("Price ($)")
    plt.tight_layout()
    plt.savefig(f"{CHARTS_DIR}/price_vs_rating.png", dpi=150)
    plt.close()


def plot_stock_status(df: pd.DataFrame) -> None:
    counts = df["in_stock"].value_counts().rename({True: "In stock", False: "Out of stock"})
    plt.figure(figsize=(5, 5))
    plt.pie(
        counts.values,
        labels=counts.index,
        autopct="%1.1f%%",
        colors=["mediumseagreen", "lightcoral"],
        startangle=90,
    )
    plt.title("Stock Availability")
    plt.tight_layout()
    plt.savefig(f"{CHARTS_DIR}/stock_status.png", dpi=150)
    plt.close()


def run_visualizations(path: str = CLEAN_PATH) -> None:
    ensure_charts_dir()
    df = pd.read_csv(path)

    plot_price_distribution(df)
    plot_avg_price_by_category(df)
    plot_rating_counts(df)
    plot_price_vs_rating(df)
    plot_stock_status(df)

    print(f"Saved 5 charts to {CHARTS_DIR}/")


if __name__ == "__main__":
    run_visualizations()
