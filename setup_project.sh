#!/bin/bash

# setup_project.sh
# Creates the repository structure for Synthetic-Models-for-Intelligent-Tutor-System-Evaluation
# Run from any directory: ./setup_project.sh
# Does NOT handle installations or Git pushes (manual steps)

# Define project root
PROJECT_DIR="Synthetic-Models-for-Intelligent-Tutor-System-Evaluation"
echo "Creating project structure in $PROJECT_DIR..."

# Create project directory and subdirectories
mkdir -p "$PROJECT_DIR/src/etl" \
         "$PROJECT_DIR/src/utils" \
         "$PROJECT_DIR/models/bkt" \
         "$PROJECT_DIR/models/agent_based" \
         "$PROJECT_DIR/models/generative_ai" \
         "$PROJECT_DIR/evaluation" \
         "$PROJECT_DIR/data/raw" \
         "$PROJECT_DIR/data/processed" \
         "$PROJECT_DIR/data/results" \
         "$PROJECT_DIR/ui" \
         "$PROJECT_DIR/config" \
         "$PROJECT_DIR/docs"

# Create README.md
cat << EOF > "$PROJECT_DIR/README.md"
# Synthetic Models for Intelligent Tutor System Evaluation

This project evaluates Intelligent Tutoring Systems (ITS) for Python/SQL learning using synthetic models: **Bayesian Knowledge Tracing (BKT)**, **Agent-Based Models**, and **Generative AI Models**. It focuses on **learning outcomes** (e.g., code accuracy) and **learning engagement** (e.g., interaction frequency), with engagement data driving learner simulations. The project integrates **Cognitive Load Theory (CLT)** and **Zone of Proximal Development (ZPD)** to optimize ITS performance.

## Repository Structure

