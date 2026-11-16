# Task 1: Data Immersion & Quality Audit Report
**Intern:** Venkata Vedhadri Marisetti (23981A44Y9)  
**Organization:** ApexPlanet Software Pvt. Ltd.  
**Project:** Global Omnichannel Superstore Analytics  
**Status:** Completed & Validated  

---

## 1. Initial Data Assessment
* **Raw Dataset Dimensions:** 5,580 rows, 24 columns
* **Duplicate Records Detected:** 66 duplicate rows (successfully eliminated)
* **Pre-cleaning Missing Values:**
  - **Customer_Name**: 114 missing (2.04%)
  - **Postal_Code**: 160 missing (2.87%)
  - **Discount**: 75 missing (1.34%)
  - **Shipping_Cost**: 144 missing (2.58%)

## 2. Wrangling & Cleaning Pipeline Executed
1. **Deduplication:** Dropped 66 redundant records maintaining primary transaction integrity.
2. **Type Casting & Normalization:** Stripped currency formatting (`$`, `,`) in `Sales`; parsed mixed date strings (`%Y-%m-%d`, `%d/%m/%Y`, `%m-%d-%Y`) into unified ISO-8601 timestamps.
3. **Imputation:**
   - `Customer_Name`: Deterministically resolved via `Customer_ID` dimension mapping.
   - `Postal_Code`: Regionally imputed using modal mapping across `Country` and `City`.
   - `Discount`: Unfilled entries imputed with default `0.0`.
   - `Shipping_Cost`: Contextually imputed via stratified median grouped by `Ship_Mode` and `Quantity`.
4. **Derived Dimensions & Feature Engineering:**
   - `Lead_Time_Days` (`Ship_Date - Order_Date`)
   - `Unit_Price`, `Total_Cost`, `Profit_Margin_Pct`
   - `Discount_Tier` (None, Low, Moderate, Aggressive)
   - Calendar hierarchies: `Order_Year`, `Order_Month`, `Order_Quarter`, `Order_Day_Name`.
5. **Storage & Multi-Format Delivery:**
   - Clean CSV: `data/processed/clean_superstore_data.csv`
   - Enterprise Excel: `data/processed/clean_superstore_data.xlsx` (with Pivot tables)
   - Relational Database: `data/database/analytics.db` with indexed `orders`, `customers`, and `products` tables.

## 3. Post-Cleaning Data Health Matrix
* **Cleaned Record Count:** 5,514 records
* **Zero Missing Values:** 100% complete across all 32 transactional & analytical fields.
* **Schema Integrity:** Fully validated against primary/foreign key relationships.
