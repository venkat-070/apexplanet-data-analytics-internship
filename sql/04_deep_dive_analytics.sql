-- ==============================================================================
-- 04_deep_dive_analytics.sql
-- Advanced Analytical SQL: Window Functions, CTEs, MoM Growth & Pareto
-- ApexPlanet Data Analytics Internship | Venkata Vedhadri Marisetti (23981A44Y9)
-- ==============================================================================

-- 1. Month-over-Month (MoM) Revenue Growth with LAG() Window Function
WITH MonthlyRevenue AS (
    SELECT 
        Order_Year_Month,
        ROUND(SUM(Sales), 2) AS Monthly_Sales,
        ROUND(SUM(Profit), 2) AS Monthly_Profit,
        COUNT(DISTINCT Order_ID) AS Monthly_Orders
    FROM orders
    GROUP BY Order_Year_Month
)
SELECT 
    Order_Year_Month,
    Monthly_Sales,
    LAG(Monthly_Sales, 1) OVER (ORDER BY Order_Year_Month) AS Prev_Month_Sales,
    ROUND(
        ((Monthly_Sales - LAG(Monthly_Sales, 1) OVER (ORDER BY Order_Year_Month)) / 
        LAG(Monthly_Sales, 1) OVER (ORDER BY Order_Year_Month)) * 100, 
        2
    ) AS MoM_Growth_Pct,
    ROUND(SUM(Monthly_Sales) OVER (ORDER BY Order_Year_Month), 2) AS Cumulative_Running_Revenue
FROM MonthlyRevenue;

-- 2. Top 5 Products by Revenue per Category using DENSE_RANK()
WITH RankedProducts AS (
    SELECT 
        Category,
        Product_Name,
        ROUND(SUM(Sales), 2) AS Product_Revenue,
        ROUND(SUM(Profit), 2) AS Product_Profit,
        DENSE_RANK() OVER (PARTITION BY Category ORDER BY SUM(Sales) DESC) AS Revenue_Rank
    FROM orders
    GROUP BY Category, Product_Name
)
SELECT 
    Category,
    Revenue_Rank,
    Product_Name,
    Product_Revenue,
    Product_Profit
FROM RankedProducts
WHERE Revenue_Rank <= 5
ORDER BY Category, Revenue_Rank;

-- 3. Pareto Analysis (80/20 Rule) on Sub-Categories
WITH SubCatTotals AS (
    SELECT 
        Sub_Category,
        ROUND(SUM(Sales), 2) AS SubCat_Sales,
        ROUND(SUM(Profit), 2) AS SubCat_Profit
    FROM orders
    GROUP BY Sub_Category
),
CumulativeShare AS (
    SELECT 
        Sub_Category,
        SubCat_Sales,
        SubCat_Profit,
        ROUND(SUM(SubCat_Sales) OVER (ORDER BY SubCat_Sales DESC) / SUM(SubCat_Sales) OVER () * 100, 2) AS Cumulative_Sales_Pct
    FROM SubCatTotals
)
SELECT 
    Sub_Category,
    SubCat_Sales,
    SubCat_Profit,
    Cumulative_Sales_Pct,
    CASE 
        WHEN Cumulative_Sales_Pct <= 80.0 THEN 'Core 80% Driver (A)'
        ELSE 'Long-Tail 20% (B/C)'
    END AS Pareto_Classification
FROM CumulativeShare
ORDER BY SubCat_Sales DESC;

-- 4. Discount Impact Analysis on Margin & Profit Erosion
SELECT 
    Discount_Tier,
    COUNT(*) AS Total_Orders,
    ROUND(AVG(Discount) * 100, 1) AS Avg_Discount_Pct,
    ROUND(SUM(Sales), 2) AS Total_Sales,
    ROUND(SUM(Profit), 2) AS Total_Profit,
    ROUND(AVG(Profit_Margin_Pct), 2) AS Avg_Profit_Margin_Pct
FROM orders
GROUP BY Discount_Tier
ORDER BY Avg_Discount_Pct ASC;
