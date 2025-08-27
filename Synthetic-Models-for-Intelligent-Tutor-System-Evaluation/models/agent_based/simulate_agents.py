import pandas as pd

def simulate_agents(n_learners=5, n_tasks=10):
    """Simulates multiple agent-based learners."""
    return pd.DataFrame({
        'learner_id': [i for i in range(n_learners) for _ in range(n_tasks)],
        'task_id': list(range(n_tasks)) * n_learners,
        'correct': [0, 1] * (n_learners * n_tasks // 2),
        'time_spent': [30, 45] * (n_learners * n_tasks // 2)
    })
