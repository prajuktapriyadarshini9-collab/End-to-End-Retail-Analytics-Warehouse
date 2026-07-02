# 🛒 End-to-End Retail Analytics Warehouse

<div align="center">

## Enterprise-Grade Retail Analytics & Business Intelligence Platform

**Built with Snowflake • dbt Core • Airbyte • SQL • Python • Power BI • GitHub**

Transforming raw retail transactions into an enterprise-ready analytics warehouse and interactive executive dashboards.

![Power BI](https://img.shields.io/badge/PowerBI-BI-F2C811?logo=powerbi&logoColor=black)
![Snowflake](https://img.shields.io/badge/Snowflake-Data_Warehouse-29B5E8?logo=snowflake)
![dbt](https://img.shields.io/badge/dbt-Transformation-FF694B?logo=dbt)
![SQL](https://img.shields.io/badge/SQL-Analytics-blue)
![Git](https://img.shields.io/badge/Git-Version_Control-red?logo=git)

</div>

---

# 📖 Project Overview

This project demonstrates a complete **end-to-end modern data engineering and business intelligence pipeline** built on the Brazilian Olist E-Commerce dataset. It follows industry-standard analytics engineering practices to transform raw transactional data into business-ready insights.

The pipeline covers every major stage of an analytics workflow:

- Data Collection
- Data Ingestion
- Data Warehousing
- Data Transformation
- Dimensional Modeling
- Business Analytics
- Executive Dashboards
- Documentation & Version Control

---

# 🎯 Business Problem

Retail organizations generate large volumes of transactional data that are difficult to analyze directly. Raw datasets often contain duplicates, missing values, inconsistent formats, and fragmented information.

This project addresses those challenges by building a scalable analytics warehouse that enables:
- Executive decision-making
- Marketing performance analysis
- Customer behavior analysis
- Logistics monitoring
- Revenue reporting

---

# 🎯 Business Objectives

- Centralize retail datasets
- Build a scalable warehouse
- Clean and standardize raw data
- Design a Star Schema
- Develop reusable dbt models
- Generate business KPIs
- Deliver interactive Power BI dashboards
- Support data-driven decision making

---

# 🛠 Technology Stack

| Layer | Technology |
|---|---|
| Data Source | CSV Files |
| Data Ingestion | Airbyte |
| Data Warehouse | Snowflake |
| Data Transformation | dbt Core |
| Programming | Python |
| Query Language | SQL |
| Data Modeling | Star Schema |
| Dashboard | Microsoft Power BI |
| Version Control | Git |
| Repository | GitHub |

---

# 🏗 Solution Architecture

```text
CSV Files
    │
    ▼
Airbyte Ingestion
    │
    ▼
Snowflake Bronze Layer
    │
    ▼
dbt Cleaning Models
    │
    ▼
Snowflake Silver Layer
    │
    ▼
dbt Business Models
    │
    ▼
Snowflake Gold Layer
    │
    ▼
Star Schema
    │
    ▼
Power BI Dashboard
    │
    ▼
Business Insights
```

---

# 🚀 Project Workflow

## Phase 1 – Data Collection
The project uses the Olist Brazilian E-Commerce dataset including Customers, Orders, Order Items, Products, Sellers, Reviews, Payments, Categories and Campaign data.

## Phase 2 – Data Ingestion
Raw CSV files are ingested through Airbyte into Snowflake. Logging and validation ensure reliable loading.

## Phase 3 – Snowflake Data Warehouse
The warehouse follows the Medallion Architecture:

- 🥉 Bronze – Raw Data
- 🥈 Silver – Cleaned & Standardized Data
- 🥇 Gold – Analytics Ready Data

## Phase 4 – Data Transformation (dbt)

Transformation includes:
- Null handling
- Type casting
- Deduplication
- Data quality tests
- Model documentation
- Reusable SQL models
  
## Phase 5 – Dimensional Modeling

Fact Table:
- Fact Orders

Dimension Tables:
- Customers
- Products
- Sellers
- Payments
- Reviews
- Categories
- Campaigns
- Date

A Star Schema is implemented for optimized analytical queries.

## Phase 6 – Business Analytics

Business metrics include:
- Revenue
- Orders
- Customer Retention
- Marketing ROI
- Product Performance
- Regional Sales
- Delivery Performance

## Phase 7 – Interactive Power BI Dashboard

Three interactive dashboard pages provide executive, marketing, and customer insights.

---

# 📊 Dashboard Pages

## 1️⃣ Executive Overview

### Business Goal
Provide executives with a high-level overview of business health, revenue growth, operational performance, and regional sales.

### KPIs
- Total Revenue
- Total Orders
- Average Order Value
- Customer Acquisition Cost
- Return on Ad Spend
- Regional Revenue
- Monthly Revenue Trend

> 📷 Adding screenshot:
> <img width="1006" height="715" alt="image" src="https://github.com/user-attachments/assets/6695bd04-707e-4902-86c5-baf5ef4edcef" />

## 2️⃣ Campaign Analytics

### Business Goal
Evaluate marketing campaigns and optimize advertising spend.

### KPIs
- Total Clicks
- CTR
- CPC
- Impressions
- ROAS
- Campaign Revenue

> 📷 Adding screenshot:
> <img width="995" height="756" alt="image" src="https://github.com/user-attachments/assets/4abd14ef-63b1-4d1d-9e02-90a111a237a4" />

## 3️⃣ Customer Insights & Logistics

### Business Goal
Analyze customer purchasing behavior and logistics performance.

### KPIs
- Customer Lifetime Value
- Average Order Value
- Fulfillment Success Rate
- Delivery SLA
- Customer Satisfaction
- Order Distribution

> 📷 Adding screenshot:
> 
<img width="1007" height="777" alt="image" src="https://github.com/user-attachments/assets/f23d2072-ba5c-42d8-b7a9-ccbb52ac9509" />
---

# 📈 Business KPIs

## Sales
- Total Revenue
- Gross Order Volume
- AOV
- Monthly Revenue

## Marketing
- ROAS
- CTR
- CPC
- CAC

## Customer
- CLV
- Repeat Buyer Ratio
- Customer Segmentation

## Logistics
- Delivery Time
- SLA Tracking
- Fulfillment Rate

---

# ⚙ Advanced DAX

```DAX
Total Revenue =
SUM(FACT_ORDERS[payment_value])
```

```DAX
AOV =
DIVIDE([Total Revenue],DISTINCTCOUNT(FACT_ORDERS[ORDER_ID]))
```

```DAX
ROAS =
DIVIDE([Revenue],[Ad Spend])
```

```DAX
CAC =
DIVIDE([Ad Spend],[New Customers])
```

```DAX
Repeat Buyer Ratio =
DIVIDE(
CALCULATE(
DISTINCTCOUNT(FACT_ORDERS[CUSTOMER_ID]),
FILTER(
VALUES(FACT_ORDERS[CUSTOMER_ID]),
COUNT(FACT_ORDERS[ORDER_ID])>1)),
DISTINCTCOUNT(FACT_ORDERS[CUSTOMER_ID]))
```

---
