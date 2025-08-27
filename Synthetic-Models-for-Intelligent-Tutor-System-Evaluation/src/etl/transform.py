from src.utils.data_processing import validate_data

def transform_data(df):
    """Transforms data for model input."""
    if df is None:
        return None
    df = validate_data(df)
    # Example: Normalize engagement metrics
    df['time_spent'] = df.get('time_spent', 0) / df['time_spent'].max()
    return df
