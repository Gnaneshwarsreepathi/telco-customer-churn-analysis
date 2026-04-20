import pandas as pd
import pyodbc
import numpy as np
from datetime import datetime

# Connect using pyodbc directly
print("🔌 Connecting to SQL Server...")
conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=localhost;'
    'DATABASE=SaaS_Customer_Analytics;'
    'Trusted_Connection=yes;'
)
cursor = conn.cursor()
print("✅ Connected to SQL Server!")

# Load CSV
print("📂 Loading CSV file...")
df = pd.read_csv('data/raw/WA_Fn-UseC_-Telco-Customer-Churn.csv')
print(f"✅ Loaded {len(df)} records")

# Clean data
print("🧹 Cleaning data...")
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
df['TotalCharges'] = df['TotalCharges'].fillna(df['MonthlyCharges'])
df['Churn'] = df['Churn'].map({'Yes': 1, 'No': 0})
print("✅ Data cleaned")

# Load dim_customer
print("📤 Loading dim_customer...")
for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO dim_customer 
        (customer_id, gender, senior_citizen, partner, dependents)
        VALUES (?, ?, ?, ?, ?)
    """,
    row['customerID'],
    row['gender'],
    int(row['SeniorCitizen']),
    row['Partner'],
    row['Dependents'])
conn.commit()
print(f"✅ {len(df)} rows loaded into dim_customer")

# Load dim_service
print("📤 Loading dim_service...")
for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO dim_service 
        (customer_id, phone_service, multiple_lines, internet_service,
         online_security, online_backup, device_protection,
         tech_support, streaming_tv, streaming_movies)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """,
    row['customerID'], row['PhoneService'], row['MultipleLines'],
    row['InternetService'], row['OnlineSecurity'], row['OnlineBackup'],
    row['DeviceProtection'], row['TechSupport'], row['StreamingTV'],
    row['StreamingMovies'])
conn.commit()
print(f"✅ {len(df)} rows loaded into dim_service")

# Load dim_contract
print("📤 Loading dim_contract...")
for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO dim_contract
        (customer_id, contract_type, paperless_billing, payment_method)
        VALUES (?, ?, ?, ?)
    """,
    row['customerID'], row['Contract'],
    row['PaperlessBilling'], row['PaymentMethod'])
conn.commit()
print(f"✅ {len(df)} rows loaded into dim_contract")

# Load fact_customer_metrics
print("📤 Loading fact_customer_metrics...")
for _, row in df.iterrows():
    churn_date = datetime.now() if row['Churn'] == 1 else None
    cursor.execute("""
        INSERT INTO fact_customer_metrics
        (customer_id, tenure_months, monthly_charges, total_charges,
         churn_flag, churn_date)
        VALUES (?, ?, ?, ?, ?, ?)
    """,
    row['customerID'], int(row['tenure']),
    float(row['MonthlyCharges']), float(row['TotalCharges']),
    int(row['Churn']), churn_date)
conn.commit()
print(f"✅ {len(df)} rows loaded into fact_customer_metrics")

cursor.close()
conn.close()

print("\n🎉 ETL Pipeline Completed Successfully!")
print(f"Total customers loaded: {len(df)}")