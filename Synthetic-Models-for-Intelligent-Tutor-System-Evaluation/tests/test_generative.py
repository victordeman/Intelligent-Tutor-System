import pytest
import pandas as pd
from models.generative_ai.generative_model import generate_response, evaluate_response, simulate_generative

@pytest.fixture
def sample_data():
    return pd.DataFrame({
        'learner_id': [1, 1, 2, 2, 3, 3],
        'task_id': [1, 2, 1, 2, 1, 2],
        'correct': [1, 0, 1, 0, 1, 1],
        'time_spent': [30, 45, 25, 60, 35, 40],
        'response': ["print('Hello')", "print(Hello", "SELECT * FROM table", "SELECT * FROM", "print('World')", "SELECT name FROM table"]
    })

def test_generate_response():
    response = generate_response("print('Hello')", error_rate=0.0)
    assert response == "print('Hello')", "Correct response altered"
    response = generate_response("SELECT * FROM table", error_rate=1.0)
    assert response != "SELECT * FROM table", "Error not introduced"

def test_evaluate_response():
    assert evaluate_response("print('Hello')", "print('Hello')") == 1.0, "Correct Python failed"
    assert evaluate_response("print(Hello", "print('Hello')") == 0.0, "Invalid Python scored"
    assert evaluate_response("SELECT * FROM table", "SELECT * FROM table") == 1.0, "Correct SQL failed"
    assert evaluate_response("SELECT * FORM table", "SELECT * FROM table") == 0.7, "Valid SQL typo failed"

def test_simulate_generative(sample_data):
    sim_data = simulate_generative(sample_data)
    assert not sim_data.empty, "Generative simulation empty"
    assert 'score' in sim_data.columns, "Missing score column"
    assert all(0 <= sim_data['score']) and all(sim_data['score'] <= 1), "Invalid score values"