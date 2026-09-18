import pandas as pd

# -----------------------------------------
# 1. Load raw dataset
# -----------------------------------------

df = pd.read_csv("DATA/raw_sales_data.csv")

print("=" * 60)
print("DATA CLEANING")
print("=" * 60)

print("\nOriginal dataset shape:")
print(df.shape)


# -----------------------------------------
# 2. Check missing values
# -----------------------------------------

print("\nMissing values before cleaning:")
print(df.isnull().sum())


# -----------------------------------------
# 3. Remove duplicate records
# -----------------------------------------

duplicate_count = df.duplicated().sum()

print(f"\nDuplicate records found: {duplicate_count}")

df = df.drop_duplicates()

print(f"Rows after removing duplicates: {len(df)}")


# -----------------------------------------
# 4. Handle missing Discount_Pct
# -----------------------------------------

df["Discount_Pct"] = df["Discount_Pct"].fillna(0)


# -----------------------------------------
# 5. Handle missing Payment_Mode
# -----------------------------------------

df["Payment_Mode"] = df["Payment_Mode"].fillna("Unknown")


# -----------------------------------------
# 6. Convert Order_Date to datetime
# -----------------------------------------

df["Order_Date"] = pd.to_datetime(
    df["Order_Date"],
    errors="coerce"
)


# -----------------------------------------
# 7. Check for invalid dates
# -----------------------------------------

invalid_dates = df["Order_Date"].isnull().sum()

print(f"\nInvalid dates found: {invalid_dates}")


# -----------------------------------------
# 8. Create Profit Margin
# -----------------------------------------

df["Profit_Margin"] = (
    df["Profit"] / df["Revenue"]
) * 100


# -----------------------------------------
# 9. Round financial columns
# -----------------------------------------

financial_columns = [
    "Unit_Price",
    "Discount_Amount",
    "Revenue",
    "Cost",
    "Profit",
    "Profit_Margin"
]

for column in financial_columns:
    df[column] = df[column].round(2)


# -----------------------------------------
# 10. Check missing values after cleaning
# -----------------------------------------

print("\nMissing values after cleaning:")
print(df.isnull().sum())


# -----------------------------------------
# 11. Check duplicates after cleaning
# -----------------------------------------

print("\nDuplicate records after cleaning:")
print(df.duplicated().sum())


# -----------------------------------------
# 12. Final dataset information
# -----------------------------------------

print("\nFinal dataset shape:")
print(df.shape)


# -----------------------------------------
# 13. Save cleaned dataset
# -----------------------------------------

output_file = "DATA/cleaned_sales_data.csv"

df.to_csv(
    output_file,
    index=False
)

print("\nCleaned dataset saved successfully:")
print(output_file)

print("\n" + "=" * 60)
print("DATA CLEANING COMPLETED")
print("=" * 60)