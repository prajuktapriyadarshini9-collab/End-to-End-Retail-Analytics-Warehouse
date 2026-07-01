SELECT
    SUM(payment_value) / COUNT(DISTINCT order_id) AS average_order_value
FROM {{ ref('fact_payments') }}