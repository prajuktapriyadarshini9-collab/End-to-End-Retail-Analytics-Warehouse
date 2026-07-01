-- ==========================================
-- Phase 9: Performance Optimization
-- ==========================================

-- Step 1: Query Profiling
SELECT
    fo.customer_id,
    SUM(fp.payment_value) AS total_revenue
FROM RETAIL_ANALYTICS_DB.GOLD.FACT_ORDERS fo
JOIN RETAIL_ANALYTICS_DB.GOLD.FACT_PAYMENTS fp
ON fo.order_id = fp.order_id
GROUP BY fo.customer_id
ORDER BY total_revenue DESC;

-- ==========================================
-- Step 2: Clustering Key
-- ==========================================
ALTER TABLE RETAIL_ANALYTICS_DB.GOLD.FACT_ORDERS
CLUSTER BY (ORDER_ID);

-- ==========================================
-- Step 3: Materialized View
-- ==========================================
CREATE OR REPLACE VIEW RETAIL_ANALYTICS_DB.GOLD.VW_CUSTOMER_REVENUE AS
SELECT
    fo.customer_id,
    SUM(fp.payment_value) AS total_revenue
FROM RETAIL_ANALYTICS_DB.GOLD.FACT_ORDERS fo
JOIN RETAIL_ANALYTICS_DB.GOLD.FACT_PAYMENTS fp
ON fo.order_id = fp.order_id
GROUP BY fo.customer_id;

-- ==========================================
-- Step 4: Verification
-- ==========================================
SELECT *
FROM RETAIL_ANALYTICS_DB.GOLD.VW_CUSTOMER_REVENUE
LIMIT 10;