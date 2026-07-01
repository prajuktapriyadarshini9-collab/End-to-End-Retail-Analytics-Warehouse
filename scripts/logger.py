import csv
from pathlib import Path
from datetime import datetime

LOG_FILE = "reports/ingestion_log.csv"


def log_ingestion(
        table_name,
        source_rows,
        loaded_rows,
        status):

    Path("reports").mkdir(
        exist_ok=True
    )

    file_exists = Path(
        LOG_FILE
    ).exists()

    with open(
            LOG_FILE,
            mode="a",
            newline=""
    ) as f:

        writer = csv.writer(f)

        if not file_exists:

            writer.writerow([
                "timestamp",
                "table_name",
                "source_rows",
                "loaded_rows",
                "status"
            ])

        writer.writerow([
            datetime.now(),
            table_name,
            source_rows,
            loaded_rows,
            status
        ])