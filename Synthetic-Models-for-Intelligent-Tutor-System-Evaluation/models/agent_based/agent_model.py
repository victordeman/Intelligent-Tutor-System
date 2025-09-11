import numpy as np
import pandas as pd

class Agent:
    def __init__(self, learner_id, initial_skill=0.5):
        self.learner_id = learner_id
        self.skill_level = initial_skill

    def update_skill(self, correct, learning_rate=0.1, forgetting_rate=0.05):
        if correct:
            self.skill_level = min(1.0, self.skill_level + learning_rate)
        else:
            self.skill_level = max(0.0, self.skill_level - forgetting_rate)
        return self.skill_level

    def predict_correct(self, task_difficulty=0.5):
        prob_correct = self.skill_level / (self.skill_level + task_difficulty)
        return np.random.random() < prob_correct

def simulate_agent(data, learner_id=None, initial_skill=0.5):
    agent = Agent(learner_id=learner_id or data['learner_id'].iloc[0], initial_skill=initial_skill)
    results = []
    
    for _, row in data.iterrows():
        correct = agent.predict_correct(task_difficulty=0.5)
        skill = agent.update_skill(correct=correct)
        results.append({
            'learner_id': agent.learner_id,
            'task_id': row['task_id'],
            'correct': int(correct),
            'skill_level': skill
        })
    
    return pd.DataFrame(results)