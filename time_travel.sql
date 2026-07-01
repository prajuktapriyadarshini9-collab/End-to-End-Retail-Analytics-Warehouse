-- ==========================================
-- Phase 10 : Snowflake Time Travel
-- Step 1 : Create Demo Table
-- ==========================================

CREATE OR REPLACE TABLE RETAIL_ANALYTICS_DB.GOLD.TIME_TRAVEL_DEMO AS
SELECT *
FROM RETAIL_ANALYTICS_DB.GOLD.DIM_CUSTOMERS
LIMIT 10;
-- ==========================================
-- Step 2 : Verify Demo Table
-- ==========================================

SELECT *
FROM RETAIL_ANALYTICS_DB.GOLD.TIME_TRAVEL_DEMO;
-- ==========================================
-- Step 3 : Drop Demo Table
-- ==========================================

DROP TABLE RETAIL_ANALYTICS_DB.GOLD.TIME_TRAVEL_DEMO;
-- ==========================================
-- Step 4 : Recover Demo Table
-- ==========================================

UNDROP TABLE RETAIL_ANALYTICS_DB.GOLD.TIME_TRAVEL_DEMO;
-- ==========================================
-- Step 5 : Verify Time Travel Recovery
-- ==========================================

SELECT *
FROM RETAIL_ANALYTICS_DB.GOLD.TIME_TRAVEL_DEMO;