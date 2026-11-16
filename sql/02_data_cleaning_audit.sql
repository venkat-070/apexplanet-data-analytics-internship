-- ==============================================================================
-- 02_data_cleaning_audit.sql
-- Data Integrity and Anomaly Detection Audits
-- ApexPlanet Data Analytics Internship | Venkata Vedhadri Marisetti (23981A44Y9)
-- ==============================================================================

-- 1. Check for missing values in core attributes
SELECT 
    COUNT(*) AS total_rows,
    SUM(CASE WHEN Order_ID IS NULL THEN 1 ELSE 0 END) AS missing_order_ids,
    SUM(CASE WHEN Customer_ID IS NULL THEN 1 ELSE 0 END) AS missing_customer_ids,
    SUM(CASE WHEN Sales IS NULL OR Sales <= 0 THEN 1 ELSE 0 END) AS invalid_sales,
    SUM(CASE WHEN Quantity IS NULL OR Quantity <= 0 THEN 1 ELSE 0 END) AS invalid_quantity,
    SUM(CASE WHEN Lead_Time_Days < 0 THEN 1 ELSE 0 END) AS negative_lead_time
FROM orders;

-- 2. Check for duplicate order IDs
SELECT 
    Order_ID, 
    COUNT(*) as frequency
FROM orders
GROUP BY Order_ID
HAVING COUNT(*) > 1;

-- 3. Audit distribution of categorical dimensions
SELECT Segment, COUNT(*) AS order_count, ROUND(AVG(Sales), 2) AS avg_sales
FROM orders
GROUP BY Segment
ORDER BY order_count DESC;

SELECT Region, COUNT(*) AS order_count, ROUND(SUM(Sales), 2) AS total_sales, ROUND(SUM(Profit), 2) AS total_profit
FROM orders
GROUP BY Region
ORDER BY total_sales DESC;
