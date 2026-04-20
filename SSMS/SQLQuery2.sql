select *  from [dbo].[dim_contract];

USE SaaS_Customer_Analytics;
GO
SELECT COUNT(*) AS TotalRows FROM stg_telco_churn;

USE SaaS_Customer_Analytics;
GO

INSERT INTO dim_customer (customer_id, gender, senior_citizen, partner, dependents)
SELECT DISTINCT
    customerID,
    gender,
    SeniorCitizen,
    Partner,
    Dependents
FROM stg_telco_churn;


INSERT INTO dim_service (
    customer_id, phone_service, multiple_lines, internet_service,
    online_security, online_backup, device_protection, tech_support,
    streaming_tv, streaming_movies
)
SELECT
    customerID,
    PhoneService,
    MultipleLines,
    InternetService,
    OnlineSecurity,
    OnlineBackup,
    DeviceProtection,
    TechSupport,
    StreamingTV,
    StreamingMovies
FROM stg_telco_churn;


INSERT INTO dim_contract (customer_id, contract_type, paperless_billing, payment_method)
SELECT
    customerID,
    Contract,
    PaperlessBilling,
    PaymentMethod
FROM stg_telco_churn;

INSERT INTO fact_customer_metrics
(customer_id, tenure_months, monthly_charges, total_charges, churn_flag, churn_date)
SELECT
    customerID,
    tenure,
    MonthlyCharges,
    TRY_CONVERT(DECIMAL(10,2), TotalCharges),
    CASE WHEN Churn='Yes' THEN 1 ELSE 0 END,
    CASE WHEN Churn='Yes' THEN GETDATE() ELSE NULL END
FROM stg_telco_churn;


SELECT COUNT(*) AS Customers FROM dim_customer;
SELECT COUNT(*) AS Services  FROM dim_service;
SELECT COUNT(*) AS Contracts FROM dim_contract;
SELECT COUNT(*) AS Metrics   FROM fact_customer_metrics;


USE SaaS_Customer_Analytics;
GO

CREATE OR ALTER VIEW vw_customer_360 AS
SELECT 
    c.customer_id,
    c.gender,
    c.senior_citizen,
    c.partner,
    c.dependents,

    s.phone_service,
    s.multiple_lines,
    s.internet_service,
    s.online_security,
    s.online_backup,
    s.device_protection,
    s.tech_support,
    s.streaming_tv,
    s.streaming_movies,

    ct.contract_type,
    ct.paperless_billing,
    ct.payment_method,

    m.tenure_months,
    m.monthly_charges,
    m.total_charges,
    m.churn_flag,
    m.churn_date,
    m.last_updated
FROM dim_customer c
LEFT JOIN dim_service s 
    ON c.customer_id = s.customer_id
LEFT JOIN dim_contract ct 
    ON c.customer_id = ct.customer_id
LEFT JOIN fact_customer_metrics m 
    ON c.customer_id = m.customer_id;
GO


SELECT TOP 10 * FROM vw_customer_360;

select * from [dbo].[dim_contract]
select * from [dbo].[dim_customer]
select * from [dbo].[dim_service]
select * from [dbo].[fact_customer_metrics]
select COUNT(*) from [dbo].[stg_telco_churn]
select * from [dbo].[stg_telco_churn]