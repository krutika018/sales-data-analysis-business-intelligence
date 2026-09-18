import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# -----------------------------------------
# 1. Load cleaned dataset
# -----------------------------------------

df = pd.read_csv("DATA/cleaned_sales_data.csv")

# Convert date column
df["Order_Date"] = pd.to_datetime(df["Order_Date"])

print("=" * 60)
print("EXPLORATORY DATA ANALYSIS")
print("=" * 60)


# -----------------------------------------
# 2. Basic Business Metrics
# -----------------------------------------

total_revenue = df["Revenue"].sum()
total_profit = df["Profit"].sum()
total_orders = df["Order_ID"].nunique()
total_quantity = df["Quantity"].sum()
average_order_value = total_revenue / total_orders
profit_margin = (total_profit / total_revenue) * 100

print("\nKEY BUSINESS METRICS")
print("-" * 40)

print(f"Total Revenue       : ₹{total_revenue:,.2f}")
print(f"Total Profit        : ₹{total_profit:,.2f}")
print(f"Total Orders        : {total_orders:,}")
print(f"Total Quantity Sold : {total_quantity:,}")
print(f"Average Order Value : ₹{average_order_value:,.2f}")
print(f"Profit Margin       : {profit_margin:.2f}%")


# -----------------------------------------
# 3. Revenue by Category
# -----------------------------------------

category_revenue = (
    df.groupby("Category")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)

print("\nREVENUE BY CATEGORY")
print("-" * 40)
print(category_revenue)


# -----------------------------------------
# 4. Profit by Category
# -----------------------------------------

category_profit = (
    df.groupby("Category")["Profit"]
    .sum()
    .sort_values(ascending=False)
)

print("\nPROFIT BY CATEGORY")
print("-" * 40)
print(category_profit)


# -----------------------------------------
# 5. Revenue by Region
# -----------------------------------------

region_revenue = (
    df.groupby("Region")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)

print("\nREVENUE BY REGION")
print("-" * 40)
print(region_revenue)


# -----------------------------------------
# 6. Profit by Region
# -----------------------------------------

region_profit = (
    df.groupby("Region")["Profit"]
    .sum()
    .sort_values(ascending=False)
)

print("\nPROFIT BY REGION")
print("-" * 40)
print(region_profit)


# -----------------------------------------
# 7. Top 10 Products by Revenue
# -----------------------------------------

top_products = (
    df.groupby("Product")["Revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTOP 10 PRODUCTS BY REVENUE")
print("-" * 40)
print(top_products)


# -----------------------------------------
# 8. Monthly Revenue
# -----------------------------------------

monthly_revenue = (
    df.groupby(
        df["Order_Date"].dt.to_period("M")
    )["Revenue"]
    .sum()
)

print("\nMONTHLY REVENUE")
print("-" * 40)
print(monthly_revenue)


# -----------------------------------------
# 9. Payment Method Analysis
# -----------------------------------------

payment_analysis = (
    df.groupby("Payment_Mode")
    .agg(
        Orders=("Order_ID", "nunique"),
        Revenue=("Revenue", "sum")
    )
    .sort_values("Orders", ascending=False)
)

print("\nPAYMENT METHOD ANALYSIS")
print("-" * 40)
print(payment_analysis)


# -----------------------------------------
# 10. City Performance
# -----------------------------------------

city_revenue = (
    df.groupby("City")["Revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTOP 10 CITIES BY REVENUE")
print("-" * 40)
print(city_revenue)


# -----------------------------------------
# 11. Create Images folder
# -----------------------------------------

images_folder = Path("IMAGES")
images_folder.mkdir(exist_ok=True)


# -----------------------------------------
# 12. Revenue by Category Chart
# -----------------------------------------

plt.figure(figsize=(10, 6))

category_revenue.plot(kind="bar")

plt.title("Revenue by Category")
plt.xlabel("Category")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(
    images_folder / "revenue_by_category.png",
    dpi=300
)

plt.show()
plt.close()


# -----------------------------------------
# 13. Revenue by Region Chart
# -----------------------------------------

plt.figure(figsize=(10, 6))

region_revenue.plot(kind="bar")

plt.title("Revenue by Region")
plt.xlabel("Region")
plt.ylabel("Revenue")
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig(
    images_folder / "revenue_by_region.png",
    dpi=300
)

plt.show()
plt.close()


# -----------------------------------------
# 14. Top Products Chart
# -----------------------------------------

plt.figure(figsize=(10, 6))

top_products.sort_values().plot(kind="barh")

plt.title("Top 10 Products by Revenue")
plt.xlabel("Revenue")
plt.ylabel("Product")
plt.tight_layout()

plt.savefig(
    images_folder / "top_10_products.png",
    dpi=300
)

plt.show()
plt.close()


# -----------------------------------------
# 15. Monthly Revenue Trend
# -----------------------------------------

plt.figure(figsize=(12, 6))

monthly_revenue.index = monthly_revenue.index.astype(str)

plt.plot(
    monthly_revenue.index,
    monthly_revenue.values,
    marker="o"
)

plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()

plt.savefig(
    images_folder / "monthly_revenue_trend.png",
    dpi=300
)

plt.show()
plt.close()


print("\n" + "=" * 60)
print("EDA COMPLETED SUCCESSFULLY")
print("=" * 60)