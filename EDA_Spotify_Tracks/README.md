# 🎧 Task 2: Exploratory Data Analysis (EDA) — Spotify Tracks Dataset

**CodeAlpha Internship — Task 2**

An in-depth exploratory data analysis of the [Spotify Tracks Dataset](https://www.kaggle.com/datasets/maharshipandya/-spotify-tracks-dataset)
(Kaggle) — 114,000 tracks across 114 genres, each described by audio
features such as danceability, energy, loudness, valence, and tempo.

## 🎯 Project Objective

Ask meaningful questions about the dataset, understand its structure, clean
it, uncover trends and anomalies, test assumptions about what drives
popularity, and present it all through clear, well-designed visuals — with
a Spotify-inspired visual theme throughout.

## 📌 EDA Workflow

1. **Data Overview** — shape, columns, data types, missing values,
   duplicates, styled summary statistics
2. **Data Cleaning** — dropping missing rows, removing cross-genre
   duplicates, type conversion, IQR outlier detection, sanity checks
3. **Univariate Analysis** — distributions of popularity, danceability,
   energy, tempo, duration, loudness, and explicit content
4. **Bivariate Analysis** — popularity vs danceability/energy, energy vs
   loudness, danceability vs valence, plus a full correlation summary
5. **Genre Deep-Dive** — a radar chart comparing the audio "fingerprint"
   of the top 5 genres by popularity
6. **What Makes a Hit?** — a direct comparison of "hit" tracks
   (popularity ≥ 70) vs the rest of the catalogue across every audio
   feature
7. **Categorical Analysis** — top 10 artists, top genres by average
   popularity, time signature breakdown
8. **Correlation Analysis** — full correlation heatmap of numeric audio
   features
9. **Insights & Conclusions** — key questions answered, an executive
   summary, data quality notes, and suggested next steps

## 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook / Google Colab

## 📂 Repository Structure

```
Task2_EDA/
│
├── Task2_Spotify_EDA.ipynb
├── data/
│   └── spotify_dataset.csv
├── charts/
│   ├── 01_univariate_distributions.png
│   ├── 02_duration_loudness_explicit.png
│   ├── 03_bivariate_relationships.png
│   ├── 04_genre_radar.png
│   ├── 05_hit_vs_nonhit.png
│   ├── 06_top_10_artists.png
│   ├── 07_top_10_genres_popularity.png
│   ├── 08_time_signature_counts.png
│   └── 09_correlation_heatmap.png
└── README.md
```

## 🚀 How to Run

### Option 1: Google Colab
1. Open [Google Colab](https://colab.research.google.com)
2. Upload `Task2_Spotify_EDA.ipynb`
3. Upload `data/spotify_dataset.csv` to the Colab session (or mount Drive)
4. Run all cells

### Option 2: Local Jupyter
```bash
pip install pandas numpy matplotlib seaborn jupyter
jupyter notebook Task2_Spotify_EDA.ipynb
```

## 📈 Key Insights

- **K-pop** and **pop-film** are the genres with the highest average
  popularity in the dataset.
- Neither **energy** nor **danceability** alone meaningfully predicts a
  track's popularity (correlations near 0).
- **Hit tracks** (popularity ≥ 70) are, on average, more danceable and
  louder, and noticeably less acoustic/instrumental than the rest of the
  catalogue.
- **Loudness and energy** are strongly correlated (~0.76); **danceability
  and valence** show a moderate positive relationship (~0.49).
- Every genre has a distinct audio "fingerprint" — metal skews high-energy
  and low-acoustic, chill is the opposite, and Latino scores high across
  danceability, energy, and valence.
- Only about **3.5%** of tracks in the cleaned dataset qualify as hits,
  reflecting music's typical long-tail popularity distribution.

See the notebook for the full analysis, all 9 charts, and the reasoning
behind each step.

