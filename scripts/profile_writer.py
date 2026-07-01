import json
from pathlib import Path


def save_profile(
        table_name,
        profile):

    Path(
        "reports/profiles"
    ).mkdir(
        parents=True,
        exist_ok=True
    )

    file_path = (
        f"reports/profiles/"
        f"{table_name.lower()}_profile.json"
    )

    with open(
            file_path,
            "w") as f:

        json.dump(
            profile,
            f,
            indent=4
        )