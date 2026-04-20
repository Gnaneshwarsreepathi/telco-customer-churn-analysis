# 📊 Telco Customer Churn Analytics with CRM Integration

## 🚀 Overview

This project presents an end-to-end data analytics solution to analyze customer churn in a telecom business and evaluate its impact on revenue and sales pipeline.

The solution integrates **Salesforce CRM**, SQL-based data modeling, Python data processing, and Power BI dashboards to generate actionable business insights.

---

## 🎯 Business Objectives

* Identify customers likely to churn
* Analyze revenue at risk due to churn
* Understand customer behavior patterns
* Evaluate sales pipeline performance
* Support CRM-driven decision making

---

## 🏗️ Project Architecture

### 🔹 Data Sources

* Telecom Customer Dataset (Excel/CSV)
* Salesforce CRM (Accounts, Opportunities)

### 🔹 Data Processing Workflow

1. Raw data imported into SQL Server (SSMS)
2. Data cleaned and transformed using SQL & Python
3. Data modeled into **Star Schema**
4. Power BI connected to SQL Server and CRM
5. Interactive dashboards built for insights

---

## 🧱 Data Modeling (SQL - Star Schema)

### Fact Table:

* `fact_customer_metrics`

  * tenure_months
  * monthly_charges
  * total_charges
  * churn_flag

### Dimension Tables:

* `dim_customer` → customer details
* `dim_contract` → contract & payment info
* `dim_service` → services used

### Staging Table:

* `stg_telco_churn` → raw dataset

---

## ⚙️ Tools & Technologies

* SQL Server (SSMS)
* Python (Pandas, NumPy)
* Power BI
* Salesforce CRM
* GitHub

---

## 📈 Power BI Dashboards

### 1️⃣ Executive Overview Dashboard

* Churn Rate %
* Total Customers
* Churned Customers
* Revenue at Risk
* Avg Tenure
* Monthly Revenue

---

### 2️⃣ Churn Analysis Dashboard

* Churn by Payment Method
* Churn by Internet Service
* Churn by Senior Citizen
* Churn by Gender
* Contract Type Filters

---

### 3️⃣ Revenue Insights Dashboard

* Total Revenue
* Revenue at Risk
* Average Tenure
* Revenue by Contract Type
* Revenue by Payment Method

---

### 4️⃣ CRM Risk Dashboard

* Total Deals
* Won Deals
* Pipeline Revenue
* Expected Revenue
* Deals by Stage
* Revenue by Lead Source
* Funnel Analysis

---

## 🔗 CRM Integration (Salesforce)

This project integrates **Salesforce CRM** with Power BI to combine customer churn insights with sales pipeline data.

### Data Extracted from CRM:

* Customer Accounts
* Opportunity Data (Sales Pipeline)
* Lead Sources

### Integration Steps:

1. Connected Salesforce to Power BI using native connector
2. Imported CRM tables (Accounts, Opportunities)
3. Combined CRM data with churn dataset
4. Built dashboards for pipeline risk analysis

### Business Value:

* Identify revenue risk due to churn
* Analyze sales pipeline performance
* Enable data-driven CRM decisions

---

## 📊 Key Insights

* Month-to-month contracts have highest churn rate
* Electronic check users show higher churn behavior
* Fiber optic users show higher churn compared to DSL
* High churn directly impacts revenue pipeline
* CRM integration helps track revenue risk in sales funnel

---

## 📁 Project Structure

```
telco-customer-churn-analysis/
│
├── dashboards/           # Power BI (.pbix) files
├── data/processed/       # Cleaned datasets
├── dataset/              # Raw dataset
├── docs/images/          # Dashboard & CRM screenshots
├── notebooks/            # Python analysis notebooks
├── scripts/              # SQL & Python scripts
├── SSMS/                 # SQL queries & schema
├── README.md
└── .gitignore
```

---

## 📸 Dashboard Previews

### Executive Overview
![Executive Overview](docs/images/executive_overview.png)

### Churn Analysis
![Churn Analysis](docs/images/churn_analysis.png)

### Revenue Insights
![Revenue Insights](docs/images/revenue_insights.png)

### CRM Risk Dashboard
![CRM Dashboard](docs/images/crm_dashboard.png)
```

---

## 🧠 Learning Outcomes

- Built end-to-end data analytics pipeline  
- Designed star schema data model  
- Performed data transformation using SQL & Python  
- Developed interactive Power BI dashboards  
- Integrated CRM (Salesforce) with analytics  
- Delivered business-focused insights  

---

## 👨‍💻 Author

**Gnaneshwar Sreepati**  
Aspiring Data Analyst | Power BI | SQL | Python  

---

## ⭐ Support

If you like this project, consider giving it a ⭐ on GitHub!
