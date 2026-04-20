# 📊 Telco Customer Churn Analytics with CRM Integration

## 🚀 Overview

This project presents an end-to-end data analytics solution to analyze customer churn in a telecom business and evaluate its impact on revenue and sales pipeline.

It integrates **Salesforce CRM data**, SQL-based data modeling, Python data processing, and Power BI dashboards to generate actionable business insights.

---

## 🎯 Business Objectives

* Identify customers likely to churn
* Analyze revenue at risk due to churn
* Understand customer behavior patterns
* Evaluate sales pipeline performance
* Support CRM-driven decision making

---

## 🏗️ Project Architecture

```
Raw Dataset (CSV)
        ↓
SQL Server (Star Schema)
        ↓
Python (ETL + Data Enrichment)
        ↓
Salesforce CRM Integration
        ↓
Power BI Dashboards
```

---

## 🔗 Data Sources

* Telco Customer Churn Dataset (CSV)
* Salesforce CRM

  * Accounts
  * Opportunities
  * Lead Source data

---

## 🧱 Data Model

### Dimension Tables

* `dim_customer`
* `dim_service`
* `dim_contract`

### Fact Table

* `fact_customer_metrics`

### CRM / Enriched Data

* `crm_enriched_data`

---

## ⚙️ Technologies Used

* Python (Pandas, NumPy)
* SQL Server (SSMS)
* Power BI
* Salesforce CRM
* Data Modeling (Star Schema)

---

## 📊 Key Insights

* 📉 Churn Rate: **26.54%**
* ⚠️ Month-to-month contracts have highest churn (**42%+**)
* 💰 Revenue at Risk: **€139K**
* 👥 New customers and low-tenure users churn more
* 💸 Higher monthly charges correlate with higher churn
* 📊 External referrals generate highest CRM revenue

---

## 📈 Dashboards

### 🔹 Executive Overview

![Executive Overview](docs/images/executive_overview.png)

---

### 🔹 Churn Analysis Dashboard

![Churn Analysis](docs/images/churn_analysis.png)

---

### 🔹 Revenue Insights Dashboard

![Revenue Insights](docs/images/revenue_insights.png)

---

### 🔹 CRM Risk Dashboard

![CRM Dashboard](docs/images/crm_dashboard.png)

---

## 📊 Key Metrics (DAX)

* **Total Revenue**
* **Total Customers**
* **Churn Rate (%)**
* **Revenue at Risk**
* **Average Tenure**
* **Total Deals (CRM)**
* **Won Deals**
* **Pipeline Revenue**
* **Expected Revenue**

---

## 🧠 Key Features

* End-to-end data pipeline
* Star schema data modeling
* Salesforce CRM data integration
* Customer segmentation and churn analysis
* Sales pipeline and deal stage analysis
* Revenue risk identification

---

## 📂 Project Structure

```
data/
notebooks/
scripts/
dashboards/
docs/images/
README.md
```

---

## 📌 Future Improvements

* Real-time Salesforce API integration
* Machine learning model for churn prediction
* Automated data refresh pipeline
* Advanced customer segmentation

---

## 👨‍💻 Author

**Gnaneshwar Sreepathi**
