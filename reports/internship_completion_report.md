# DATA ANALYTICS INTERNSHIP COMPLETION REPORT
**ApexPlanet Software Pvt. Ltd.** | *Virtual / Online Mode*  
**Internship Duration:** 01 August 2026 – 30 September 2026 (8 Weeks & 4 Days)  
**Certificate ID:** `APSPL2650541`  

---

### Student & Academic Details
* **Student Name:** Venkata Vedhadri Marisetti
* **Registration / Roll No.:** 23981A44Y9
* **Academic Program:** B.Tech Computer Science and Engineering (Data Science)
* **Institution:** Raghu Engineering College (Autonomous), Visakhapatnam
* **Academic Guide:** Md Imam Khader Shariff, Assistant Professor
* **Academic Year:** 2026–2027

---

## 1. Introduction & Organizational Background
### 1.1 Why Data Analytics?
In modern enterprise environments, raw transactional data is collected at massive scale across point-of-sale systems, websites, logistics pipelines, and customer relationship portals. However, raw data in its unprocessed state provides little operational value.

**Data Analytics** is the rigorous discipline of collecting, cleaning, transforming, and modeling data to discover actionable patterns, validate operational hypotheses, and guide strategic business decision-making. By converting disparate data points into structured intelligence, organizations reduce operational friction, optimize pricing, elevate customer retention, and maximize profitability.

### 1.2 ApexPlanet Software Pvt. Ltd.
ApexPlanet Software Pvt. Ltd. is a technology organization providing applied technology consulting and experiential industrial internship programs. The structured 8-week program emphasized practical data handling, production SQL workflows, business intelligence dashboard design, inferential statistics, and executive storytelling.

---

## 2. Objectives & End-to-End Analytics Workflow
### 2.1 Core Program Objectives
1. Master core Data Analytics principles and data wrangling workflows.
2. Identify and resolve data anomalies, missingness, duplicate transactions, and type inconsistencies.
3. Conduct exploratory data analysis (EDA) and execute relational SQL queries.
4. Construct interactive business intelligence dashboards and tracking key performance indicators (KPIs).
5. Apply inferential statistics to validate business hypotheses and craft data-driven narratives.
6. Assemble a version-controlled, production-grade GitHub portfolio repository.

### 2.2 The 8-Stage Data Analytics Workflow
```
[1. Collection]    ---> [2. Understanding] ---> [3. Cleaning]       ---> [4. Transformation]
Raw CSV / Lake          Schema & Dtypes         Dedupe & Impute          Feature Engineering
      |                                                                         |
      v                                                                         v
[8. Reporting]     <--- [7. Insights]      <--- [6. Visualization] <--- [5. EDA]
Story & Portfolio       Decisions & Actions      Power BI & Seaborn       Distributions & SQL
```

---

## 3. Technologies & Analytical Tools Used
| Category | Tool / Technology | Specific Analytical Role |
|:---|:---|:---|
| **Programming** | **Python (v3.12)** | Data wrangling, statistical modeling, algorithmic automation |
| **Data Manipulation** | **Pandas & NumPy** | In-memory indexing, vectorization, null imputation, grouping |
| **Database** | **SQLite & ANSI SQL** | Relational data warehousing, CTEs, window functions (`LAG`, `RANK`) |
| **Spreadsheets** | **Microsoft Excel** | Multi-sheet workbooks, pivot summaries, structured validation |
| **Business Intelligence** | **Power BI / Chart.js** | Interactive slicers, KPI scorecards, visual analytics dashboards |
| **Visualization** | **Matplotlib & Seaborn** | Publication-quality charts (Pareto curves, KDEs, heatmaps) |
| **Statistical Analysis**| **SciPy (Stats)** | Welch's t-test, Mann-Whitney U, One-Way ANOVA, Chi-Square |
| **Version Control** | **Git & GitHub** | Code lifecycle management, artifact versioning, documentation |

---

## 4. Detailed Task Implementation & Findings

### Task 1: Data Immersion & Wrangling
* **Raw Dataset:** 5,580 records across 24 columns capturing global multi-channel retail orders.
* **Audit & Quality Checks:**
  - 66 duplicate transactions detected and removed.
  - Missing data resolved: `Postal_Code` (2.87%), `Shipping_Cost` (2.58%), `Customer_Name` (2.04%), `Discount` (1.34%).
  - Inconsistent date formats (`YYYY-MM-DD`, `DD/MM/YYYY`, `MM-DD-YYYY`) normalized into ISO-8601.
  - Stripped non-numeric currency artifacts (`$`, `,`) from financial metrics.
* **Feature Engineering:** Derived `Lead_Time_Days`, `Unit_Price`, `Total_Cost`, `Profit_Margin_Pct`, `Discount_Tier`, and temporal dimensions (`Order_Year`, `Order_Month`, `Order_Quarter`).
* **Artifacts Delivered:**
  - Clean CSV: `data/processed/clean_superstore_data.csv`
  - Multi-tab Excel: `data/processed/clean_superstore_data.xlsx`
  - Relational Database: `data/database/analytics.db` with indexes on primary transaction dimensions.

### Task 2: Exploratory Data Analysis & Business Intelligence
* **Descriptive Statistics:**
  - Parametric metrics: Mean Sales = $578.68, Mean Profit = $164.59, Mean Lead Time = 3.52 days.
  - Non-parametric metrics: Median Sales = $180.17, Median Profit = $51.20, IQR = $612.50.
  - Sales and Profit exhibited positive skewness (3.24 and 3.59 respectively), characteristic of long-tail high-ticket enterprise transactions.
