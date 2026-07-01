SELECT
    r.total_revenue,
    c.total_spend,
    r.total_revenue / NULLIF(c.total_spend, 0) AS roas
FROM
(
    SELECT SUM(payment_value) AS total_revenue
    FROM {{ ref('fact_payments') }}
) r
CROSS JOIN
(
    SELECT SUM(spend) AS total_spend
    FROM {{ ref('fct_campaign_performance') }}
) c