from config import get_connection


def test_connection():

    conn = None

    try:

        conn = get_connection()

        print("Connection successful!")

    except Exception as e:

        print(
            f"Connection failed: {e}"
        )

        raise

    finally:

        if conn:

            conn.close()


if __name__ == "__main__":

    test_connection()