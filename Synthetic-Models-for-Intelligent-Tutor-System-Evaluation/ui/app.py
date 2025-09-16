from flask import Flask, request, jsonify, send_from_directory
import os
import pandas as pd
from src.etl.extract import extract_data
from src.etl.transform import transform_data
from src.etl.load import load_data
from evaluation.evaluate_models import evaluate_model
from evaluation.affective_metrics import calculate_affective_metrics
from evaluation.visualize_results import visualize_results

app = Flask(__name__, static_folder='frontend/public', template_folder='frontend/public')

# Serve the HTML frontend
@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')

# Serve static files (CSS, JS, etc.)
@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory(app.static_folder, path)

# Serve result files (e.g., plots)
@app.route('/data/results/<path:filename>')
def serve_results(filename):
    return send_from_directory('data/results', filename)

# API endpoint for CSV upload and model evaluation
@app.route('/api/evaluate', methods=['POST'])
def evaluate():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    
    file = request.files['file']
    model_type = request.form.get('model', 'BKT')
    
    # Save uploaded file temporarily
    upload_path = 'data/raw/uploaded_data.csv'
    os.makedirs(os.path.dirname(upload_path), exist_ok=True)
    file.save(upload_path)
    
    # Process data through ETL pipeline
    df = extract_data(upload_path)
    if df is None:
        return jsonify({'error': 'Invalid CSV file'}), 400
    
    df = transform_data(df)
    if df is None:
        return jsonify({'error': 'Data transformation failed'}), 400
    
    load_data(df, 'data/processed/processed_data.csv')
    
    # Evaluate model
    results = evaluate_model(model_type, df)
    affective_metrics = calculate_affective_metrics(df)
    
    # Generate visualization
    visualize_results([results], output_path='data/results/results_plot.png')
    
    # Prepare response
    response = {
        'model': model_type,
        'outcomes': results['outcomes'],
        'engagement': results['engagement'],
        'affective': affective_metrics,
        'plot': '/data/results/results_plot.png'
    }
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)