SELECT
    total_spend,
    total_customers,
    ROUND(
        total_spend / NULLIF(total_customers, 0),
        2
    ) AS customer_acquisition_cost
FROM
(
    SELECT
        SUM(spend) AS total_spend
    FROM {{ ref('fct_campaign_performance') }}
) s
CROSS JOIN
(
    SELECT
        COUNT(DISTINCT customer_unique_id) AS total_customers
    FROM {{ ref('dim_customers') }}
) c