# User Guide

## Running the Streamlit App

1. Install dependencies:
   ```bash
   pip install -r docs/requirements.txt
   ```

2. Run the app from root:
   ```bash
   streamlit run ui/app.py
   ```

3. Upload a synthetic CSV, select a model, and evaluate.

## CSV Format

- Columns: learner_id, task_id, correct, time_spent, response (optional)
- Example: See `data/synthetic/sample_learner_data.csv`
