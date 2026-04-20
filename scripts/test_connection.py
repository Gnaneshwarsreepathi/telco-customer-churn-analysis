import pyodbc

server = 'localhost'
database = 'SaaS_Customer_Analytics'

conn_str = (
    f'DRIVER={{ODBC Driver 17 for SQL Server}};'
    f'SERVER={server};'
    f'DATABASE={database};'
    f'Trusted_Connection=yes;'
)

try:
    conn = pyodbc.connect(conn_str)
    print("✅ Connected to SQL Server successfully!")
    conn.close()
except Exception as e:
    print(f"❌ Connection failed: {e}")