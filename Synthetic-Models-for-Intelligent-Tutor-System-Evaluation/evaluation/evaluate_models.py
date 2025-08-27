from src.utils.metrics import calculate_outcomes, calculate_engagement

def evaluate_model(model_type, data):
    """Evaluates a model against tasks."""
    outcomes = calculate_outcomes(data['correct'].sum(), len(data))
    engagement = calculate_engagement(len(data), data['time_spent'].sum())
    return {'model': model_type, 'outcomes': outcomes, 'engagement': engagement}
