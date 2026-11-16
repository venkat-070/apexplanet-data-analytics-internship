-- ==============================================================================
-- 03_business_kpis.sql
-- Executive Business Intelligence KPIs & Aggregations
-- ApexPlanet Data Analytics Internship | Venkata Vedhadri Marisetti (23981A44Y9)
-- ==============================================================================

-- 1. Global Executive Performance Scorecard
SELECT 
    COUNT(DISTINCT Order_ID) AS Total_Orders,
    COUNT(DISTINCT Customer_ID) AS Total_Customers,
    ROUND(SUM(Sales), 2) AS Total_Revenue,
    ROUND(SUM(Profit), 2) AS Total_Profit,
    ROUND((SUM(Profit) / SUM(Sales)) * 100, 2) AS Overall_Profit_Margin_Pct,
    ROUND(SUM(Sales) / COUNT(DISTINCT Order_ID), 2) AS Average_Order_Value,
    ROUND(AVG(Lead_Time_Days), 2) AS Avg_Shipping_Lead_Days,
    ROUND(SUM(CASE WHEN Returned = 'Yes' THEN 1.0 ELSE 0.0 END) / COUNT(*) * 100, 2) AS Return_Rate_Pct
FROM orders;

-- 2. Category Level Financial Breakdown
SELECT 
    Category,
    COUNT(DISTINCT Order_ID) AS Orders,
    SUM(Quantity) AS Total_Units_Sold,
    ROUND(SUM(Sales), 2) AS Total_Revenue,
    ROUND(SUM(Profit), 2) AS Total_Profit,
    ROUND((SUM(Profit) / SUM(Sales)) * 100, 2) AS Margin_Pct,
    ROUND(AVG(Discount) * 100, 2) AS Avg_Discount_Pct
FROM orders
GROUP BY Category
ORDER BY Total_Revenue DESC;

-- 3. Regional Profitability and Performance
SELECT 
    Region,
    COUNT(DISTINCT Order_ID) AS Total_Orders,
    ROUND(SUM(Sales), 2) AS Revenue,
    ROUND(SUM(Profit), 2) AS Profit,
    ROUND((SUM(Profit) / SUM(Sales)) * 100, 2) AS Profit_Margin_Pct
FROM orders
GROUP BY Region
ORDER BY Profit DESC;

-- 4. Customer Segment Contribution
SELECT 
    Segment,
    COUNT(DISTINCT Customer_ID) AS Customer_Count,
    COUNT(DISTINCT Order_ID) AS Order_Count,
    ROUND(SUM(Sales), 2) AS Segment_Revenue,
    ROUND(SUM(Profit), 2) AS Segment_Profit,
    ROUND(SUM(Sales) / COUNT(DISTINCT Order_ID), 2) AS Segment_AOV
FROM orders
GROUP BY Segment
ORDER BY Segment_Revenue DESC;
