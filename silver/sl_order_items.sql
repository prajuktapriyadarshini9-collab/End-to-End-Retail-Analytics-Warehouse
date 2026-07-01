{{ config(
    materialized='table'
) }}

SELECT
    order_id,
    order_item_id,
    product_id,
    seller_id,
    shipping_limit_date,
    price,
    freight_value

FROM {{ ref('br_order_items') }}