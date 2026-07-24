# 📊 Task 1: Web Data Collection & Analysis

A Python-based web scraping project that collects publicly available data
from the web, cleans and preprocesses it, performs exploratory data
analysis (EDA), and visualizes the key findings.

## 🎯 Project Objective

Develop a Python pipeline to:
1. Scrape structured data from a public website
2. Clean and preprocess the raw data
3. Perform exploratory data analysis
4. Visualize insights with charts
5. Export a clean, reusable dataset

## 🌐 Data Source

This project scrapes [**Books to Scrape**](https://books.toscrape.com) —
a public sandbox website built specifically for practicing and
demonstrating web scraping. It's free to scrape and doesn't require
any authentication, which makes it a safe and legal target for this
kind of educational/portfolio project. For each book, the following
fields are collected: `title`, `price`, `rating`, `availability`, and
`category`.

## 📌 Project Workflow

### 1. Web Data Collection (`scraper.py`)
- Sends HTTP requests with `requests`
- Parses HTML with `BeautifulSoup`
- Crawls multiple paginated listing pages
- Visits each book's product page to read its category
- Saves the raw output to `data/raw_data.csv`

### 2. Data Cleaning & Preprocessing (`preprocessing.py`)
- Removes duplicate records
- Handles missing values (median imputation for price/rating, dropped
  rows for unusable records)
- Converts data types (price → float, rating → int, category → category)
- Derives an `in_stock` boolean from the raw availability text
- Saves the result to `data/cleaned_data.csv`

### 3. Exploratory Data Analysis (`analysis.py`)
- Prints dataset shape, column types, and a preview
- Generates summary statistics (`describe()`)
- Answers key analytical questions, e.g.:
  - How many books are in each category?
  - Which category has the highest average price?
  - What percentage of books are currently in stock?
  - Is there a correlation between price and rating?
  - Which books are the cheapest / most expensive?
- Flags price outliers using the IQR method

### 4. Data Visualization (`visualization.py`)
Generates and saves the following charts to `charts/`:
- `price_distribution.png` – histogram of book prices
- `avg_price_by_category.png` – bar chart of average price per category
- `rating_counts.png` – count of books per star rating
- `price_vs_rating.png` – box plot of price by rating
- `stock_status.png` – pie chart of in-stock vs. out-of-stock books

### 5. Export Results
- Cleaned dataset saved as `data/cleaned_data.csv`
- All charts saved as PNG files in `charts/`

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python | Core language |
| Requests | HTTP requests |
| BeautifulSoup | HTML parsing |
| Pandas | Data manipulation |
| NumPy | Numerical operations |
| Matplotlib | Plotting |
| Seaborn | Statistical visualization |

## 📂 Repository Structure

```
Task1_Web_Data_Collection/
│
├── scraper.py
├── preprocessing.py
├── analysis.py
├── visualization.py
├── data/
│   ├── raw_data.csv
│   └── cleaned_data.csv
├── charts/
├── requirements.txt
└── README.md
```

## 🚀 How to Run

1. Clone the repository and move into the project folder:
   ```bash
   git clone <your-repo-url>
   cd Task1_Web_Data_Collection
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the pipeline step by step:
   ```bash
   python scraper.py          # collect raw data (requires internet access)
   python preprocessing.py    # clean the data
   python analysis.py         # run EDA and print insights
   python visualization.py    # generate charts
   ```

> **Note:** `scraper.py` needs an active internet connection to reach
> `books.toscrape.com`. Sample `raw_data.csv` / `cleaned_data.csv` files
> and pre-generated charts are already included in this repo so you can
> explore `analysis.py` and `visualization.py` immediately without
> re-scraping.

## 📈 Sample Insights

Running the pipeline on the sample dataset shows patterns such as
category-level pricing differences, the overall stock availability
rate, and the relationship (or lack thereof) between price and rating —
see the console output of `analysis.py` and the charts in `charts/`
for the full picture.

## 📄 License

This project is for educational purposes. Please respect the target
website's `robots.txt` and terms of service when scraping.
