def calculate_affective_metrics(data):
    """Calculates affective engagement metrics (e.g., frustration)."""
    frustration = (data['time_spent'] > 60).mean()  # Example: Long pauses indicate frustration
    return {'frustration': frustration}
