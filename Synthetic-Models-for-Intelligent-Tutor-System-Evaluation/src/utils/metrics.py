def calculate_outcomes(correct, total):
    """Calculates learning outcome metrics (e.g., accuracy)."""
    return correct / total if total > 0 else 0

def calculate_engagement(interactions, time_spent):
    """Calculates engagement metrics."""
    return {'interactions': interactions, 'avg_time': time_spent / interactions if interactions > 0 else 0}
