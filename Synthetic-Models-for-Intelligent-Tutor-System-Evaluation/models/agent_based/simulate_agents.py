import pandas as pd
from .agent_model import Agent, simulate_agent

def simulate_agents(data, n_learners=5, n_tasks=10, initial_skill=0.5):
    """Simulates multiple agent-based learners."""
    if data.empty:
        data = pd.DataFrame({
            'learner_id': [i for i in range(1, n_learners + 1) for _ in range(n_tasks)],
            'task_id': list(range(n_tasks)) * n_learners,
            'correct': [0, 1] * (n_learners * n_tasks // 2),
            'time_spent': [30, 45] * (n_learners * n_tasks // 2)
        })
    
    results = []
    for learner_id in data['learner_id'].unique():
        learner_data = data[data['learner_id'] == learner_id][['learner_id', 'task_id']]
        sim_data = simulate_agent(learner_data, learner_id=learner_id, initial_skill=initial_skill)
        results.append(sim_data)
    
    sim_results = pd.concat(results, ignore_index=True)
    print("Simulated agent data:", sim_results[['learner_id', 'task_id', 'correct']].head())
    return sim_results