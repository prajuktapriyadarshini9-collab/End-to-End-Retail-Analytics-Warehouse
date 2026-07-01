SELECT
    SUM(payment_value) AS total_revenue
FROM {{ ref('fact_payments') }}