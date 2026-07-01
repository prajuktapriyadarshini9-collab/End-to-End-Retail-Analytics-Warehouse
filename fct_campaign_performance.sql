SELECT
    campaign_id,
    campaign_name,
    platform,
    campaign_date,
    spend,
    clicks,
    impressions
FROM {{ ref('dim_campaigns') }}