USE SaaS_Customer_Analytics;

-- Clear all tables in correct order
DELETE FROM fact_customer_metrics;
DELETE FROM dim_contract;
DELETE FROM dim_service;
DELETE FROM dim_customer;

PRINT 'All tables cleared!';


USE SaaS_Customer_Analytics;
DELETE FROM fact_customer_metrics;
PRINT 'fact table cleared!';

USE SaaS_Customer_Analytics;

SELECT 'dim_customer' as TableName, COUNT(*) as Records FROM dim_customer
UNION ALL
SELECT 'dim_service', COUNT(*) FROM dim_service
UNION ALL
SELECT 'dim_contract', COUNT(*) FROM dim_contract
UNION ALL
SELECT 'fact_customer_metrics', COUNT(*) FROM fact_customer_metrics;