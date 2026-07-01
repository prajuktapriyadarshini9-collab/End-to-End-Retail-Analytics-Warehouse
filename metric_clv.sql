SELECT
    dc.customer_unique_id,
    SUM(fp.payment_value) AS customer_lifetime_value
FROM {{ ref('fact_orders') }} fo
JOIN {{ ref('fact_payments') }} fp
    ON fo.order_id = fp.order_id
JOIN {{ ref('dim_customers') }} dc
    ON fo.customer_id = dc.customer_id
GROUP BY dc.customer_unique_id