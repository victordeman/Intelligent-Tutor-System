import os

def load_data(df, output_path='data/processed/processed_data.csv'):
    """Loads processed data to file."""
    if df is None:
        return False
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    return True
