def validate_data(df):
    """Validates and preprocesses engagement data."""
    required_columns = ['learner_id', 'task_id', 'correct', 'time_spent']
    if not all(col in df.columns for col in required_columns):
        raise ValueError("Missing required columns")
    return df.dropna()
