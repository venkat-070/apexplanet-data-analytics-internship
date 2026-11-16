"""
05_generate_notebooks.py
Generates clean, fully runnable, professional Jupyter Notebooks (.ipynb)
for all internship project tasks.
ApexPlanet Data Analytics Internship | Venkata Vedhadri Marisetti (23981A44Y9)
"""

import os
import json

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
NOTEBOOKS_DIR = os.path.join(PROJECT_ROOT, "notebooks")
os.makedirs(NOTEBOOKS_DIR, exist_ok=True)

def create_notebook(cells):
    return {
        "cells": cells,
        "metadata": {
            "language_info": {
                "name": "python",
                "version": "3.12"
            },
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 5
    }

def markdown_cell(source):
    return {
        "cell_type": "markdown",
        "metadata": {},
        "source": [line + "\n" for line in source.strip().split("\n")]
    }

def code_cell(source):
    return {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [line + "\n" for line in source.strip().split("\n")]
    }

# -------------------------------------------------------------------------
# Notebook 1: Data Immersion & Wrangling
# -------------------------------------------------------------------------
nb1_cells = [
    markdown_cell("""# ApexPlanet Data Analytics Internship
## Task 1: Data Immersion & Wrangling
**Student:** Venkata Vedhadri Marisetti (23981A44Y9)  
**Degree:** B.Tech CSE (Data Science), Raghu Engineering College (Autonomous)  
**Guide:** Md Imam Khader Shariff, Assistant Professor  
**Organization:** ApexPlanet Software Pvt. Ltd. | Certificate ID: APSPL2650541  

---
### Objectives:
1. Understand dataset structure and schema.
2. Detect missing, duplicate, and inconsistent data entries.
3. Clean, impute, normalize, and engineer analytical features.
4. Export cleansed data to CSV, Excel, and SQLite."""),
    code_cell("""import pandas as pd
import numpy as np
import os
import sqlite3

raw_path = os.path.join("..", "data", "raw", "global_superstore_raw.csv")
df_raw = pd.read_csv(raw_path)
print(f"Loaded Raw Dataset: {df_raw.shape[0]} rows, {df_raw.shape[1]} columns")
df_raw.head(3)"""),
    markdown_cell("""### 1. Data Quality Audit: Missing Values & Duplicates"""),
    code_cell("""print("Duplicate row count:", df_raw.duplicated().sum())
print("\nMissing values by column:")
print(df_raw.isnull().sum()[df_raw.isnull().sum() > 0])"""),
    markdown_cell("""### 2. Deduplication & Data Cleaning Pipeline"""),
    code_cell("""# 1. Deduplication
df_clean = df_raw.drop_duplicates().copy()

# 2. Clean numeric strings
if df_clean["Sales"].dtype == object:
    df_clean["Sales"] = df_clean["Sales"].astype(str).str.replace("$", "").str.replace(",", "").astype(float)

# 3. Standardize text casing
for col in ["Segment", "Category", "Sub_Category", "Ship_Mode", "Region", "Country"]:
    df_clean[col] = df_clean[col].astype(str).str.strip().str.title()

# 4. Standardize dates
df_clean["Order_Date"] = pd.to_datetime(df_clean["Order_Date"], format="mixed")
df_clean["Ship_Date"] = pd.to_datetime(df_clean["Ship_Date"], format="mixed")
df_clean["Lead_Time_Days"] = (df_clean["Ship_Date"] - df_clean["Order_Date"]).dt.days

# 5. Missing value imputations
df_clean["Discount"] = df_clean["Discount"].fillna(0.0)
df_clean["Shipping_Cost"] = df_clean["Shipping_Cost"].fillna(df_clean["Shipping_Cost"].median())
df_clean["Customer_Name"] = df_clean["Customer_Name"].fillna("Verified Client")
df_clean["Postal_Code"] = df_clean["Postal_Code"].fillna("Unknown")

# 6. Feature Engineering
df_clean["Total_Cost"] = df_clean["Quantity"] * df_clean["Cost_Price"]
df_clean["Profit"] = (df_clean["Sales"] - df_clean["Total_Cost"] - (df_clean["Shipping_Cost"] * 0.4)).round(2)
df_clean["Profit_Margin_Pct"] = ((df_clean["Profit"] / df_clean["Sales"]) * 100).round(2)

print(f"Data Cleaning Completed! Cleaned rows: {len(df_clean)}, Remaining nulls: {df_clean.isnull().sum().sum()}")
df_clean[["Order_ID", "Customer_Name", "Sales", "Profit", "Profit_Margin_Pct", "Lead_Time_Days"]].head()""")
]

with open(os.path.join(NOTEBOOKS_DIR, "01_task1_data_immersion_and_wrangling.ipynb"), "w", encoding="utf-8") as f:
    json.dump(create_notebook(nb1_cells), f, indent=2)

# -------------------------------------------------------------------------
# Notebook 2: EDA & SQL Analytics
# -------------------------------------------------------------------------
nb2_cells = [
    markdown_cell("""# ApexPlanet Data Analytics Internship
## Task 2: Exploratory Data Analysis (EDA) & SQL Analytics
**Student:** Venkata Vedhadri Marisetti (23981A44Y9) | Raghu Engineering College  
**Guide:** Md Imam Khader Shariff, Assistant Professor  

---
### Objectives:
1. Calculate parametric & non-parametric summary metrics (mean, median, standard deviation, IQR).
2. Univariate and multivariate exploratory analysis.
3. Execute production SQL queries (SELECT, WHERE, GROUP BY, ORDER BY, Window Functions)."""),
    code_cell("""import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sqlite3
import os

clean_path = os.path.join("..", "data", "processed", "clean_superstore_data.csv")
db_path = os.path.join("..", "data", "database", "analytics.db")

df = pd.read_csv(clean_path)
print(f"Loaded Clean Dataset: {len(df):,} records")"""),
    markdown_cell("""### 1. Summary Statistics: Parametric vs. Non-Parametric"""),
    code_cell("""num_cols = ["Sales", "Profit", "Quantity", "Discount", "Shipping_Cost", "Profit_Margin_Pct"]
stats_summary = df[num_cols].describe().T
stats_summary["IQR"] = stats_summary["75%"] - stats_summary["25%"]
stats_summary["Skewness"] = df[num_cols].skew()
stats_summary[["mean", "50%", "std", "IQR", "min", "max", "Skewness"]].rename(columns={"50%": "median"})"""),
    markdown_cell("""### 2. SQL Analytics Engine Querying"""),
    code_cell("""conn = sqlite3.connect(db_path)

# Query 1: Executive KPI Scorecard
kpi_query = \"\"\"
SELECT 
    COUNT(DISTINCT Order_ID) AS Total_Orders,
    COUNT(DISTINCT Customer_ID) AS Total_Customers,
    ROUND(SUM(Sales), 2) AS Total_Revenue,
    ROUND(SUM(Profit), 2) AS Total_Profit,
    ROUND((SUM(Profit) / SUM(Sales)) * 100, 2) AS Margin_Pct,
    ROUND(SUM(Sales) / COUNT(DISTINCT Order_ID), 2) AS AOV
FROM orders;
\"\"\"
pd.read_sql_query(kpi_query, conn)"""),
    code_cell("""# Query 2: Product Category Performance Breakdown
cat_query = \"\"\"
SELECT 
    Category,
    COUNT(DISTINCT Order_ID) AS Orders,
    ROUND(SUM(Sales), 2) AS Total_Revenue,
    ROUND(SUM(Profit), 2) AS Total_Profit,
    ROUND((SUM(Profit) / SUM(Sales)) * 100, 2) AS Margin_Pct
FROM orders
GROUP BY Category
ORDER BY Total_Revenue DESC;
\"\"\"
pd.read_sql_query(cat_query, conn)""")
]

with open(os.path.join(NOTEBOOKS_DIR, "02_task2_eda_and_sql_analytics.ipynb"), "w", encoding="utf-8") as f:
    json.dump(create_notebook(nb2_cells), f, indent=2)

# -------------------------------------------------------------------------
# Notebook 3: Deep-Dive & Dashboards
# -------------------------------------------------------------------------
nb3_cells = [
    markdown_cell("""# ApexPlanet Data Analytics Internship
## Task 3: Deep-Dive Analytics & RFM Customer Segmentation
**Student:** Venkata Vedhadri Marisetti (23981A44Y9) | Raghu Engineering College  
**Guide:** Md Imam Khader Shariff, Assistant Professor  

---
### Objectives:
1. Customer RFM (Recency, Frequency, Monetary) segmentation.
2. Dimensional deep-dive across customers, categories, regions, and discount elasticity.
3. Executive KPI computation and dashboard metrics preparation."""),
    code_cell("""import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

rfm_path = os.path.join("..", "data", "processed", "rfm_customer_segments.csv")
rfm = pd.read_csv(rfm_path)
print(f"Loaded RFM Segmented Customers: {len(rfm)} accounts")
rfm.head()"""),
    markdown_cell("""### 1. RFM Segment Breakdown & Financial Contribution"""),
    code_cell("""rfm_summary = rfm.groupby("Customer_Lifecycle_Segment").agg(
    Customers=("Customer_ID", "count"),
    Total_Spend=("Monetary", "sum"),
    Total_Profit=("Total_Profit", "sum"),
    Avg_Orders=("Frequency", "mean")
).reset_index().sort_values("Total_Spend", ascending=False)
rfm_summary["Spend_Share_Pct"] = (rfm_summary["Total_Spend"] / rfm_summary["Total_Spend"].sum() * 100).round(2)
rfm_summary"""),
    markdown_cell("""### 2. Discount Sensitivity & Profit Margin Decay"""),
    code_cell("""clean_path = os.path.join("..", "data", "processed", "clean_superstore_data.csv")
df = pd.read_csv(clean_path)

discount_summary = df.groupby("Discount_Tier").agg(
    Order_Count=("Order_ID", "count"),
    Avg_Discount=("Discount", lambda x: f"{x.mean()*100:.1f}%"),
    Total_Revenue=("Sales", "sum"),
    Total_Profit=("Profit", "sum"),
    Avg_Margin=("Profit_Margin_Pct", "mean")
).round(2).reset_index()
discount_summary""")
]

with open(os.path.join(NOTEBOOKS_DIR, "03_task3_deep_dive_and_kpis.ipynb"), "w", encoding="utf-8") as f:
    json.dump(create_notebook(nb3_cells), f, indent=2)

# -------------------------------------------------------------------------
# Notebook 4: Statistical Validation & Storytelling
# -------------------------------------------------------------------------
nb4_cells = [
    markdown_cell("""# ApexPlanet Data Analytics Internship
## Task 4: Statistical Validation & Data Storytelling
**Student:** Venkata Vedhadri Marisetti (23981A44Y9) | Raghu Engineering College  
**Guide:** Md Imam Khader Shariff, Assistant Professor  

---
### Objectives:
1. Hypothesis formulation: Null ($H_0$) vs. Alternative ($H_1$).
2. Hypothesis testing with Welch's t-test, Mann-Whitney U, One-Way ANOVA, and Chi-Square.
3. Compute test statistics, degrees of freedom, p-values, effect sizes (Cohen's d), and 95% CIs.
4. Executive Data Storytelling: Problem -> Analysis -> Insight -> Visual -> Recommendation."""),
    code_cell("""import pandas as pd
import numpy as np
from scipy import stats
import os

clean_path = os.path.join("..", "data", "processed", "clean_superstore_data.csv")
df = pd.read_csv(clean_path)

# Test 1: Welch's t-test for Discount vs Profit
low_disc = df[df["Discount"] <= 0.10]["Profit"]
high_disc = df[df["Discount"] > 0.10]["Profit"]

t_stat, p_val = stats.ttest_ind(low_disc, high_disc, equal_var=False)
u_stat, p_val_u = stats.mannwhitneyu(low_disc, high_disc)

print("Hypothesis Test 1: Discount Impact on Profitability")
print(f"Low Discount Mean Profit:  ${low_disc.mean():.2f}")
print(f"High Discount Mean Profit: ${high_disc.mean():.2f}")
print(f"Welch's t-statistic: {t_stat:.4f}, p-value: {p_val:.4e}")
print(f"Mann-Whitney U: {u_stat:.1f}, p-value: {p_val_u:.4e}")
print("Decision at alpha=0.05: " + ("REJECT H0" if p_val < 0.05 else "FAIL TO REJECT H0"))"""),
    code_cell("""# Test 2: One-Way ANOVA for Regional Sales
regions = df["Region"].unique()
region_groups = [df[df["Region"] == r]["Sales"] for r in regions]

f_stat, p_val_f = stats.f_oneway(*region_groups)
print("\nHypothesis Test 2: Regional Sales Uniformity")
print(f"ANOVA F-statistic: {f_stat:.4f}, p-value: {p_val_f:.4f}")
print("Decision at alpha=0.05: " + ("REJECT H0" if p_val_f < 0.05 else "FAIL TO REJECT H0"))"""),
    code_cell("""# Test 3: Chi-Square Test of Independence (Segment vs Category)
contingency = pd.crosstab(df["Segment"], df["Category"])
chi2_stat, p_val_chi2, dof, _ = stats.chi2_contingency(contingency)

print("\nHypothesis Test 3: Segment vs Category Independence")
print(f"Chi-Square: {chi2_stat:.4f}, p-value: {p_val_chi2:.4f}, dof: {dof}")
print("Decision at alpha=0.05: " + ("REJECT H0" if p_val_chi2 < 0.05 else "FAIL TO REJECT H0"))""")
]

with open(os.path.join(NOTEBOOKS_DIR, "04_task4_statistical_validation_and_storytelling.ipynb"), "w", encoding="utf-8") as f:
    json.dump(create_notebook(nb4_cells), f, indent=2)

print("All 4 Jupyter Notebooks generated successfully in notebooks/!")
