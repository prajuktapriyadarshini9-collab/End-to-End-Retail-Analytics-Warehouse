def profile_dataframe(
        df,
        primary_key=None):

    profile = {

        "rows":
        len(df),

        "columns":
        len(df.columns),

        "duplicate_rows":
        int(
            df
            .duplicated()
            .sum()
        ),

        "null_counts":
        (
            df
            .isnull()
            .sum()
            .to_dict()
        )

    }

    # Duplicate primary key check

    if primary_key:

        duplicate_primary_keys = int(

            df

            .duplicated(
                subset=primary_key
            )

            .sum()

        )

        profile[
            "duplicate_primary_keys"
        ] = duplicate_primary_keys

    return profile