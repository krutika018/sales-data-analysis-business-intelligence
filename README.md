# 📊 Sales Data Analysis & Business Intelligence Dashboard

## 📌 Project Overview

An end-to-end **Sales Data Analysis and Business Intelligence project** that transforms raw sales data into meaningful business insights using **Python, SQL Server, and Power BI**.

The project analyzes revenue, profit, products, categories, regions, cities, payment modes, and monthly sales trends through an interactive dashboard.

---

## 🎯 Objectives

* Clean and preprocess raw sales data
* Identify missing and duplicate records
* Analyze revenue and profitability
* Identify top-performing products and categories
* Analyze regional and city-wise sales
* Track monthly sales trends
* Calculate key business KPIs
* Build an interactive Power BI dashboard

---

## 🔄 Workflow

```text
Raw Sales Data
      ↓
Data Cleaning & Preprocessing
      ↓
Exploratory Data Analysis
      ↓
SQL Server Analysis
      ↓
Power BI Dashboard
      ↓
Business Insights
```

---

## 🛠️ Technologies Used

* **Python**
* **Pandas & NumPy**
* **Matplotlib & Seaborn**
* **SQL & Microsoft SQL Server**
* **Power BI & DAX**
* **PyODBC**
* **Git & GitHub**

---

## 📂 Project Structure

```text
sales-data-analysis-business-intelligence/
│
├── DATA/
│   ├── raw_sales_data.csv
│   └── cleaned_sales_data.csv
│
├── IMAGES/
│   ├── revenue_by_category.png
│   ├── revenue_by_region.png
│   ├── top_10_products.png
│   └── monthly_revenue_trend.png
│
├── POWER BI/
│   └── Sales_Data_Analysis_Dashboard.pbix
│
├── PYTHON/
│   ├── generate_dataset.py
│   ├── data_cleaning.py
│   ├── eda_analysis.py
│   ├── sales_analysis.py
│   ├── import_to_sql.py
│   └── sales_analysis.ipynb
│
└── SQL/
    ├── sales_queries.sql
    └── SQLQuery1.sql
```

---

## 🐍 Data Processing

A synthetic dataset containing **10,200 raw records** was generated with duplicate and missing values to simulate real-world data-quality issues.

Using Pandas, the data was cleaned by:

* Handling missing values
* Removing duplicates
* Validating data types
* Creating calculated fields
* Calculating revenue, profit, and profit margin

Final dataset: **10,000 records and 16 columns**.

---

## 🗄️ SQL Server Analysis

The cleaned dataset was imported into a SQL Server database:

**Database:** `sales_analysis`
**Table:** `sales`

SQL was used to analyze:

* Revenue and profit
* Category and regional performance
* Top products and cities
* Monthly sales
* Payment modes
* Business KPIs
* Profit margins

---

## 📊 Power BI Dashboard

The interactive dashboard provides:

### Key KPIs

| KPI                 |    Value |
| ------------------- | -------: |
| Total Revenue       | ₹340.31M |
| Total Profit        | ₹111.05M |
| Total Orders        |      10K |
| Total Quantity      |      40K |
| Average Order Value |  ₹34.03K |
| Profit Margin       |   32.63% |

### Dashboard Visuals

* Revenue & Profit by Category
* Revenue & Profit by Region
* Top Products
* City-wise Performance
* Monthly Revenue Trend
* Payment Mode Distribution

### Filters

**Region | Year | Category | Product**

---

## 💡 Key Insights

* Total revenue: **₹340.31M**
* Total profit: **₹111.05M**
* Overall profit margin: **32.63%**
* **Electronics** generated the highest category revenue
* **Laptop** generated the highest product revenue

---

## 🚀 Future Enhancements

* Sales forecasting
* Demand forecasting
* Customer segmentation
* Customer Lifetime Value analysis
* Automated data refresh
* Advanced DAX measures
* Machine learning-based prediction
* Cloud database integration

---

## 📚 Skills Demonstrated

**Python | Pandas | NumPy | SQL | SQL Server | Power BI | DAX | Data Cleaning | EDA | Data Visualization | Business Intelligence | KPI Analysis**

---

