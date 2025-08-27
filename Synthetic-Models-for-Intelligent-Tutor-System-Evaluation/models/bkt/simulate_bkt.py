import pandas as pd

def simulate_bkt_learner(n_tasks=10):
    """Simulates learner interactions for BKT."""
    return pd.DataFrame({
        'learner_id': [1] * n_tasks,
        'task_id': range(n_tasks),
        'correct': [0, 1, 0, 1] * (n_tasks // 4),
        'time_spent': [30, 45, 20, 50] * (n_tasks // 4)
    })
