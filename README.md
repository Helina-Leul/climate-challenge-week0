# 🌍 Climate Challenge Week 0

This project analyzes climate data for five African countries using NASA POWER dataset and builds a climate vulnerability ranking system.

---

## ⚙️ Setup Instructions

1. Clone the repository
2. Install dependencies:

pip install -r requirements.txt


3. Run notebooks:
- notebooks/ethiopia_eda.ipynb
- notebooks/compare_countries.ipynb

4. Run dashboard:

streamlit run app/main.py


---

## 📊 Task 2 – Exploratory Data Analysis

- Temperature shows strong seasonal variation
- Precipitation is irregular with wet and dry seasons
- Humidity follows rainfall patterns
- Wind speed is relatively stable

### Correlation findings:
- Temperature and max temperature are strongly positive
- Temperature and humidity are negatively correlated

---

## 🌍 Task 3 – Climate Vulnerability Ranking

Countries analyzed:
- Ethiopia
- Kenya
- Sudan
- Tanzania
- Nigeria

A vulnerability score was calculated using:
- Mean temperature
- Dry days
- Extreme heat days

Countries were ranked based on climate risk.

---

## 📈 Dashboard

The Streamlit dashboard includes:
- Country selection
- Temperature trends
- Precipitation analysis
- Humidity and wind speed
- Vulnerability ranking visualization

---

## 📸 Screenshots

### Home Dashboard
![Home](dashboard_screenshots/home.png)

### Country View
![Country](dashboard_screenshots/ethiopia_view.png)

### Vulnerability Ranking
![Vulnerability](dashboard_screenshots/vulnerability.png)