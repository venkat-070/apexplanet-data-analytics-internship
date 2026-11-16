<div align="center">

# 📊 Enterprise Omnichannel Data Analytics & Business Intelligence
### **ApexPlanet Software Pvt. Ltd. — Data Analytics Internship Project**

![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Wrangling-150458?style=for-the-badge&logo=pandas&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-SQLite%20%7C%20Window%20Functions-CC292B?style=for-the-badge&logo=sqlite&logoColor=white)
![Power BI](https://img.shields.io/badge/Power%20BI-Dashboard-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed%20%26%20Validated-success?style=for-the-badge)

</div>

---

## 👨‍🎓 Student & Academic Credentials
* **Student Name:** **Venkata Vedhadri Marisetti**
* **Hall Ticket / Roll No.:** `23981A44Y9`
* **Degree & Specialization:** B.Tech Computer Science and Engineering (Data Science)
* **Institution:** Raghu Engineering College (Autonomous), Visakhapatnam
* **Academic Guide:** **Md Imam Khader Shariff**, Assistant Professor
* **Academic Year:** 2026–2027
* **Internship Organization:** **ApexPlanet Software Pvt. Ltd.** (Virtual/Online)
* **Internship Tenure:** 01 August 2026 – 30 September 2026 (8 Weeks & 4 Days)
* **Certificate ID:** `APSPL2650541`

---

## 📌 Executive Summary & Project Overview
This repository contains the complete industrial-grade Data Analytics Capstone developed during the 8-week internship at **ApexPlanet Software Pvt. Ltd.** The project investigates an enterprise omnichannel retail dataset of **5,500+ transactions ($3.19M Gross Sales, $907.5K Operating Profit)** to diagnose root causes of profit margin erosion, optimize promotional discounting, and construct automated Business Intelligence dashboards.

```
========================================================================================================
                                      EXECUTIVE KPI SCORECARD
  Gross Revenue: $3,190,836.65   |   Net Profit: $907,565.75   |   Profit Margin: 28.44%
  Total Orders:  5,500           |   Active Clients: 450       |   Average Order Value: $580.15
========================================================================================================
```

---

## 🔄 The 8-Stage Data Analytics Workflow
```mermaid
flowchart LR
    A["1. Collection"] --> B["2. Understanding"]
    B --> C["3. Cleaning"]
    C --> D["4. Transformation"]
    D --> E["5. EDA"]
    E --> F["6. Visualization"]
    F --> G["7. Insights"]
    G --> H["8. Reporting"]
```

1. **Collection:** Multi-source transactional data ingestion across global sales channels.
2. **Understanding:** Auditing dimensions, data types, distributions, and null values.
3. **Cleaning:** Removing duplicate entries, imputing missing values, and standardizing formats.
4. **Transformation:** Feature engineering (`Lead_Time_Days`, `Profit_Margin_Pct`, `Discount_Tier`).
5. **EDA:** Univariate and multivariate statistical analysis with parametric and non-parametric indicators.
6. **Visualization:** Publication-grade visuals with Matplotlib, Seaborn, and interactive web charts.
7. **Insights:** Empirical discovery of discount margin decay and customer lifetime value.
8. **Reporting:** Executive data storytelling, hypothesis validation, and GitHub portfolio delivery.

---

## 🛠️ Technologies & Tools Used
* **Python 3.12:** Core processing, data cleaning, automated feature engineering.
* **Pandas & NumPy:** In-memory vectorization, time-series parsing, data wrangling.
* **SQL (SQLite & ANSI SQL):** Relational schema design, CTEs, window functions (`LAG`, `DENSE_RANK`, `SUM() OVER()`).
* **Microsoft Excel:** Multi-tab formatted analytical workbooks, pivot tables, and regional summaries (`clean_superstore_data.xlsx`).
* **Power BI & Web BI:** Interactive responsive executive dashboard (`dashboard/index.html`) featuring Chart.js, slicers, and real-time filtering.
* **Matplotlib & Seaborn:** Publication-quality distribution plots, correlation heatmaps, and Pareto charts.
* **SciPy:** Rigorous inferential statistical hypothesis testing (Welch's t-test, Mann-Whitney U, One-Way ANOVA, Chi-Square).
* **Git & GitHub:** Version control, continuous integration, and portfolio presentation.

---

## 📂 Repository Structure
```
apexplanet-data-analytics-internship/
├── .gitignore                                 <- Git ignore rules
├── README.md                                  <- Master portfolio documentation
├── requirements.txt                           <- Python environment dependencies
│
├── data/
│   ├── raw/
│   │   └── global_superstore_raw.csv          <- Raw dataset with authentic imperfections
│   ├── processed/
│   │   ├── clean_superstore_data.csv          <- Cleaned, validated, enriched dataset
│   │   ├── clean_superstore_data.xlsx         <- Multi-sheet Excel workbook with Pivot tables
│   │   └── rfm_customer_segments.csv          <- RFM customer segmentation scores
│   └── database/
│       ├── analytics.db                       <- Indexed SQLite relational database
│       └── schema.sql                         <- DDL schema definition
│
├── sql/
│   ├── 01_schema_setup.sql                    <- Relational staging and indexes
│   ├── 02_data_cleaning_audit.sql             <- SQL validation, null & duplicate checks
│   ├── 03_business_kpis.sql                   <- Executive scorecard & category breakdown
│   ├── 04_deep_dive_analytics.sql             <- CTEs, window functions, MoM growth, Pareto
│   └── 05_rfm_segmentation.sql                <- Quintile RFM segmentation queries
│
├── scripts/
│   ├── 00_generate_dataset.py                 <- Multi-year enterprise dataset generator
│   ├── 01_data_wrangling.py                   <- Task 1: Data Immersion & Wrangling Pipeline
│   ├── 02_eda_and_bi.py                       <- Task 2: Descriptive stats & SQL engine
│   ├── 03_deep_dive_analysis.py               <- Task 3: RFM segmentation & Dashboard engine
│   ├── 04_statistical_validation.py           <- Task 4: Hypothesis tests & Storytelling
│   ├── 05_generate_notebooks.py               <- Task 5: Jupyter Notebook generation
│   └── run_all.py                             <- Master single-command pipeline runner
│
├── notebooks/
│   ├── 01_task1_data_immersion_and_wrangling.ipynb
│   ├── 02_task2_eda_and_sql_analytics.ipynb
│   ├── 03_task3_deep_dive_and_kpis.ipynb
│   └── 04_task4_statistical_validation_and_storytelling.ipynb
│
├── visuals/
│   ├── 01_missing_data_matrix.png             <- Pre-cleaning missing value distribution
│   ├── 02_sales_profit_distribution.png       <- Univariate KDE & financial histograms
│   ├── 03_correlation_matrix.png              <- Multivariate correlation heatmap
│   ├── 04_category_performance_pareto.png     <- 80/20 revenue Pareto distribution
│   ├── 05_regional_profitability_map.png      <- Regional sales vs profit margins
│   ├── 06_monthly_sales_trend_seasonality.png <- 2024-2026 monthly sales & 3M moving avg
│   ├── 07_rfm_customer_segments.png           <- RFM customer lifecycle distribution
│   ├── 08_discount_vs_profit_decay.png        <- Profit margin erosion vs discount curve
│   └── 09_hypothesis_test_distributions.png   <- Statistical test boxplots & ANOVA bars
│
├── dashboard/
│   ├── index.html                             <- Interactive Power BI-style Web BI Dashboard
│   ├── styles.css                             <- Glassmorphism dark executive theme
│   ├── app.js                                 <- Dynamic Chart.js and slicer engine
│   └── data.json                              <- Pre-calculated analytical payload
│
└── reports/
    ├── data_quality_audit.md                  <- Pre/post cleaning data health audit
    ├── sql_query_analysis.md                  <- SQL verification and financial outputs
    ├── deep_dive_analysis_report.md           <- RFM and dimensional breakdown report
    ├── statistical_test_results.md            <- p-values, test statistics, 95% CIs
    ├── data_storytelling_report.md            <- Problem -> Analysis -> Insight -> Action
    ├── executive_summary.md                   <- C-suite executive summary
    └── internship_completion_report.md        <- Formal ApexPlanet completion report
```

---

## 🔬 Detailed Internship Task Walkthrough

### 🔹 Task 1: Data Immersion & Wrangling
* **Audit:** Audited 5,580 initial transactional rows; detected 66 duplicate orders and missing values in `Postal_Code` (2.87%), `Shipping_Cost` (2.58%), `Customer_Name` (2.04%), and `Discount` (1.34%).
* **Cleaning Pipeline:**
  - Automated deduplication dropping redundant transactions.
  - Stripped non-numeric currency symbols (`$`, `,`) in `Sales` and normalized to `float64`.
  - Multi-format date parser standardized mixed date formats into ISO-8601 (`YYYY-MM-DD`).
  - Contextual modal imputation for postal codes and stratified median imputation for shipping fees.
* **Feature Engineering:** Derived `Lead_Time_Days`, `Unit_Price`, `Total_Cost`, `Profit_Margin_Pct`, `Discount_Tier`, and calendar hierarchies.
* **Outputs:** Clean CSV, Multi-tab Excel workbook with Pivot tables, and indexed SQLite tables.

### 🔹 Task 2: Exploratory Data Analysis & Relational SQL Analytics
* **Descriptive Summary:**
  | Metric | Sales ($) | Profit ($) | Quantity | Discount | Shipping Cost ($) | Lead Time (Days) |
  |:---|---:|---:|---:|---:|---:|---:|
  | **Mean** | 578.68 | 164.59 | 2.96 | 0.10 | 17.95 | 3.52 |
  | **Median** | 180.17 | 51.20 | 3.00 | 0.05 | 17.73 | 3.00 |
  | **Std. Dev** | 966.45 | 318.12 | 1.87 | 0.13 | 6.22 | 1.35 |
  | **IQR** | 612.50 | 174.49 | 2.00 | 0.15 | 9.06 | 1.00 |
  | **Skewness** | +3.24 | +3.59 | +1.11 | +1.65 | +0.32 | +0.48 |
* **SQL Query Execution:**
  - Designed 5 production SQL scripts with Window functions (`LAG()`, `DENSE_RANK()`, `SUM() OVER()`).
  - Audited month-over-month (MoM) revenue growth and Top-5 product lines by category.

### 🔹 Task 3: Deep-Dive Multi-Dimensional Analytics & BI Dashboard
* **Customer RFM Segmentation:** Evaluated 450 customer accounts on Recency, Frequency, and Monetary quintiles (1-5 scale) into 6 actionable lifecycle cohorts:
  - *Champions & Loyal Customers* (38% of accounts) contribute 54% of net profit.
  - *At Risk & Hibernating* accounts prioritized for automated reactivation.
* **Pareto 80/20 Analysis:** Top 6 sub-categories (Chairs, Copiers, Phones, Bookcases, Machines, Storage) represent 72% of gross revenue.
* **Interactive BI Dashboard (`dashboard/index.html`):**
  - Live interactive slicers for Region, Category, Customer Segment, and Discount Tier.
  - Real-time recalculation of all 6 KPI cards.
  - Interactive Chart.js charts: Monthly Revenue/Profit trend, Category Donut, Regional Margin Bars, and RFM Polar Chart.
  - Transaction table with client-side live search.

### 🔹 Task 4: Inferential Statistical Hypothesis Testing & Storytelling
Three rigorous statistical hypothesis tests were conducted at significance level $\alpha = 0.05$:

#### 🧪 Test 1: Impact of Promotional Discounts on Profitability
* **$H_0$:** Net profit per order for low discounts ($\le 10\%$) is equal to or less than high discounts ($> 10\%$) ($\mu_{low} \le \mu_{high}$).
* **$H_1$:** Promotional discounts significantly erode net profit per order ($\mu_{low} > \mu_{high}$).
* **Statistical Output:**
  - Low Discount Mean Profit: **$211.11** ($n = 3,771$)
  - High Discount Mean Profit: **$63.95** ($n = 1,743$)
  - **Welch's $t$-statistic:** **20.2793**, **$p$-value:** **$3.31 \times 10^{-88}$**
  - **Mann-Whitney $U$-statistic:** **$4,547,979$**, **$p$-value:** **$1.36 \times 10^{-116}$**
  - **Cohen's $d$ Effect Size:** **0.474** (Medium-to-large practical impact)
  - **95% Confidence Interval for Loss:** **[$132.94, $161.38]** per transaction.
* **Decision:** **REJECT $H_0$**. Aggressive discounts significantly degrade operating profitability.

#### 🧪 Test 2: Regional Sales Uniformity
* **$H_0$:** Mean transaction sales are identical across all operating regions.
* **One-Way ANOVA:** $F = 1.3928, p = 0.2337$.
* **Decision:** **FAIL TO REJECT $H_0$**. Per-order basket sizes are consistent nationwide.

#### 🧪 Test 3: Customer Segment Independence Across Product Categories
* **$H_0$:** Customer segment and product category preferences are independent.
* **Chi-Square Test:** $\chi^2 = 4.7551, p = 0.3134, dof = 4$.
* **Decision:** **FAIL TO REJECT $H_0$**. Uniform category demand across consumer and corporate clients.

---

## 📈 Key Visualizations
* `visuals/02_sales_profit_distribution.png`: Parametric/non-parametric distributions and positive skew.
* `visuals/03_correlation_matrix.png`: Negative correlation between discount and operating margin.
* `visuals/04_category_performance_pareto.png`: Cumulative 80/20 sub-category sales concentration.
* `visuals/05_regional_profitability_map.png`: Regional revenue vs net operating margin comparison.
* `visuals/07_rfm_customer_segments.png`: Customer scatter plot of Recency vs Monetary spend.
* `visuals/08_discount_vs_profit_decay.png`: Empirical profit margin decay curve crossing $0 at >20% discount.
* `visuals/09_hypothesis_test_distributions.png`: Boxplot and ANOVA confidence intervals validating hypotheses.

---

## 🚀 How to Run & Reproduce Locally

### 1. Clone the Repository
```bash
git clone https://github.com/venkat-070/apexplanet-data-analytics-internship.git
cd apexplanet-data-analytics-internship
```

### 2. Set Up Virtual Environment & Install Dependencies
```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate

pip install -r requirements.txt
```

### 3. Run the Entire Pipeline in One Command
```bash
python scripts/run_all.py
```
This single command automatically generates the raw data, executes data wrangling, performs EDA, executes SQL queries, computes RFM segmentation, runs statistical hypothesis testing, and builds all 4 Jupyter Notebooks.

### 4. Open the Interactive BI Dashboard
Simply open `dashboard/index.html` in any web browser:
```bash
# Windows
start dashboard/index.html
# macOS
open dashboard/index.html
# Linux
xdg-open dashboard/index.html
```

---

## 🌐 Applications of Data Analytics Across Industries
* **Business & Retail:** Dynamic pricing, margin protection, customer lifetime value modeling, churn reduction.
* **Finance:** Credit risk scoring, fraud detection algorithms, algorithmic portfolio balancing.
* **Healthcare:** Clinical resource planning, length-of-stay forecasting, drug efficacy trials.
* **Education:** Predictive student retention, engagement scoring, personalized learning pathways.
* **E-Commerce:** Recommendation engines, search re-ranking, automated inventory replenishment.
* **Manufacturing:** Predictive maintenance, supply chain lead-time optimization, quality control.

---

## 💡 Strategic Business Recommendations
1. **Institute a Strict 15% Maximum Discount Policy:** Frontline discounts $>15\%$ must require regional VP approval to protect margins.
2. **Prioritize High-Margin Technology Bundles:** Leverage Technology's 28.3% margin by cross-selling low-cost Office Supplies accessories.
3. **Automate RFM Churn Interventions:** Trigger automated win-back incentives for the 18% of accounts currently in the "At Risk" quadrant.
4. **Fulfillment Consolidation:** Maintain the 3.52-day fulfillment lead time by consolidating ground shipping carriers.

---

## 🎓 Acknowledgments
Special thanks to **Md Imam Khader Shariff, Assistant Professor**, Department of CSE (Data Science), **Raghu Engineering College (Autonomous)**, for continuous academic guidance, and to **ApexPlanet Software Pvt. Ltd.** for providing this virtual internship opportunity.
