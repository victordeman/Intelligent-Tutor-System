import pandas as pd
import random
import ast
import sqlparse

def generate_response(correct_response, error_rate=0.3):
    """Generates a synthetic learner response with potential errors."""
    if random.random() < error_rate:
        # Introduce errors based on response type
        if 'print' in correct_response:  # Python
            errors = [
                correct_response.replace('(', ''),  # Missing parenthesis
                correct_response.replace("'", '"'),  # Wrong quotes
                correct_response + ';',  # Extra semicolon
            ]
            return random.choice(errors)
        elif 'SELECT' in correct_response.upper():  # SQL
            errors = [
                correct_response.replace('*', ''),  # Missing *
                correct_response.replace('FROM', 'FORM'),  # Typo
                correct_response + ' WHERE'  # Incomplete clause
            ]
            return random.choice(errors)
    return correct_response

def evaluate_response(response, correct_response):
    """Evaluates the quality of a generated response (0–1)."""
    try:
        if 'print' in correct_response:  # Python
            ast.parse(response)
            return 1.0 if response == correct_response else 0.8  # Partial credit for syntax
        elif 'SELECT' in correct_response.upper():  # SQL
            sqlparse.parse(response)
            return 1.0 if response == correct_response else 0.7  # Partial credit for syntax
    except (SyntaxError, sqlparse.exceptions.SQLParseError):
        return 0.0  # Invalid syntax
    return 0.5  # Fallback for unexpected cases

def simulate_generative(data):
    """Simulates generative AI learner responses."""
    if data.empty:
        return pd.DataFrame()
    
    results = []
    for _, row in data.iterrows():
        correct_response = row['response']
        generated_response = generate_response(correct_response)
        score = evaluate_response(generated_response, correct_response)
        results.append({
            'learner_id': row['learner_id'],
            'task_id': row['task_id'],
            'generated_response': generated_response,
            'score': score
        })
    sim_data = pd.DataFrame(results)
    print("Generative AI sim_data:", sim_data.head())
    return sim_data