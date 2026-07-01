from snowflake.connector.pandas_tools import write_pandas

from config import get_connection
from validator import validate_csv
from profiler import profile_dataframe
from profile_writer import save_profile
from logger import log_ingestion


def load_csv_to_snowflake(
        csv_path,
        table_name,
        required_columns,
        required_primary_key):

    source_rows = 0
    conn = None

    try:

        print(f"\nValidating {table_name}...")

        df = validate_csv(
            csv_path,
            required_columns
        )

        # Standardize dataframe column names
        df.columns = (
            df.columns
            .str.upper()
            .str.strip()
        )

        # Standardize required columns
        required_columns = [

            column
            .upper()
            .strip()

            for column

            in required_columns

        ]

        # Standardize primary key columns
        required_primary_key = [

            column
            .upper()
            .strip()

            for column

            in required_primary_key

        ]

        source_rows = len(df)

        print("Validation successful.")

        print("Profiling data...")

        profile = profile_dataframe(
            df,
            primary_key=required_primary_key
        )

        save_profile(
            table_name,
            profile
        )

        print("Profile saved.")

        print("Connecting to Snowflake...")

        conn = get_connection()

        print(f"Loading RAW.{table_name}...")

        success, nchunks, nrows, _ = write_pandas(
            conn,
            df,
            table_name=table_name
        )

        # Verification
        if source_rows != nrows:

            raise ValueError(

                f"Row count mismatch. "
                f"Source={source_rows}, "
                f"Loaded={nrows}"

            )

        print(
            f"Verification successful. "
            f"{nrows} rows loaded."
        )

        if success:

            print(
                f"Loaded {nrows} rows into RAW.{table_name}"
            )

            log_ingestion(
                table_name,
                source_rows,
                nrows,
                "SUCCESS"
            )

        else:

            log_ingestion(
                table_name,
                source_rows,
                0,
                "FAILED"
            )

    except Exception as e:

        log_ingestion(
            table_name,
            source_rows,
            0,
            "FAILED"
        )

        raise

    finally:

        if conn:

            conn.close()