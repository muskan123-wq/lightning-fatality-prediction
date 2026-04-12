# Lightning-Induced Fatality Analysis in India

##  Overview

This project presents a comprehensive analysis of lightning-induced fatalities across Indian states using a **data warehouse framework** combined with **machine learning techniques**.

The study integrates multiple heterogeneous datasets, including lightning activity, fatality records, and socio-economic indicators, to explore patterns, relationships, and risk factors influencing fatalities.

An interactive **Gradio-based prediction system** is also developed to estimate fatalities based on environmental and socio-economic inputs.

---

## Objectives

* Analyze spatial and temporal patterns of lightning-induced fatalities
* Integrate multi-source data using OLTP and data warehouse design
* Perform OLAP queries for analytical insights
* Apply machine learning models for predictive analysis
* Develop an interactive system for real-time prediction

---

## Dataset

The dataset consists of state-wise annual data (2019–2020) including:
* Lightning intensity
* Lightning-induced fatalities
* Poverty rate
* Literacy rate
* Population
* Forest cover percentage
* Lightning density

All datasets are available in the `/data` folder.

---

## Project Structure

```
datawarehouse/
│
├── data/
│   ├── final_dataset.csv
│   ├── lightning_intensity.csv
│   ├── lightning_fatalities.csv
│
├── scripts/
│   ├── analysis.py       
│   ├── app.py             
│
├── outputs/
│   ├── intensity_vs_fatalities.png
│   ├── avg_intensity_by_state.png
│   ├── poverty_vs_fatalities.png
│   ├── heatmap.png
│   ├── decision_tree.png
│   ├── feature_importance.png
│   ├── clustering.png
│
├── report.pdf
├── README.md
```

---

## Analysis & Visualization

The project includes the following key visualizations:

* Lightning Intensity vs Fatalities (Scatter Plot)
* Average Lightning Intensity by State (Bar Chart)
* Poverty Rate vs Fatalities (Regression Plot)
* Correlation Heatmap
* Regression Fit (Actual vs Predicted)
* Decision Tree Visualization
* Feature Importance Plot
* Clustering Analysis (PCA Projection)

---

##  Machine Learning Models

* **Linear Regression** (baseline model)
* **Decision Tree Regressor** (non-linear relationships)
* **K-Means Clustering** (pattern discovery)

### Key Insights

* Lightning intensity shows a positive relationship with fatalities
* Poverty rate significantly increases vulnerability
* Literacy rate has a protective (negative) effect
* Fatalities are influenced by both environmental and socio-economic factors

---

## Interactive Prediction System

A **Gradio-based web interface** allows users to input parameters and get real-time predictions.

### Run the app locally:

```
python scripts/app.py
```

---

## Installation & Setup

1. Clone the repository:

```
git clone <your-repo-link>
cd datawarehouse
```

2. Install dependencies:

```
pip install pandas matplotlib seaborn scikit-learn gradio
```

3. Run analysis:

```
python scripts/analysis.py
```

4. Run the app:

```
python scripts/app.py
```

---

## Limitations

* Data limited to 2019–2020
* State-level granularity only
* Limited sample size for machine learning
* Some external factors (weather, infrastructure) not included

---

## Future Work

* Extend dataset to multiple years
* Incorporate real-time lightning data
* Use advanced ML models (ensemble, deep learning)
* Build a deployable web application

---

## Author

**Muskan Kumari**
IISER Thiruvananthapuram
School of Data Science

---
