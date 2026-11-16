# Task 2: Exploratory Data Analysis & SQL Analytics Verification
**Intern:** Venkata Vedhadri Marisetti (23981A44Y9)  
**Organization:** ApexPlanet Software Pvt. Ltd.  
**Academic Guide:** Md Imam Khader Shariff, Assistant Professor  

---

## 1. Descriptive Statistical Summary
Parametric (Mean, Std. Dev) and Non-Parametric (Median, IQR, Skewness) indicators:

| Attribute | Mean | Median | Std. Dev | IQR | Min | 25% | 75% | Max | Skewness |
|:---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| **Sales** | 578.68 | 180.17 | 966.45 | 612.5 | 4.63 | 50.98 | 663.48 | 8577.63 | 3.24 |
| **Profit** | 164.59 | 51.2 | 318.12 | 174.49 | -1767.1 | 13.77 | 188.26 | 3169.11 | 3.59 |
| **Quantity** | 2.96 | 3.0 | 1.87 | 2.0 | 1.0 | 2.0 | 4.0 | 9.0 | 1.11 |
| **Discount** | 0.1 | 0.05 | 0.13 | 0.15 | 0.0 | 0.0 | 0.15 | 0.6 | 1.65 |
| **Shipping_Cost** | 17.95 | 17.73 | 6.22 | 9.06 | 5.5 | 13.32 | 22.38 | 43.83 | 0.32 |
| **Lead_Time_Days** | 3.52 | 3.0 | 1.35 | 1.0 | 1.0 | 3.0 | 4.0 | 7.0 | 0.48 |
| **Profit_Margin_Pct** | 26.86 | 31.54 | 18.65 | 16.09 | -136.35 | 22.07 | 38.16 | 54.31 | -2.45 |

### Statistical Observations:
- **Sales Revenue:** Shows positive right-skew (3.24), demonstrating that majority orders fall in the moderate price bracket while high-value enterprise bundles drive long-tail revenue.
- **Profitability:** Demonstrates high variability with negative tails in heavily discounted transactions.
- **Lead Time:** Centered around ~4.0 days with standard deviation ~1.4 days, demonstrating operational consistency across distribution hubs.

---

## 2. Executive KPI Scorecard (SQL Query 03)
* **Total Transactions (Orders):** 5,500
* **Unique Enterprise Customers:** 450
* **Total Revenue:** $3,190,836.65
* **Total Net Profit:** $907,565.75
* **Overall Profit Margin:** 28.44%
* **Average Order Value (AOV):** $580.15

---

## 3. Product Category Performance
| Category | Orders | Total Revenue ($) | Total Profit ($) | Profit Margin (%) |
|:---|---:|---:|---:|---:|
| **Technology** | 1,457 | $2,166,544.59 | $612,891.91 | 28.29% |
| **Furniture** | 1,293 | $712,833.60 | $191,775.60 | 26.9% |
| **Office Supplies** | 2,750 | $311,458.46 | $102,898.24 | 33.04% |

---

## 4. Key EDA Discoveries
1. **Pareto Concentration:** The top 6 sub-categories account for over 72% of cumulative sales, confirming the Pareto 80/20 distribution principle in omnichannel merchandising.
2. **Correlation Findings:** Discount exhibits a negative correlation with net profit, signaling that promotional discounts beyond 20% severely cannibalize operating profit margins.
3. **Temporal Stability:** Sales exhibit strong quarterly surges in Q4 and mid-year enterprise procurement cycles.
