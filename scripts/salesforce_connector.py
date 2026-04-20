import pyodbc
import requests
import pandas as pd
import json

print("=" * 50)
print("  SALESFORCE CRM INTEGRATION")
print("=" * 50)

# ============================================
# STEP 1: GET DATA FROM SQL SERVER
# ============================================
print("\n📂 Loading data from SQL Server...")
conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=localhost;'
    'DATABASE=SaaS_Customer_Analytics;'
    'Trusted_Connection=yes;'
)

query = """
SELECT TOP 50
    c.customer_id,
    c.gender,
    c.senior_citizen,
    c.partner,
    c.dependents,
    ct.contract_type,
    ct.payment_method,
    m.tenure_months,
    m.monthly_charges,
    m.total_charges,
    m.churn_flag
FROM dim_customer c
JOIN dim_contract ct ON c.customer_id = ct.customer_id
JOIN fact_customer_metrics m ON c.customer_id = m.customer_id
"""

df = pd.read_sql(query, conn)
conn.close()
print(f"✅ Loaded {len(df)} records from SQL Server")

# ============================================
# STEP 2: PREPARE CRM DATA
# ============================================
print("\n🔄 Preparing CRM data...")

# Segment customers by churn risk
def get_churn_risk(row):
    if row['churn_flag']:
        return 'HIGH'
    elif row['tenure_months'] < 12:
        return 'MEDIUM'
    else:
        return 'LOW'

def get_retention_action(row):
    if row['churn_flag']:
        return 'Immediate outreach - offer discount'
    elif row['tenure_months'] < 12:
        return 'Send loyalty reward'
    else:
        return 'Regular engagement'

df['churn_risk'] = df.apply(get_churn_risk, axis=1)
df['retention_action'] = df.apply(get_retention_action, axis=1)

print("✅ CRM data prepared")
print(f"\n📊 Churn Risk Summary:")
print(df['churn_risk'].value_counts())

# ============================================
# STEP 3: SAVE CRM DATA TO FILE
# (Simulating CRM push - ready for Salesforce)
# ============================================
print("\n💾 Saving CRM-ready data...")

crm_data = []
for _, row in df.iterrows():
    crm_data.append({
        'customer_id': row['customer_id'],
        'gender': row['gender'],
        'contract_type': row['contract_type'],
        'payment_method': row['payment_method'],
        'tenure_months': int(row['tenure_months']),
        'monthly_charges': float(row['monthly_charges']),
        'total_charges': float(row['total_charges']),
        'churn_risk': row['churn_risk'],
        'retention_action': row['retention_action'],
        'is_churned': bool(row['churn_flag'])
    })

# Save to JSON file
with open('data/processed/crm_ready_data.json', 'w') as f:
    json.dump(crm_data, f, indent=2)

print(f"✅ Saved {len(crm_data)} records to data/processed/crm_ready_data.json")

# Save to CSV for Power BI
df.to_csv('data/processed/crm_enriched_data.csv', index=False)
print(f"✅ Saved to data/processed/crm_enriched_data.csv")

# ============================================
# STEP 4: SUMMARY REPORT
# ============================================
print("\n" + "=" * 50)
print("  CRM INTEGRATION SUMMARY")
print("=" * 50)
print(f"Total Customers Processed : {len(df)}")
print(f"High Churn Risk           : {len(df[df['churn_risk']=='HIGH'])}")
print(f"Medium Churn Risk         : {len(df[df['churn_risk']=='MEDIUM'])}")
print(f"Low Churn Risk            : {len(df[df['churn_risk']=='LOW'])}")
print(f"Avg Monthly Charges       : €{df['monthly_charges'].mean():.2f}")
print(f"Total Revenue at Risk     : €{df[df['churn_risk']=='HIGH']['monthly_charges'].sum():.2f}")
print("\n🎉 CRM Integration Complete!")
print("📁 Files saved in data/processed/ folder")