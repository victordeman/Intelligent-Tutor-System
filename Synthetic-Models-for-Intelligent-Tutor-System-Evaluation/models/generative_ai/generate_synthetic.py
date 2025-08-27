import pandas as pd

def generate_synthetic_data(n_tasks=10):
    """Generates synthetic learner data."""
    return pd.DataFrame({
        'learner_id': [1] * n_tasks,
        'task_id': range(n_tasks),
        'correct': [0, 1] * (n_tasks // 2),
        'time_spent': [30, 60] * (n_tasks // 2),
        'response': ['print(i' + ')' * (i % 2) for i in range(n_tasks)]  # Simulated buggy code
    })