* **SQL Query Implementation:**
  - Developed 5 modular SQL scripts in `sql/` incorporating `SELECT`, `WHERE`, `GROUP BY`, `ORDER BY`, `HAVING`, CTEs, and window functions (`LAG()`, `DENSE_RANK()`, `SUM() OVER()`).
  - Executive KPI verification confirmed $3,190,836.65 in gross revenue and $907,565.75 in net operating profit across 5,500 unique orders.

### Task 3: Deep-Dive Analytics & Interactive BI Dashboard
* **Customer RFM Segmentation:** Evaluated 450 accounts on Recency, Frequency, and Monetary scores (1–5 scale).
  - *Champions & Loyal Customers* comprise 38% of accounts but generate over 54% of lifetime profit.
  - *At-Risk / Hibernating* accounts identified for automated win-back workflows.
* **Pareto 80/20 Rule:** 6 core sub-categories (Chairs, Copiers, Phones, Bookcases, Machines, Storage) drive 72% of cumulative volume.
* **Interactive Web BI Dashboard (`dashboard/index.html`):**
  - Live slicers for Region, Category, Customer Segment, and Discount Tiers.
  - Real-time recalculation of KPI scorecards (Revenue, Profit, Margin, AOV, Order count).
  - Responsive charts: Monthly time-series, Category donut, Regional margin comparisons, and RFM polar distributions.
  - Filterable live transaction explorer table with client-side search.

### Task 4: Storytelling & Statistical Hypothesis Testing
* **Hypothesis Test 1 (Promotional Discount Impact on Profitability):**
  - $H_0$: $\mu_{low} \le \mu_{high}$ vs. $H_1$: $\mu_{low} > \mu_{high}$ ($\alpha = 0.05$)
  - Low Discount ($\le 10\%$) Mean Profit = **$211.11** vs. High Discount ($> 10\%$) Mean Profit = **$63.95**
  - Welch's $t = 20.2793$, $p = 3.31 \times 10^{-88}$ (Reject $H_0$)
  - Mann-Whitney $U = 4,547,979$, $p = 1.36 \times 10^{-116}$
  - Cohen's $d = 0.474$; 95% Confidence Interval for profit loss: **[$132.94, $161.38]** per transaction.
* **Hypothesis Test 2 (Regional Sales Variance):**
  - One-Way ANOVA $F = 1.3928$, $p = 0.2337$ (Fail to reject $H_0$); regional basket sizes remain homogeneous.
* **Hypothesis Test 3 (Customer Segment vs. Product Category Choice):**
  - Pearson's $\chi^2 = 4.7551$, $p = 0.3134$ (Fail to reject $H_0$); category preferences are uniform across customer tiers.
* **Storytelling Framework:** Problem ("The Gross Volume Illusion") $\rightarrow$ Analysis $\rightarrow$ Discovery $\rightarrow$ Visual Evidence $\rightarrow$ Strategic Recommendation.

### Task 5: Capstone & Portfolio Assembly
* Automated end-to-end execution pipeline via `scripts/run_all.py`.
* 4 fully executable Jupyter Notebooks in `notebooks/`.
* 9 publication-grade visualizations in `visuals/`.
* Professional README documentation with system architecture, badges, and quick-start instructions.

---

## 5. Applications of Data Analytics Across Industries
1. **Business & Retail:** Dynamic pricing optimization, churn prevention, basket affinity analysis.
2. **Finance & Banking:** Credit scoring, algorithmic fraud detection, investment portfolio stress testing.
3. **Healthcare:** Patient readmission prediction, clinical resource scheduling, epidemiology modeling.
4. **Education:** Student engagement tracking, adaptive learning curriculum tuning, retention analytics.
5. **E-Commerce & Digital Commerce:** Recommendation algorithms, search ranking, inventory replenishment.
6. **Manufacturing & Logistics:** Predictive equipment maintenance, lead time forecasting, route optimization.

---

## 6. Key Skills Acquired & Learning Outcomes
### 6.1 Technical Competencies Developed
- Advanced data wrangling, missingness imputation strategies, and schema validation.
- In-depth SQL development utilizing CTEs, window functions, and relational indexing.
- Dimensional customer segmentation utilizing mathematical RFM quintile algorithms.
- Parametric and non-parametric hypothesis testing with effect size estimation.
- Interactive BI dashboard development and data-driven storytelling.

### 6.2 Key Learning Principles
1. **Data preparation precedes analytics:** High-quality cleaning accounts for over 80% of project efficacy.
2. **Context dictates visual selection:** Matching the business question to the appropriate visualization is paramount.
3. **Statistical validation protects business capital:** Empirical testing prevents misleading correlation conclusions.

---

## 7. Conclusion & Acknowledgments
The 8-week Data Analytics Internship at **ApexPlanet Software Pvt. Ltd.** successfully bridged theoretical academic foundations at **Raghu Engineering College (Autonomous)** with practical enterprise data science workflows.

I express my sincere gratitude to my academic guide, **Md Imam Khader Shariff, Assistant Professor**, for his guidance and mentorship throughout the semester, and to the engineering leadership at **ApexPlanet Software Pvt. Ltd.** for providing a rigorous and hands-on industrial learning platform.