- **src/**: ETL pipeline and utilities.
  - **etl/**: Extract, transform, load scripts.
  - **utils/**: Data processing and metrics.
- **models/**: Model implementations (branches: bkt, agent_based, generative_ai).
  - **bkt/**: Bayesian Knowledge Tracing.
  - **agent_based/**: Agent-Based Models.
  - **generative_ai/**: Generative AI Models.
- **evaluation/**: Model evaluation, comparison, and visualization.
- **data/**: Stores raw, processed, and result data (not tracked).
- **ui/**: Streamlit app for CSV upload and evaluation.
- **config/**: ETL configuration.
- **docs/**: User and developer guides, requirements.

## Prerequisites

- Python 3.8+
- Streamlit
- Dependencies listed in \`docs/requirements.txt\`

## Installation

1. Clone the repository:
   \`\`\`bash
   git clone https://github.com/victordeman/Synthetic-Models-for-Intelligent-Tutor-System-Evaluation.git
   cd Synthetic-Models-for-Intelligent-Tutor-System-Evaluation
   \`\`\`

2. Install dependencies from root:
   \`\`\`bash
   pip install -r docs/requirements.txt
   \`\`\`

3. Run the Streamlit app from root:
   \`\`\`bash
   streamlit run ui/app.py
   \`\`\`

## Usage

1. **Upload Synthetic CSV**: Use the Streamlit interface to upload a CSV with engagement data (e.g., code submissions, errors, time spent).
2. **ETL Process**: The app runs the ETL pipeline (\`src/etl/\`) to process data.
3. **Select Model**: Choose BKT, Agent-Based, or Generative AI model.
4. **Evaluate**: The app evaluates the model (\`evaluation/evaluate_models.py\`), stores results (\`data/results/\`), and visualizes them (\`evaluation/visualize_results.py\').
5. **Compare Models**: View performance comparisons across models.
6. **Affective Metrics**: Assess engagement metrics (e.g., frustration) via \`evaluation/affective_metrics.py\`.

## Hosting

The system is hosted on [Streamlit.io](https://streamlit.io) for public access. See \`ui/config.toml\` for configuration.

## Git Branches

- **main**: Evaluation and assessment code.
- **bkt**: Bayesian Knowledge Tracing model.
- **agent_based**: Agent-Based Models.
- **generative_ai**: Generative AI Models.

## Development

- Add model code to respective branches (\`models/<model>/*\`).
- Update evaluation scripts in \`evaluation/\`.
- See \`docs/dev_guide.md\` for contribution guidelines.

## License

MIT License

## Contact

Victor Deman ([GitHub](https://github.com/victordeman))
EOF

# Create .gitignore
cat << EOF > "$PROJECT_DIR/.gitignore"
# Data directories (not tracked)
data/raw/*
data/processed/*
data/results/*

# Python
__pycache__/
*.pyc
*.pyo
*.pyd
.Python
env/
venv/
*.egg-info/

# Streamlit
.streamlit/secrets.toml

# IDE
.vscode/
.idea/

# Misc
*.log
*.csv
*.bak
EOF

# Create src/etl/extract.py
cat << EOF > "$PROJECT_DIR/src/etl/extract.py"
import pandas as pd

def extract_data(file_path):
    """Extracts data from synthetic CSV file."""
    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        print(f"Error extracting data: {e}")
        return None
EOF

# Create src/etl/transform.py
cat << EOF > "$PROJECT_DIR/src/etl/transform.py"
from src.utils.data_processing import validate_data

def transform_data(df):
    """Transforms data for model input."""
    if df is None:
        return None
    df = validate_data(df)
    # Example: Normalize engagement metrics
    df['time_spent'] = df.get('time_spent', 0) / df['time_spent'].max()
    return df
EOF

# Create src/etl/load.py
cat << EOF > "$PROJECT_DIR/src/etl/load.py"
import os

def load_data(df, output_path='data/processed/processed_data.csv'):
    """Loads processed data to file."""
    if df is None:
        return False
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    return True
EOF

# Create src/utils/data_processing.py
cat << EOF > "$PROJECT_DIR/src/utils/data_processing.py"
def validate_data(df):
    """Validates and preprocesses engagement data."""
    required_columns = ['learner_id', 'task_id', 'correct', 'time_spent']
    if not all(col in df.columns for col in required_columns):
        raise ValueError("Missing required columns")
    return df.dropna()
EOF

# Create src/utils/metrics.py
cat << EOF > "$PROJECT_DIR/src/utils/metrics.py"
def calculate_outcomes(correct, total):
    """Calculates learning outcome metrics (e.g., accuracy)."""
    return correct / total if total > 0 else 0

def calculate_engagement(interactions, time_spent):
    """Calculates engagement metrics."""
    return {'interactions': interactions, 'avg_time': time_spent / interactions if interactions > 0 else 0}
EOF

# Create models/bkt/bkt_model.py
cat << EOF > "$PROJECT_DIR/models/bkt/bkt_model.py"
from pyBKT.models import Model

def train_bkt(data):
    """Trains Bayesian Knowledge Tracing model."""
    model = Model()
    model.fit(data=data)
    return model

def predict_bkt(model, data):
    """Predicts learner knowledge states."""
    return model.predict(data)
EOF

# Create models/bkt/simulate_bkt.py
cat << EOF > "$PROJECT_DIR/models/bkt/simulate_bkt.py"
import pandas as pd

def simulate_bkt_learner(n_tasks=10):
    """Simulates learner interactions for BKT."""
    return pd.DataFrame({
        'learner_id': [1] * n_tasks,
        'task_id': range(n_tasks),
        'correct': [0, 1, 0, 1] * (n_tasks // 4),
        'time_spent': [30, 45, 20, 50] * (n_tasks // 4)
    })
EOF

# Create models/agent_based/agent_model.py
cat << EOF > "$PROJECT_DIR/models/agent_based/agent_model.py"
class Agent:
    def __init__(self, skill_level):
        self.skill_level = skill_level

def simulate_agent(data):
    """Simulates agent-based learner behavior."""
    agent = Agent(skill_level=0.5)
    # Placeholder: Simulate responses based on skill
    return data
EOF

# Create models/agent_based/simulate_agents.py
cat << EOF > "$PROJECT_DIR/models/agent_based/simulate_agents.py"
import pandas as pd

def simulate_agents(n_learners=5, n_tasks=10):
    """Simulates multiple agent-based learners."""
    return pd.DataFrame({
        'learner_id': [i for i in range(n_learners) for _ in range(n_tasks)],
        'task_id': list(range(n_tasks)) * n_learners,
        'correct': [0, 1] * (n_learners * n_tasks // 2),
        'time_spent': [30, 45] * (n_learners * n_tasks // 2)
    })
EOF

# Create models/generative_ai/generative_model.py
cat << EOF > "$PROJECT_DIR/models/generative_ai/generative_model.py"
from transformers import pipeline

def generate_synthetic_response(prompt):
    """Generates synthetic learner responses using LLM."""
    generator = pipeline('text-generation', model='gpt2')
    return generator(prompt, max_length=50)[0]['generated_text']
EOF

# Create models/generative_ai/generate_synthetic.py
cat << EOF > "$PROJECT_DIR/models/generative_ai/generate_synthetic.py"
import pandas as pd

def generate_synthetic_data(n_tasks=10):
    """Generates synthetic learner data."""
    return pd.DataFrame({
        'learner_id': [1] * n_tasks,
        'task_id': range(n_tasks),
        'correct': [0, 1] * (n_tasks // 2),
        'time_spent': [30, 60] * (n_tasks // 2),
        'response': ['print(i' + ')' * (i % 2) for i in range(n_tasks)]  # Simulated buggy code
    })
EOF

# Create evaluation/evaluate_models.py
cat << EOF > "$PROJECT_DIR/evaluation/evaluate_models.py"
from src.utils.metrics import calculate_outcomes, calculate_engagement

def evaluate_model(model_type, data):
    """Evaluates a model against tasks."""
    outcomes = calculate_outcomes(data['correct'].sum(), len(data))
    engagement = calculate_engagement(len(data), data['time_spent'].sum())
    return {'model': model_type, 'outcomes': outcomes, 'engagement': engagement}
EOF

# Create evaluation/compare_results.py
cat << EOF > "$PROJECT_DIR/evaluation/compare_results.py"
import pandas as pd

def compare_models(results):
    """Compares performance across models."""
    df = pd.DataFrame(results)
    return df.sort_values(by='outcomes', ascending=False)
EOF

# Create evaluation/visualize_results.py
cat << EOF > "$PROJECT_DIR/evaluation/visualize_results.py"
import matplotlib.pyplot as plt

def visualize_results(results, output_path='data/results/results_plot.png'):
    """Visualizes evaluation results."""
    df = pd.DataFrame(results)
    df.plot(x='model', y=['outcomes', 'engagement.interactions'], kind='bar')
    plt.savefig(output_path)
    plt.close()
EOF

# Create evaluation/affective_metrics.py
cat << EOF > "$PROJECT_DIR/evaluation/affective_metrics.py"
def calculate_affective_metrics(data):
    """Calculates affective engagement metrics (e.g., frustration)."""
    frustration = (data['time_spent'] > 60).mean()  # Example: Long pauses indicate frustration
    return {'frustration': frustration}
EOF

# Create ui/app.py
cat << EOF > "$PROJECT_DIR/ui/app.py"
import streamlit as st
from src.etl.extract import extract_data
from src.etl.transform import transform_data
from src.etl.load import load_data
from evaluation.evaluate_models import evaluate_model
from evaluation.compare_results import compare_models
from evaluation.visualize_results import visualize_results
from evaluation.affective_metrics import calculate_affective_metrics

def main():
    st.title("Synthetic Models for ITS Evaluation")
    uploaded_file = st.file_uploader("Upload Synthetic CSV", type="csv")
    if uploaded_file:
        df = extract_data(uploaded_file)
        df = transform_data(df)
        load_data(df)
        model_type = st.selectbox("Select Model", ["BKT", "Agent-Based", "Generative AI"])
        if st.button("Evaluate"):
            results = evaluate_model(model_type, df)
            st.write(results)
            st.write(calculate_affective_metrics(df))
            visualize_results([results])
            st.image("data/results/results_plot.png")

if __name__ == "__main__":
    main()
EOF

# Create ui/config.toml
cat << EOF > "$PROJECT_DIR/ui/config.toml"
[server]
headless = true
port = 8501
enableCORS = false

[theme]
primaryColor = "#F63366"
backgroundColor = "#FFFFFF"
secondaryBackgroundColor = "#F0F2F6"
textColor = "#262730"
EOF

# Create config/etl_config.yaml
cat << EOF > "$PROJECT_DIR/config/etl_config.yaml"
input_columns:
  - learner_id
  - task_id
  - correct
  - time_spent
output_path: data/processed/processed_data.csv
EOF

# Create docs/user_guide.md
cat << EOF > "$PROJECT_DIR/docs/user_guide.md"
# User Guide

## Running the Streamlit App

1. Install dependencies:
   \`\`\`bash
   pip install -r docs/requirements.txt
   \`\`\`

2. Run the app from root:
   \`\`\`bash
   streamlit run ui/app.py
   \`\`\`

3. Upload a synthetic CSV, select a model, and evaluate.

## CSV Format

- Columns: learner_id, task_id, correct, time_spent, response (optional)
- Example: See \`data/synthetic/sample_learner_data.csv\`
EOF

# Create docs/dev_guide.md
cat << EOF > "$PROJECT_DIR/docs/dev_guide.md"
# Developer Guide

## Adding a New Model

1. Create a new branch (e.g., \`git checkout -b new_model\`).
2. Add model code to \`models/new_model/\`.
3. Update \`evaluation/evaluate_models.py\` to include the new model.

## Extending Evaluation

- Modify \`evaluation/affective_metrics.py\` for new engagement metrics.
- Update \`evaluation/visualize_results.py\` for custom visualizations.
EOF

# Create docs/requirements.txt
cat << EOF > "$PROJECT_DIR/docs/requirements.txt"
pandas
numpy
pyBKT
transformers
streamlit
matplotlib
pyyaml
EOF

echo "Project structure created successfully in $PROJECT_DIR!"
