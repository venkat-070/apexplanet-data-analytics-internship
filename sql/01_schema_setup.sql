-- ==============================================================================
-- 01_schema_setup.sql
-- Database Schema Setup & Relational Staging
-- ApexPlanet Data Analytics Internship | Venkata Vedhadri Marisetti (23981A44Y9)
-- ==============================================================================

-- Core Orders Transaction Table
CREATE TABLE IF NOT EXISTS orders_staging (
    Order_ID TEXT PRIMARY KEY,
    Order_Date_Str TEXT,
    Ship_Date_Str TEXT,
    Ship_Mode TEXT,
    Customer_ID TEXT,
    Customer_Name TEXT,
    Segment TEXT,
    Country TEXT,
    State TEXT,
    City TEXT,
    Postal_Code TEXT,
    Region TEXT,
    Product_ID TEXT,
    Category TEXT,
    Sub_Category TEXT,
    Product_Name TEXT,
    Cost_Price REAL,
    Sales REAL,
    Quantity INTEGER,
    Discount REAL,
    Profit REAL,
    Shipping_Cost REAL,
    Order_Priority TEXT,
    Returned TEXT,
    Order_Year INTEGER,
    Order_Month INTEGER,
    Order_Quarter TEXT,
    Order_Day_Name TEXT,
    Lead_Time_Days INTEGER,
    Unit_Price REAL,
    Total_Cost REAL,
    Profit_Margin_Pct REAL,
    Discount_Tier TEXT
);

-- Indices for rapid analytical filtering
CREATE INDEX IF NOT EXISTS idx_staging_order_dt ON orders_staging(Order_Date_Str);
CREATE INDEX IF NOT EXISTS idx_staging_customer ON orders_staging(Customer_ID);
CREATE INDEX IF NOT EXISTS idx_staging_region ON orders_staging(Region);
CREATE INDEX IF NOT EXISTS idx_staging_category ON orders_staging(Category);
