import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the raw sales dataset
df = pd.read_csv("DATA/raw_sales_data.csv")

print("=" * 60)
print("SALES DATA ANALYSIS")
print("=" * 60)

# 1. Display first 5 rows
print("\nFIRST 5 ROWS:")
print(df.head())

# 2. Dataset dimensions
print("\nDATASET SHAPE:")
print(df.shape)

# 3. Column names
print("\nCOLUMN NAMES:")
print(df.columns.tolist())

# 4. Data types
print("\nDATA TYPES:")
print(df.dtypes)

# 5. Missing values
print("\nMISSING VALUES:")
print(df.isnull().sum())

# 6. Duplicate records
print("\nDUPLICATE RECORDS:")
print(df.duplicated().sum())

print("\n" + "=" * 60)
print("ANALYSIS COMPLETED")
print("=" * 60)