from src.utils.metrics import calculate_outcomes, calculate_engagement
from models.bkt.bkt_model import train_bkt, predict_bkt
from models.agent_based.simulate_agents import simulate_agents
from models.generative_ai.generative_model import simulate_generative

def evaluate_model(model_type, data):
    """Evaluates a model against tasks."""
    if data.empty:
        print(f"{model_type} evaluation: Empty input data")
        return {'model': model_type, 'outcomes': 0.0, 'engagement': {'interactions': 0, 'avg_time': 0.0}}
    
    if model_type == "BKT":
        try:
            bkt_model = train_bkt(data)
            predictions = predict_bkt(bkt_model, data)
            outcomes = predictions['correct_predictions'].mean() if not predictions.empty else 0.0
            print(f"BKT outcomes: {outcomes}")
        except Exception as e:
            print(f"BKT evaluation error: {str(e)}")
            outcomes = 0.0
    elif model_type == "Agent-Based":
        try:
            sim_data = simulate_agents(data)
            print(f"Agent-Based sim_data correct: {sim_data['correct'].tolist()}")
            outcomes = calculate_outcomes(sim_data['correct'].sum(), len(sim_data))
            print(f"Agent-Based outcomes: {outcomes}")
        except Exception as e:
            print(f"Agent-Based evaluation error: {str(e)}")
            outcomes = 0.0
    else:
        try:
            sim_data = simulate_generative(data)
            outcomes = sim_data['score'].mean() if not sim_data.empty else 0.0
            print(f"Generative AI outcomes: {outcomes}")
        except Exception as e:
            print(f"Generative AI evaluation error: {str(e)}")
            outcomes = 0.0
    
    engagement = calculate_engagement(len(data), data['time_spent'].sum())
    return {'model': model_type, 'outcomes': outcomes, 'engagement': engagement}