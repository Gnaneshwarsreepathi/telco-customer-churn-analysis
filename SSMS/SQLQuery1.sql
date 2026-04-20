USE SaaS_Customer_Analytics;
GO

CREATE TABLE dim_customer (
    customer_id VARCHAR(50) PRIMARY KEY,
    gender VARCHAR(10),
    senior_citizen BIT,
    partner VARCHAR(5),
    dependents VARCHAR(5),
    created_date DATETIME DEFAULT GETDATE()
);

CREATE TABLE dim_service (
    service_id INT IDENTITY(1,1) PRIMARY KEY,
    customer_id VARCHAR(50),
    phone_service VARCHAR(5),
    multiple_lines VARCHAR(20),
    internet_service VARCHAR(20),
    online_security VARCHAR(20),
    online_backup VARCHAR(20),
    device_protection VARCHAR(20),
    tech_support VARCHAR(20),
    streaming_tv VARCHAR(20),
    streaming_movies VARCHAR(20),
    FOREIGN KEY (customer_id) REFERENCES dim_customer(customer_id)
);

CREATE TABLE dim_contract (
    contract_id INT IDENTITY(1,1) PRIMARY KEY,
    customer_id VARCHAR(50),
    contract_type VARCHAR(20),
    paperless_billing VARCHAR(5),
    payment_method VARCHAR(50),
    FOREIGN KEY (customer_id) REFERENCES dim_customer(customer_id)
);

CREATE TABLE fact_customer_metrics (
    metric_id INT IDENTITY(1,1) PRIMARY KEY,
    customer_id VARCHAR(50),
    tenure_months INT,
    monthly_charges DECIMAL(10,2),
    total_charges DECIMAL(10,2),
    churn_flag BIT,
    churn_date DATETIME,
    last_updated DATETIME DEFAULT GETDATE(),
    FOREIGN KEY (customer_id) REFERENCES dim_customer(customer_id)
);
GO
