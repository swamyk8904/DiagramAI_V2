import pandas as pd


def read_csv(file_path):
    """
    Reads a CSV file and converts it to text.
    """

    try:
        df = pd.read_csv(file_path)

        return df.to_string(index=False)

    except Exception as e:
        return f"Error reading CSV: {e}"