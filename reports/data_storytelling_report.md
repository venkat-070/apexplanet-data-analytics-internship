# Task 4: Enterprise Data Storytelling Report
**Title:** Optimizing Profit Margins & Omnichannel Strategy Through Data Analytics  
**Author:** Venkata Vedhadri Marisetti (23981A44Y9)  
**Organization:** ApexPlanet Software Pvt. Ltd. | Data Analytics Internship  
**Faculty Guide:** Md Imam Khader Shariff, Assistant Professor | Raghu Engineering College  

---

```
  +-------------+      +--------------+      +----------------+      +--------------+      +--------------------+
  | 1. PROBLEM  | ---> | 2. ANALYSIS  | ---> | 3. DISCOVERY   | ---> | 4. EVIDENCE  | ---> | 5. RECOMMENDATION  |
  | Volume Trap |      | 5,500 Orders |      | Margin Erosion |      | Stats & BI   |      | Margin Governance  |
  +-------------+      +--------------+      +----------------+      +--------------+      +--------------------+
```

### 1. The Business Problem: The "Gross Volume Illusion"
ApexPlanet's omnichannel retail enterprise achieved rapid gross topline growth ($3.19M total sales). However, despite rising order volumes, quarterly operating profit margins experienced unpredictable dips. Senior leadership sought answers to two fundamental questions:
1. *Are aggressive customer discounts actually generating incremental net profit, or are they eroding profitability?*
2. *Which product categories and customer cohorts truly fuel bottom-line financial health?*

---

### 2. The Analytical Workflow
To establish empirical clarity, an end-to-end data pipeline was executed:
1. **Data Cleaning & Wrangling:** Cleansed 5,580 raw records, removed duplicate transactions, imputed missing postal codes and shipping fees, and engineered profit margins.
2. **Exploratory Data Analysis (EDA):** Evaluated parametric and non-parametric distributions, correlation matrices, and sub-category Pareto curves.
3. **Advanced SQL Engine:** Executed windowed CTEs, MoM growth calculations, and quintile RFM customer scoring in SQLite.
4. **Statistical Hypothesis Testing:** Conducted Welch's two-sample t-tests, one-way ANOVA, and Chi-square independence tests at $\alpha = 0.05$.

---

### 3. Core Insights & Empirical Discoveries
1. **The Discount Danger Zone:** 
   - Statistical hypothesis testing definitively rejected the null hypothesis ($p = 3.31e-88$, Welch's $t = 20.28$).
   - Orders with discounts exceeding 10% earned an average profit of only **$63.95**, compared to **$211.11** for low/no discount orders.
   - Transactions discounted at >20% resulted in net negative profit margins due to fulfillment overhead.
2. **Technology as the Growth Engine:**
   - Technology drove $2.17M (67.9%) of total gross sales with a strong 28.3% margin.
   - In contrast, Furniture exhibited the highest vulnerability to discount degradation.
3. **Customer Cohort Concentration:**
   - RFM segmentation classified 450 accounts into actionable lifecycle stages (Champions, Loyal, Recent Potential, At Risk, Hibernating).
   - The top 20% "Champion" and "Loyal" accounts generated over 54% of lifetime net operating profit.

---

### 4. Visual Evidence
- **Visual 04 (Pareto Analysis):** Demonstrates that 6 sub-categories (Chairs, Copiers, Phones, Bookcases, Machines, Storage) drive 72% of total enterprise volume.
- **Visual 07 (RFM Segmentation):** Reveals clear separation between high-frequency enterprise buyers and low-recency churn risks.
- **Visual 08 (Discount Decay):** Visualizes the steep drop in profit margins as discount rates scale past 15%.
- **Visual 09 (Statistical Validation):** Illustrates the statistically significant separation in net profits between discount cohorts.

---

### 5. Actionable Strategic Recommendations
1. **Implement Dynamic Discount Caps:** Institute an executive lock preventing frontline discounts greater than **15%** without regional VP approval.
2. **Double Down on Technology Bundling:** Prioritize high-margin Technology categories (Copiers, Phones, Accessories) with complementary Office Supplies to lift Average Order Value (AOV).
3. **Retention Over Acquisition:** Launch automated VIP retention and proactive win-back workflows targeting "At Risk" accounts before they transition to "Hibernating".
4. **Fulfillment Route Optimization:** Standardize carrier selection across regional hubs to sustain the 3.5-day fulfillment lead time while reducing parcel logistics expenditure.
