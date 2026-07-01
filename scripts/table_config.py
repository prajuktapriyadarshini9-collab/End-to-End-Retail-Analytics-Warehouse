TABLES = {

    "CUSTOMERS": {

        "path":
        "data/olist_customers_dataset.csv",

        "columns": [

            "customer_id",
            "customer_unique_id",
            "customer_zip_code_prefix",
            "customer_city",
            "customer_state"

        ],

        "primary_key": [

            "customer_id"

        ]

    },

    "ORDERS": {

        "path":
        "data/olist_orders_dataset.csv",

        "columns": [

            "order_id",
            "customer_id",
            "order_status",
            "order_purchase_timestamp",
            "order_approved_at",
            "order_delivered_carrier_date",
            "order_delivered_customer_date",
            "order_estimated_delivery_date"

        ],

        "primary_key": [

            "order_id"

        ]

    },

    "ORDER_ITEMS": {

        "path":
        "data/olist_order_items_dataset.csv",

        "columns": [

            "order_id",
            "order_item_id",
            "product_id",
            "seller_id",
            "shipping_limit_date",
            "price",
            "freight_value"

        ],

        "primary_key": [

            "order_id",
            "order_item_id"

        ]

    },

    "PRODUCTS": {

        "path":
        "data/olist_products_dataset.csv",

        "columns": [

            "product_id",
            "product_category_name",
            "product_name_lenght",
            "product_description_lenght",
            "product_photos_qty",
            "product_weight_g",
            "product_length_cm",
            "product_height_cm",
            "product_width_cm"

        ],

        "primary_key": [

            "product_id"

        ]

    },

    "PAYMENTS": {

        "path":
        "data/olist_order_payments_dataset.csv",

        "columns": [

            "order_id",
            "payment_sequential",
            "payment_type",
            "payment_installments",
            "payment_value"

        ],

        "primary_key": [

            "order_id",
            "payment_sequential"

        ]

    },

    "SELLERS": {

        "path":
        "data/olist_sellers_dataset.csv",

        "columns": [

            "seller_id",
            "seller_zip_code_prefix",
            "seller_city",
            "seller_state"

        ],

        "primary_key": [

            "seller_id"

        ]

    },

    "CAMPAIGNS": {

        "path":
        "data/campaign_data.csv",

        "columns": [

            "campaign_id",
            "campaign_name",
            "platform",
            "campaign_date",
            "spend",
            "clicks",
            "impressions"

        ],

        "primary_key": [

            "campaign_id"

        ]

    }

}