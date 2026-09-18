import pandas as pd
import numpy as np
from pathlib import Path

# -----------------------------
# 1. Settings
# -----------------------------

np.random.seed(42)

num_records = 10000

# Find the project folder automatically
project_folder = Path(__file__).resolve().parent.parent
data_folder = project_folder / "DATA"

# Create DATA folder if it doesn't exist
data_folder.mkdir(exist_ok=True)

# -----------------------------
# 2. Product information
# -----------------------------

products = {
    "Electronics": [
        ("Laptop", 55000),
        ("Smartphone", 25000),
        ("Tablet", 18000),
        ("Headphones", 2500),
        ("Smart Watch", 6000)
    ],
    "Furniture": [
        ("Office Chair", 8500),
        ("Desk", 12000),
        ("Bookshelf", 7000),
        ("Sofa", 25000),
        ("Dining Table", 22000)
    ],
    "Clothing": [
        ("T-Shirt", 800),
        ("Jeans", 1800),
        ("Jacket", 3500),
        ("Sneakers", 3000),
        ("Hoodie", 2200)
    ],
    "Home Appliances": [
        ("Mixer Grinder", 4500),
        ("Microwave", 9000),
        ("Air Fryer", 7000),
        ("Vacuum Cleaner", 8500),
        ("Electric Kettle", 1800)
    ],
    "Accessories": [
        ("Backpack", 1800),
        ("Wallet", 1200),
        ("Belt", 900),
        ("Sunglasses", 1500),
        ("Phone Case", 600)
    ]
}

# -----------------------------
# 3. Regions and cities
# -----------------------------

region_cities = {
    "South": ["Bangalore", "Chennai", "Hyderabad", "Kochi"],
    "West": ["Mumbai", "Pune", "Ahmedabad", "Goa"],
    "North": ["Delhi", "Jaipur", "Lucknow", "Chandigarh"],
    "East": ["Kolkata", "Bhubaneswar", "Patna", "Guwahati"]
}

regions = list(region_cities.keys())

# -----------------------------
# 4. Generate basic data
# -----------------------------

data = []

for i in range(num_records):

    category = np.random.choice(
        list(products.keys())
    )

    product, unit_price = products[category][
        np.random.randint(len(products[category]))
    ]

    region = np.random.choice(regions)

    city = np.random.choice(
        region_cities[region]
    )

    quantity = np.random.randint(1, 8)

    discount_pct = np.random.choice(
        [0, 5, 10, 15, 20],
        p=[0.20, 0.30, 0.30, 0.15, 0.05]
    )

    order_date = pd.Timestamp(
        np.random.choice(
            pd.date_range(
                start="2024-01-01",
                end="2025-12-31"
            )
        )
    )

    customer_id = f"CUST{np.random.randint(1000, 3000)}"

    payment_mode = np.random.choice(
        ["Credit Card", "Debit Card", "UPI", "Cash", "Net Banking"]
    )

    # -----------------------------
    # 5. Financial calculations
    # -----------------------------

    gross_sales = quantity * unit_price

    discount_amount = (
        gross_sales * discount_pct / 100
    )

    revenue = gross_sales - discount_amount

    # Cost is between 55% and 80% of revenue
    cost_percentage = np.random.uniform(
        0.55, 0.80
    )

    cost = revenue * cost_percentage

    profit = revenue - cost

    data.append([
        f"ORD{i + 1:05d}",
        order_date,
        customer_id,
        product,
        category,
        region,
        city,
        quantity,
        unit_price,
        discount_pct,
        discount_amount,
        revenue,
        cost,
        profit,
        payment_mode
    ])

# -----------------------------
# 6. Create DataFrame
# -----------------------------

columns = [
    "Order_ID",
    "Order_Date",
    "Customer_ID",
    "Product",
    "Category",
    "Region",
    "City",
    "Quantity",
    "Unit_Price",
    "Discount_Pct",
    "Discount_Amount",
    "Revenue",
    "Cost",
    "Profit",
    "Payment_Mode"
]

df = pd.DataFrame(
    data,
    columns=columns
)

# -----------------------------
# 7. Add a few missing values
#    for our data-cleaning step
# -----------------------------

missing_discount = np.random.choice(
    df.index,
    size=100,
    replace=False
)

df.loc[
    missing_discount,
    "Discount_Pct"
] = np.nan

missing_payment = np.random.choice(
    df.index,
    size=50,
    replace=False
)

df.loc[
    missing_payment,
    "Payment_Mode"
] = np.nan

# -----------------------------
# 8. Add duplicate records
#    for our cleaning step
# -----------------------------

duplicates = df.sample(
    200,
    random_state=42
)

df = pd.concat(
    [df, duplicates],
    ignore_index=True
)

# -----------------------------
# 9. Shuffle the dataset
# -----------------------------

df = df.sample(
    frac=1,
    random_state=42
).reset_index(drop=True)

# -----------------------------
# 10. Save raw dataset
# -----------------------------

output_file = (
    data_folder / "raw_sales_data.csv"
)

df.to_csv(
    output_file,
    index=False
)

# -----------------------------
# 11. Display results
# -----------------------------

print("=" * 60)
print("SALES DATASET CREATED SUCCESSFULLY")
print("=" * 60)

print(f"Rows generated: {len(df)}")
print(f"Columns: {len(df.columns)}")
print(f"File saved at: {output_file}")

print("\nFirst 5 records:")
print(df.head())

print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate rows:")
print(df.duplicated().sum())

print("=" * 60)