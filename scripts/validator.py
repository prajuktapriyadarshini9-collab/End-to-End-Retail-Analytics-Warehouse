from pathlib import Path
import pandas as pd


def validate_csv(csv_path, required_columns=None):

    if not Path(csv_path).exists():
        raise FileNotFoundError(
            f"{csv_path} does not exist."
        )

    df = pd.read_csv(csv_path)

    if required_columns:

        missing_columns = (
            set(required_columns)
            - set(df.columns)
        )

        if missing_columns:

            raise ValueError(
                f"Missing columns: {missing_columns}"
            )

    return df