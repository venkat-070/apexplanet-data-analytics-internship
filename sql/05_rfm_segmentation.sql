-- ==============================================================================
-- 05_rfm_segmentation.sql
-- Customer RFM (Recency, Frequency, Monetary) Segmentation
-- ApexPlanet Data Analytics Internship | Venkata Vedhadri Marisetti (23981A44Y9)
-- ==============================================================================

WITH ReferenceDate AS (
    SELECT MAX(Order_Date_Str) AS max_date FROM orders
),
CustomerAggregates AS (
    SELECT 
        o.Customer_ID,
        o.Customer_Name,
        o.Segment,
        ROUND(JULIANDAY(r.max_date) - JULIANDAY(MAX(o.Order_Date_Str))) AS Recency_Days,
        COUNT(DISTINCT o.Order_ID) AS Frequency,
        ROUND(SUM(o.Sales), 2) AS Monetary
    FROM orders o
    CROSS JOIN ReferenceDate r
    GROUP BY o.Customer_ID, o.Customer_Name, o.Segment
),
RFMScores AS (
    SELECT 
        Customer_ID,
        Customer_Name,
        Segment,
        Recency_Days,
        Frequency,
        Monetary,
        NTILE(5) OVER (ORDER BY Recency_Days DESC) AS R_Score,  -- Higher score = more recent
        NTILE(5) OVER (ORDER BY Frequency ASC) AS F_Score,     -- Higher score = more frequent
        NTILE(5) OVER (ORDER BY Monetary ASC) AS M_Score       -- Higher score = higher spend
    FROM CustomerAggregates
)
SELECT 
    Customer_ID,
    Customer_Name,
    Segment,
    Recency_Days,
    Frequency,
    Monetary,
    R_Score,
    F_Score,
    M_Score,
    (R_Score + F_Score + M_Score) AS RFM_Total,
    CASE 
        WHEN R_Score >= 4 AND F_Score >= 4 AND M_Score >= 4 THEN 'Champions'
        WHEN R_Score >= 3 AND F_Score >= 3 THEN 'Loyal Customers'
        WHEN R_Score >= 4 AND F_Score < 3 THEN 'Recent Potential'
        WHEN R_Score < 2 AND F_Score >= 3 THEN 'At Risk / Need Attention'
        WHEN R_Score < 2 AND F_Score < 2 THEN 'Hibernating / Lost'
        ELSE 'Promising / Growth'
    END AS RFM_Segment
FROM RFMScores
ORDER BY Monetary DESC;
