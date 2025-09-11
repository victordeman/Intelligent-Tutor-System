from pyBKT.models import Model
import pandas as pd

def train_bkt(data):
    """Trains a Bayesian Knowledge Tracing model."""
    if data.empty:
        raise ValueError("Input data is empty")
    
    print("BKT train input:", data.head())
    bkt_data = data.rename(columns={'learner_id': 'user_id', 'task_id': 'skill_name'})
    if 'skill_name' not in bkt_data.columns:
        bkt_data['skill_name'] = bkt_data['user_id'].astype(str) + '_' + bkt_data['task_id'].astype(str)
    
    print("BKT train columns:", bkt_data.columns.tolist())
    try:
        model = Model(seed=42, num_fits=1)
        model.fit(data=bkt_data)
        print("BKT model trained successfully")
        return model
    except Exception as e:
        print(f"BKT training failed: {str(e)}")
        raise RuntimeError(f"BKT training failed: {str(e)}")

def predict_bkt(model, data):
    """Predicts learner knowledge states and returns probabilities."""
    if data.empty or model is None:
        print("BKT predict: Empty data or model")
        return pd.DataFrame()
    
    print("BKT predict input:", data.head())
    bkt_data = data.rename(columns={'learner_id': 'user_id', 'task_id': 'skill_name'})
    if 'skill_name' not in bkt_data.columns:
        bkt_data['skill_name'] = bkt_data['user_id'].astype(str) + '_' + bkt_data['task_id'].astype(str)
    
    try:
        predictions = model.predict(data=bkt_data)
        print("BKT prediction columns:", predictions.columns.tolist())
        print("BKT predictions:", predictions.head())
        # Use 'correct_predictions' (probability of correct response)
        if 'correct_predictions' in predictions.columns:
            return predictions[['user_id', 'skill_name', 'correct_predictions']]
        else:
            print("BKT warning: 'correct_predictions' not in output")
            return pd.DataFrame()
    except Exception as e:
        print(f"BKT prediction failed: {str(e)}")
        return pd.DataFrame()