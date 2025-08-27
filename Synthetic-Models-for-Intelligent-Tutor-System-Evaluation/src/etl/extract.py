import pandas as pd

def extract_data(file_path):
    """Extracts data from synthetic CSV file."""
    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        print(f"Error extracting data: {e}")
        return None
