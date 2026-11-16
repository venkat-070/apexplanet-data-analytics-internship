"""
00_generate_dataset.py
Generates the raw enterprise Global Omnichannel Superstore dataset with realistic anomalies
for the ApexPlanet Data Analytics Internship project.
Student: Venkata Vedhadri Marisetti (23981A44Y9)
"""

import os
import random
import numpy as np
import pandas as pd
from datetime import datetime, timedelta

# Set deterministic seed
random.seed(42)
np.random.seed(42)

NUM_RECORDS = 5500

customer_first_names = [
    "Aarav", "Aditi", "Rohan", "Priya", "Rahul", "Sneha", "Vikram", "Ananya", "Karthik", "Divya",
    "Alexander", "Emily", "Michael", "Sophia", "James", "Emma", "William", "Olivia", "Daniel", "Mia",
    "David", "Isabella", "Lucas", "Ava", "Henry", "Charlotte", "Ethan", "Amelia", "Benjamin", "Harper"
]
customer_last_names = [
    "Sharma", "Patel", "Verma", "Rao", "Reddy", "Nair", "Iyer", "Mehta", "Singh", "Gupta",
    "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez",
    "Wilson", "Anderson", "Taylor", "Thomas", "Moore", "Jackson", "Martin", "Lee", "Perez", "Thompson"
]

customers = []
for i in range(450):
    cid = f"CUST-{1000 + i}"
    fn = random.choice(customer_first_names)
    ln = random.choice(customer_last_names)
    name = f"{fn} {ln}"
    seg = random.choices(["Consumer", "Corporate", "Home Office"], weights=[0.52, 0.30, 0.18])[0]
    customers.append((cid, name, seg))

catalog = [
    # Furniture
    ("FUR-BO-1001", "Furniture", "Bookcases", "Ergonomic Modular Oak Bookcase", 180.0, 260.0),
    ("FUR-CH-1002", "Furniture", "Chairs", "Executive High-Back Mesh Chair", 110.0, 190.0),
    ("FUR-TA-1003", "Furniture", "Tables", "Conference Training Folding Table", 220.0, 340.0),
    ("FUR-FU-1004", "Furniture", "Furnishings", "Anti-Glare LED Desk Lamp", 25.0, 48.0),
    # Technology
    ("TEC-PH-2001", "Technology", "Phones", "SmartPhone Pro 5G Enterprise Edition", 450.0, 680.0),
    ("TEC-AC-2002", "Technology", "Accessories", "Noise-Cancelling Wireless Headset", 65.0, 120.0),
    ("TEC-MA-2003", "Technology", "Machines", "Thermal Receipt & Barcode Printer", 280.0, 420.0),
    ("TEC-CO-2004", "Technology", "Copiers", "Multifunction Color Laser Copier/Scanner", 600.0, 950.0),
    # Office Supplies
    ("OFF-ST-3001", "Office Supplies", "Storage", "Heavy-Duty Stackable File Organizer", 35.0, 62.0),
    ("OFF-BI-3002", "Office Supplies", "Binders", "Heavy-Duty 3-Ring Presentation Binder", 8.0, 18.0),
    ("OFF-AP-3003", "Office Supplies", "Appliances", "Compact Energy-Star Breakroom Microwave", 95.0, 160.0),
    ("OFF-PA-3004", "Office Supplies", "Paper", "Premium Recycled Multipurpose Copy Paper", 14.0, 28.0),
    ("OFF-EN-3005", "Office Supplies", "Envelopes", "Security Tint Self-Seal Envelopes (Pack)", 10.0, 22.0),
    ("OFF-LA-3006", "Office Supplies", "Labels", "Self-Adhesive Address Shipping Labels", 6.0, 15.0),
    ("OFF-FA-3007", "Office Supplies", "Fasteners", "Magnetic Stainless Steel Paper Clips Box", 4.0, 9.5),
    ("OFF-SU-3008", "Office Supplies", "Supplies", "High-Precision Ergonomic Scissors Kit", 12.0, 24.0)
]

locations = [
    ("United States", "New York", "New York", "10001", "East"),
    ("United States", "California", "Los Angeles", "90001", "West"),
    ("United States", "Illinois", "Chicago", "60601", "Central"),
    ("United States", "Texas", "Houston", "77001", "Central"),
    ("United States", "Florida", "Miami", "33101", "South"),
    ("United States", "Washington", "Seattle", "98101", "West"),
    ("India", "Maharashtra", "Mumbai", "400001", "West"),
    ("India", "Karnataka", "Bengaluru", "560001", "South"),
    ("India", "Delhi", "New Delhi", "110001", "North"),
    ("India", "Telangana", "Hyderabad", "500001", "South"),
    ("India", "Tamil Nadu", "Chennai", "600001", "South"),
    ("United Kingdom", "England", "London", "EC1A", "East"),
    ("United Kingdom", "England", "Manchester", "M1", "North"),
    ("Germany", "Berlin", "Berlin", "10115", "Central"),
    ("Germany", "Bavaria", "Munich", "80331", "South"),
    ("Canada", "Ontario", "Toronto", "M5H", "East"),
    ("Canada", "British Columbia", "Vancouver", "V6B", "West"),
    ("Australia", "New South Wales", "Sydney", "2000", "East"),
    ("Australia", "Victoria", "Melbourne", "3000", "South"),
    ("Singapore", "Singapore", "Singapore", "018989", "East")
]

ship_modes = ["Standard Class", "Second Class", "First Class", "Same Day"]
ship_weights = [0.60, 0.20, 0.15, 0.05]

