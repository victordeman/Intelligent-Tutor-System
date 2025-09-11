import pytest
import pandas as pd
from models.bkt.bkt_model import train_bkt, predict_bkt

@pytest.fixture
def sample_data():
    return pd.DataFrame({
        'learner_id': [1, 1, 2, 2, 3, 3],
        'task_id': [1, 2, 1, 2, 1, 2],
        'correct': [1, 0, 1, 0, 1, 1],
        'time_spent': [30, 45, 25, 60, 35, 40]
    })

def test_train_bkt(sample_data):
    model = train_bkt(sample_data)
    assert model is not None, "BKT model training failed"

def test_predict_bkt(sample_data):
    model = train_bkt(sample_data)
    predictions = predict_bkt(model, sample_data)
    assert not predictions.empty, "BKT predictions empty"
    assert 'correct_predictions' in predictions.columns, "Missing correct_predictions"
    assert all(0 <= predictions['correct_predictions']) and all(predictions['correct_predictions'] <= 1), "Invalid prediction values"