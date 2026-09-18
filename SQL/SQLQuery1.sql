CREATE DATABASE sales_analysis;
USE sales_analysis;

USE sales_analysis;

CREATE TABLE sales (
    Order_ID VARCHAR(20),
    Order_Date DATE,
    Customer_ID VARCHAR(20),
    Product VARCHAR(100),
    Category VARCHAR(50),
    Region VARCHAR(30),
    City VARCHAR(50),
    Quantity INT,
    Unit_Price DECIMAL(12,2),
    Discount_Pct DECIMAL(5,2),
    Discount_Amount DECIMAL(12,2),
    Revenue DECIMAL(14,2),
    Cost DECIMAL(14,2),
    Profit DECIMAL(14,2),
    Payment_Mode VARCHAR(30),
    Profit_Margin DECIMAL(8,2)
);

SELECT TABLE_NAME
FROM INFORMATION_SCHEMA.TABLES
WHERE TABLE_TYPE = 'BASE TABLE';

SELECT 
    COLUMN_NAME,
    DATA_TYPE
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_NAME = 'sales'
ORDER BY ORDINAL_POSITION;

USE sales_analysis;

SELECT COUNT(*) AS Total_Records
FROM sales;

SELECT
    SUM(Revenue) AS Total_Revenue
FROM sales;

SELECT
    SUM(Profit) AS Total_Profit
FROM sales;

SELECT
    Category,
    SUM(Revenue) AS Total_Revenue
FROM sales
GROUP BY Category
ORDER BY Total_Revenue DESC;

SELECT
    Category,
    SUM(Profit) AS Total_Profit
FROM sales
GROUP BY Category
ORDER BY Total_Profit DESC;

SELECT
    Region,
    SUM(Revenue) AS Total_Revenue
FROM sales
GROUP BY Region
ORDER BY Total_Revenue DESC;

SELECT
    Region,
    SUM(Profit) AS Total_Profit
FROM sales
GROUP BY Region
ORDER BY Total_Profit DESC;

SELECT
    Product,
    SUM(Revenue) AS Total_Revenue
FROM sales
GROUP BY Product
ORDER BY Total_Revenue DESC
OFFSET 0 ROWS
FETCH NEXT 10 ROWS ONLY;

SELECT
    YEAR(Order_Date) AS Sales_Year,
    MONTH(Order_Date) AS Sales_Month,
    SUM(Revenue) AS Total_Revenue
FROM sales
GROUP BY
    YEAR(Order_Date),
    MONTH(Order_Date)
ORDER BY
    Sales_Year,
    Sales_Month;

SELECT
    Payment_Mode,
    COUNT(*) AS Number_of_Orders,
    SUM(Revenue) AS Total_Revenue
FROM sales
GROUP BY Payment_Mode
ORDER BY Total_Revenue DESC;

SELECT
    City,
    SUM(Revenue) AS Total_Revenue
FROM sales
GROUP BY City
ORDER BY Total_Revenue DESC
OFFSET 0 ROWS
FETCH NEXT 10 ROWS ONLY;

SELECT
    YEAR(Order_Date) AS Sales_Year,
    MONTH(Order_Date) AS Sales_Month,
    SUM(Profit) AS Total_Profit
FROM sales
GROUP BY
    YEAR(Order_Date),
    MONTH(Order_Date)
ORDER BY
    Sales_Year,
    Sales_Month;


SELECT
    COUNT(DISTINCT Order_ID) AS Total_Orders,
    SUM(Revenue) AS Total_Revenue,
    SUM(Revenue) / COUNT(DISTINCT Order_ID) AS Average_Order_Value
FROM sales;


SELECT
    Category,
    SUM(Revenue) AS Total_Revenue,
    SUM(Profit) AS Total_Profit,
    (SUM(Profit) / NULLIF(SUM(Revenue), 0)) * 100 AS Profit_Margin_Percentage
FROM sales
GROUP BY Category
ORDER BY Profit_Margin_Percentage DESC;


USE sales_analysis;

SELECT TOP 10
    Product,
    SUM(Profit) AS Total_Profit
FROM sales
GROUP BY Product
ORDER BY Total_Profit DESC;


USE sales_analysis;

SELECT TOP 10
    City,
    SUM(Revenue) AS Total_Revenue
FROM sales
GROUP BY City
ORDER BY Total_Revenue DESC;


SELECT TOP 10
    City,
    SUM(Profit) AS Total_Profit
FROM sales
GROUP BY City
ORDER BY Total_Profit DESC;



SELECT
    Payment_Mode,
    COUNT(*) AS Number_of_Orders,
    SUM(Revenue) AS Total_Revenue
FROM sales
GROUP BY Payment_Mode
ORDER BY Total_Revenue DESC;


SELECT
    YEAR(Order_Date) AS Sales_Year,
    MONTH(Order_Date) AS Sales_Month,
    SUM(Revenue) AS Total_Revenue,
    SUM(Profit) AS Total_Profit
FROM sales
GROUP BY
    YEAR(Order_Date),
    MONTH(Order_Date)
ORDER BY
    Sales_Year,
    Sales_Month;



SELECT
    COUNT(DISTINCT Order_ID) AS Total_Orders,
    SUM(Quantity) AS Total_Quantity,
    SUM(Revenue) AS Total_Revenue,
    SUM(Profit) AS Total_Profit,
    (SUM(Profit) / NULLIF(SUM(Revenue), 0)) * 100 AS Profit_Margin_Percentage,
    SUM(Revenue) / NULLIF(COUNT(DISTINCT Order_ID), 0) AS Average_Order_Value
FROM sales;