from ingest_table import load_csv_to_snowflake
from table_config import TABLES


for table_name, config in TABLES.items():

    print(f"\nProcessing {table_name}")

    load_csv_to_snowflake(

        csv_path=config["path"],

        table_name=table_name,

        required_columns=config["columns"],
        required_primary_key=config["primary_key"]
        


    )

print("\nIngestion completed.")