priorities = ["Critical", "High", "Medium", "Low"]
prio_weights = [0.10, 0.30, 0.45, 0.15]

start_date = datetime(2024, 1, 1)
end_date = datetime(2026, 8, 31)
date_range_days = (end_date - start_date).days

records = []

for i in range(1, NUM_RECORDS + 1):
    order_id = f"ORD-{2024 + random.randint(0, 2)}-{10000 + i}"
    cust = random.choice(customers)
    prod = random.choice(catalog)
    loc = random.choice(locations)
    
    order_dt = start_date + timedelta(days=random.randint(0, date_range_days))
    ship_delay = random.choices([1, 2, 3, 4, 5, 6, 7], weights=[0.05, 0.15, 0.35, 0.25, 0.10, 0.07, 0.03])[0]
    ship_dt = order_dt + timedelta(days=ship_delay)
    ship_mode = random.choices(ship_modes, weights=ship_weights)[0]
    prio = random.choices(priorities, weights=prio_weights)[0]
    
    qty = random.choices(range(1, 10), weights=[0.25, 0.25, 0.20, 0.12, 0.08, 0.04, 0.03, 0.02, 0.01])[0]
    
    # Discount policy: high discounts erode profit!
    discount = random.choices(
        [0.0, 0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.40, 0.50, 0.60],
        weights=[0.38, 0.15, 0.14, 0.10, 0.08, 0.05, 0.04, 0.03, 0.02, 0.01]
    )[0]
    
    unit_cost = prod[4]
    unit_base_price = prod[5]
    
    # Add slight random price fluctuation
    unit_price = round(unit_base_price * (1.0 + random.uniform(-0.05, 0.05)), 2)
    sales = round(qty * unit_price * (1.0 - discount), 2)
    
    # Base shipping cost
    shipping_cost = round(random.uniform(4.0, 22.0) + (qty * 1.5) + (10.0 if ship_mode == "Same Day" else 0.0), 2)
    
    # Profit calculation: Sales - (Total Cost) - Shipping Cost
    total_cost = qty * unit_cost
    profit = round(sales - total_cost - (shipping_cost * 0.4), 2)
    
    # Return rate ~ 4.5%
    returned = random.choices(["No", "Yes"], weights=[0.955, 0.045])[0]
    
    records.append({
        "Order_ID": order_id,
        "Order_Date": order_dt.strftime("%Y-%m-%d"),
        "Ship_Date": ship_dt.strftime("%Y-%m-%d"),
        "Ship_Mode": ship_mode,
        "Customer_ID": cust[0],
        "Customer_Name": cust[1],
        "Segment": cust[2],
        "Country": loc[0],
        "State": loc[1],
        "City": loc[2],
        "Postal_Code": loc[3],
        "Region": loc[4],
        "Product_ID": prod[0],
        "Category": prod[1],
        "Sub_Category": prod[2],
        "Product_Name": prod[3],
        "Cost_Price": unit_cost,
        "Sales": sales,
        "Quantity": qty,
        "Discount": discount,
        "Profit": profit,
        "Shipping_Cost": shipping_cost,
        "Order_Priority": prio,
        "Returned": returned
    })

df = pd.DataFrame(records)

# Introduce realistic real-world data imperfections for Task 1:
# 1. Duplicates (~80 rows duplicated)
duplicate_indices = random.sample(range(len(df)), 80)
df_dupes = df.iloc[duplicate_indices].copy()
df_raw = pd.concat([df, df_dupes], ignore_index=True)

# 2. Random missing values
for col, rate in [("Postal_Code", 0.03), ("Customer_Name", 0.02), ("Shipping_Cost", 0.025), ("Discount", 0.015)]:
    mask = np.random.rand(len(df_raw)) < rate
    df_raw.loc[mask, col] = np.nan

# 3. Inconsistent date formats in some Order_Date records
for idx in random.sample(range(len(df_raw)), 120):
    val = df_raw.loc[idx, "Order_Date"]
    if pd.notna(val):
        dt = datetime.strptime(str(val)[:10], "%Y-%m-%d")
        if random.random() < 0.5:
            df_raw.loc[idx, "Order_Date"] = dt.strftime("%d/%m/%Y")
        else:
            df_raw.loc[idx, "Order_Date"] = dt.strftime("%m-%d-%Y")

# 4. Inconsistent text casing / whitespaces
for idx in random.sample(range(len(df_raw)), 150):
    val = df_raw.loc[idx, "Segment"]
    if pd.notna(val):
        transforms = [val.upper(), val.lower(), f"  {val}  ", val.capitalize()]
        df_raw.loc[idx, "Segment"] = random.choice(transforms)

for idx in random.sample(range(len(df_raw)), 100):
    val = df_raw.loc[idx, "Category"]
    if pd.notna(val):
        df_raw.loc[idx, "Category"] = f" {val} " if random.random() < 0.5 else val.upper()

# 5. String formatting with currency symbols in Sales column for some rows
for idx in random.sample(range(len(df_raw)), 80):
    val = df_raw.loc[idx, "Sales"]
    if pd.notna(val):
        df_raw.loc[idx, "Sales"] = f"${val:,.2f}"

# Save raw dataset
output_dir = os.path.join(os.path.dirname(__file__), "..", "data", "raw")
os.makedirs(output_dir, exist_ok=True)
raw_csv_path = os.path.join(output_dir, "global_superstore_raw.csv")
df_raw.to_csv(raw_csv_path, index=False)

print(f"Dataset generated successfully at: {raw_csv_path}")
print(f"Total raw rows: {len(df_raw)}, columns: {len(df_raw.columns)}")
