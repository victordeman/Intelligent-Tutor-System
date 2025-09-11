import pytest
import pandas as pd
from models.agent_based.simulate_agents import simulate_agents
from models.agent_based.agent_model import Agent

@pytest.fixture
def sample_data():
    return pd.DataFrame({
        'learner_id': [1, 1, 2, 2, 3, 3],
        'task_id': [1, 2, 1, 2, 1, 2],
        'correct': [1, 0, 1, 0, 1, 1],
        'time_spent': [30, 45, 25, 60, 35, 40]
    })

def test_simulate_agents(sample_data):
    sim_data = simulate_agents(sample_data)
    assert not sim_data.empty, "Agent simulation empty"
    assert 'correct' in sim_data.columns, "Missing correct column"
    assert sim_data['correct'].isin([0, 1]).all(), "Invalid correct values"
    assert len(sim_data) == len(sample_data), "Mismatched simulation length"

def test_agent_skill_update():
    agent = Agent(learner_id=1, initial_skill=0.5)
    initial_skill = agent.skill_level
    agent.update_skill(correct=True)
    assert agent.skill_level > initial_skill, "Skill did not increase"
    agent.update_skill(correct=False)
    assert agent.skill_level < 0.6, "Skill did not decrease"