import pandas as pd
import pyodbc

# -----------------------------------------
# 1. Load cleaned CSV
# -----------------------------------------

df = pd.read_csv("DATA/cleaned_sales_data.csv")

print(f"Rows loaded from CSV: {len(df)}")


# -----------------------------------------
# 2. Connect to SQL Server
# -----------------------------------------

connection = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost;"
    "DATABASE=sales_analysis;"
    "Trusted_Connection=yes;"
)

cursor = connection.cursor()

print("SQL Server connection successful!")


# -----------------------------------------
# 3. Insert data
# -----------------------------------------

insert_query = """
INSERT INTO sales (
    Order_ID,
    Order_Date,
    Customer_ID,
    Product,
    Category,
    Region,
    City,
    Quantity,
    Unit_Price,
    Discount_Pct,
    Discount_Amount,
    Revenue,
    Cost,
    Profit,
    Payment_Mode,
    Profit_Margin
)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
"""


# Replace NaN with None for SQL Server
df = df.where(pd.notnull(df), None)

data = [
    tuple(row)
    for row in df.itertuples(index=False, name=None)
]

cursor.fast_executemany = True
cursor.executemany(insert_query, data)

connection.commit()

print(f"Rows inserted into SQL Server: {len(data)}")


# -----------------------------------------
# 4. Close connection
# -----------------------------------------

cursor.close()
connection.close()

print("SQL Server connection closed.")
print("=" * 60)
print("DATA IMPORT COMPLETED SUCCESSFULLY")
print("=" * 60)