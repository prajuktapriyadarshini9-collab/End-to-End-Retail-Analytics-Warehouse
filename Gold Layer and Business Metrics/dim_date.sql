SELECT DISTINCT
    CAST(order_purchase_timestamp AS DATE) AS date_key,
    EXTRACT(YEAR FROM order_purchase_timestamp) AS year,
    EXTRACT(MONTH FROM order_purchase_timestamp) AS month,
    EXTRACT(DAY FROM order_purchase_timestamp) AS day,
    DAYNAME(order_purchase_timestamp) AS day_name,
    MONTHNAME(order_purchase_timestamp) AS month_name
FROM {{ ref('sl_orders') }}
WHERE order_purchase_timestamp IS NOT NULL