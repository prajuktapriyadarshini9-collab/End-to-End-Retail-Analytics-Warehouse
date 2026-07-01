SELECT
    customer_id,
    customer_unique_id,
    customer_city,
    customer_state,

    CURRENT_DATE() AS effective_date,

    NULL AS end_date,

    TRUE AS is_current

FROM {{ ref('dim_customers') }}