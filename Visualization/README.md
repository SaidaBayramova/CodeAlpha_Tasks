# 📊 Task 3: Data Visualization — Spotify Tracks Dataset

**CodeAlpha Internship — Task 3**

## 📖 Project Overview

This project transforms the Spotify Tracks Dataset into a full set of
clear, compelling visualizations — histograms, bar charts, scatter plots,
a correlation heatmap, boxplots, a violin plot, a pairplot, and one
interactive Plotly chart — all tied together in a final summary dashboard.
The goal is to design visuals that reveal insights at a glance and support
a strong data-storytelling portfolio piece.

## 📊 Dataset

**Source:** [Spotify Tracks Dataset](https://www.kaggle.com/datasets/maharshipandya/-spotify-tracks-dataset)
(Kaggle) — 114,000 tracks across 114 genres, with audio features such as
danceability, energy, loudness, valence, and tempo.

> This dataset does not include a `release_year` column. Chart #7
> ("Songs Released per Year") is substituted with a comparable line chart
> — **average tempo across popularity levels** — since a true
> release-year trend isn't possible with the fields available here. This
> is explained inline in the notebook.

## 🔄 Workflow

1. **Import Libraries** — Pandas, NumPy, Matplotlib, Seaborn, **Plotly**
2. **Load Dataset** — shape, columns, missing values
3. **Data Cleaning** — remove duplicates, handle missing values, convert
   data types

## 🎨 Design System

Every chart in this notebook follows the same visual language:

- **One consistent color palette** across all charts — Spotify green
  (`#1DB954`) + dark grey (`#2C2C2C`), with a single red accent color
  reserved only for annotations/highlights
- **Title + one-line explanation** on every chart, so it's understandable
  without reading the code
- **Annotated key values** — the highest bar, the peak point, or the
  correlation coefficient is called out directly on the chart
- **Clean, minimal design** — no unnecessary gridlines or clutter,
  readable fonts, consistent sizing
- A final **3×3 summary dashboard** that brings the whole story together
  in one image

## 📈 Visualizations

| # | Chart | Type |
|---|---|---|
| 1 | Popularity Distribution | Histogram |
| 2 | Danceability Distribution | Histogram |
| 3 | Energy Distribution | Histogram |
| 4 | Top 10 Genres | Horizontal Bar Chart |
| 5 | Top 15 Artists | Bar Chart |
| 6 | Average Popularity by Genre | Bar Chart |
| 7 | Tempo Trend Across Popularity Levels *(substitute for release year)* | Line Chart |
| 8 | Popularity vs Danceability | **Interactive Scatter Plot (Plotly)** |
| 9 | Energy vs Loudness | Scatter Plot |
| 10 | Correlation Heatmap ⭐ | Heatmap |
| 11 | Tempo Distribution | Boxplot |
| 12 | Popularity by Genre (Top 6) | Boxplot |
| 13 | Danceability by Genre (Top 6) | Violin Plot |
| 14 | Pairplot (optional) | Pairplot |
| — | **Summary Dashboard** | 3×3 multi-panel |

## 🔑 Key Insights

- ✔ Danceability and Energy show a positive relationship, and both connect
  strongly to loudness.
- ✔ Some genres — especially K-pop and pop-film — consistently achieve
  higher average popularity scores than others.
- ✔ Most tracks fall within a moderate popularity range; very few reach
  the highest tier (70+).
- ✔ Loud tracks generally tend to have higher energy values
  (r ≈ 0.76 between loudness and energy).
- ✔ A few outliers exist in tempo and duration — kept intentionally, as
  they likely represent legitimate edge cases (e.g. ambient/spoken-word
  tracks) rather than data errors.
- ✔ Genre "shape" varies as much as genre averages — some genres cluster
  tightly on danceability, others are far more spread out.

## 🛠️ Technologies

- 🐍 Python
- 🐼 Pandas
- 🔢 NumPy
- 📊 Matplotlib
- 📈 Seaborn
- 🔵 Plotly

## 📂 Repository Structure

```
Task3_Visualization/
│
├── Task3_Data_Visualization.ipynb
├── data/
│   └── spotify_dataset.csv
├── charts/
│   ├── 01_popularity_distribution.png
│   ├── 02_danceability_distribution.png
│   ├── 03_energy_distribution.png
│   ├── 04_top_10_genres.png
│   ├── 05_top_15_artists.png
│   ├── 06_avg_popularity_by_genre.png
│   ├── 07_tempo_trend_by_popularity.png
│   ├── 09_energy_vs_loudness.png
│   ├── 10_correlation_heatmap.png
│   ├── 11_tempo_boxplot.png
│   ├── 12_popularity_by_genre_boxplot.png
│   ├── 13_danceability_violin.png
│   ├── 14_pairplot.png
│   └── 15_summary_dashboard.png
├── requirements.txt
└── README.md
```

> Note: chart #8 (the interactive Plotly scatter plot) renders inline in
> the notebook and isn't saved as a static PNG, since its value is in the
> interactivity (hover tooltips, zoom).

## 🚀 How to Run

### Option 1: Google Colab
1. Open [Google Colab](https://colab.research.google.com)
2. Upload `Task3_Data_Visualization.ipynb`
3. Upload `data/spotify_dataset.csv` to the Colab session
4. Run all cells

### Option 2: Local Jupyter
```bash
pip install -r requirements.txt
jupyter notebook Task3_Data_Visualization.ipynb
```

