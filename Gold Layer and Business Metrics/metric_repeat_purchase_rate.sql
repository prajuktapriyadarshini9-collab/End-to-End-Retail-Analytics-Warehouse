WITH customer_orders AS (

    SELECT
        dc.customer_unique_id,
        COUNT(DISTINCT fo.order_id) AS total_orders

    FROM {{ ref('fact_orders') }} fo
    JOIN {{ ref('dim_customers') }} dc
      ON fo.customer_id = dc.customer_id

    GROUP BY dc.customer_unique_id

)

SELECT
    COUNT_IF(total_orders > 1) AS repeat_customers,

    ROUND(
        COUNT_IF(total_orders > 1) * 100.0 /
        COUNT(*),
        2
    ) AS repeat_purchase_rate

FROM customer_orders