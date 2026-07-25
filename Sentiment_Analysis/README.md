# 💬 Task 4: Sentiment Analysis on Amazon Product Reviews

**CodeAlpha Internship — Task 4**

## 📖 Project Overview

This project analyzes customer reviews to classify them as **Positive**,
**Negative**, or **Neutral** using NLP techniques and lexicon-based
sentiment scoring (VADER). The goal is to understand public opinion
patterns in product reviews and surface insights that could inform product
development, quality control, or customer service priorities.

## 📊 Dataset

**Source:** [Amazon Product Reviews Dataset](http://jmcauley.ucsd.edu/data/amazon/)
(Julian McAuley, UCSD) — "Cell Phones and Accessories" 5-core subset.

- Original file: 194,439 reviews
- This notebook analyzes a **random sample of 20,000 reviews**
  (`data/amazon_cellphone_reviews.csv`) for fast, reproducible runtime —
  the sample size is a single variable (`SAMPLE_SIZE`) you can change to
  scale up to the full dataset.
- Fields used: `reviewText`, `summary`, `overall` (1-5 star rating),
  `reviewTime`

## 🔄 Workflow

1. **Import Libraries** — Pandas, NumPy, Matplotlib, Seaborn, NLTK, VADER,
   WordCloud
2. **Load Dataset & Data Overview** — shape, types, missing values,
   star-rating distribution
3. **Data Cleaning** — remove duplicates & missing values, lowercase,
   strip URLs/punctuation/numbers/extra whitespace
4. **Text Preprocessing** — tokenization, stopword removal,
   lemmatization
5. **Sentiment Analysis (VADER)** — compound score → Positive / Neutral /
   Negative classification, validated against star ratings
6. **Visualization** — sentiment bar & pie charts, positive/negative
   WordClouds, review length distribution, top 20 frequent words,
   compound score vs star rating
7. **Insights** — key questions answered and a summary of findings

## 📈 Visualizations

| Chart | Description |
|---|---|
| `00_star_rating_distribution.png` | Distribution of 1-5 star ratings |
| `01_sentiment_distribution.png` | Sentiment class bar chart + pie chart |
| `02_wordclouds_positive_negative.png` | Most common words in positive vs negative reviews |
| `03_review_length_distribution.png` | Histogram of review length (words) |
| `04_top_20_words.png` | Top 20 most frequent words across all reviews |
| `05_compound_score_by_rating.png` | VADER compound score distribution by star rating |

## 🔑 Key Findings

- **Positive reviews dominate the dataset** (~84% of the sample),
  consistent with the well-known positivity skew of e-commerce reviews.
- **Product quality and durability**, not delivery, is the most discussed
  complaint theme among negative reviews — words like *waste*, *broke*,
  *poor*, *disappointed*, and *cheap* appear disproportionately often in
  negative reviews. Only ~16% of negative reviews even mention
  delivery/shipping.
- **Neutral reviews are relatively rare** (~3%) — most reviewers clearly
  lean positive or negative.
- **VADER's sentiment scores track star ratings well** at the aggregate
  level, validating lexicon-based sentiment as a fast, effective first
  pass for large-scale review analysis — though individual mismatches
  (e.g. sarcasm) do occur, a known limitation of lexicon-based tools.

## 🛠️ Tech Stack

- 🐍 Python
- 🐼 Pandas
- 🔢 NumPy
- 📊 Matplotlib
- 📈 Seaborn
- 💬 NLTK
- 🧠 VADER (vaderSentiment)
- ☁️ WordCloud

## 📂 Repository Structure

```
Task4_Sentiment_Analysis/
│
├── Task4_Sentiment_Analysis.ipynb
├── data/
│   └── amazon_cellphone_reviews.csv
├── charts/
│   ├── 00_star_rating_distribution.png
│   ├── 01_sentiment_distribution.png
│   ├── 02_wordclouds_positive_negative.png
│   ├── 03_review_length_distribution.png
│   ├── 04_top_20_words.png
│   └── 05_compound_score_by_rating.png
├── requirements.txt
└── README.md
```

## 🚀 How to Run

### Option 1: Google Colab
1. Open [Google Colab](https://colab.research.google.com)
2. Upload `Task4_Sentiment_Analysis.ipynb`
3. Upload `data/amazon_cellphone_reviews.csv` to the Colab session
4. Run all cells (NLTK data downloads automatically on first run)

### Option 2: Local Jupyter
```bash
pip install -r requirements.txt
jupyter notebook Task4_Sentiment_Analysis.ipynb
```

## 📄 License

This project is for educational and portfolio purposes as part of the
CodeAlpha Data Science/Analytics internship. Dataset provided by Julian
McAuley (UCSD) for academic/research use.
