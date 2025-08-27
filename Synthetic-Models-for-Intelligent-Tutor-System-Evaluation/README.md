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
- Dependencies listed in `docs/requirements.txt`

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/victordeman/Synthetic-Models-for-Intelligent-Tutor-System-Evaluation.git
   cd Synthetic-Models-for-Intelligent-Tutor-System-Evaluation
   ```

2. Install dependencies from root:
   ```bash
   pip install -r docs/requirements.txt
   ```

3. Run the Streamlit app from root:
   ```bash
   streamlit run ui/app.py
   ```

## Usage

1. **Upload Synthetic CSV**: Use the Streamlit interface to upload a CSV with engagement data (e.g., code submissions, errors, time spent).
2. **ETL Process**: The app runs the ETL pipeline (`src/etl/`) to process data.
3. **Select Model**: Choose BKT, Agent-Based, or Generative AI model.
4. **Evaluate**: The app evaluates the model (`evaluation/evaluate_models.py`), stores results (`data/results/`), and visualizes them (`evaluation/visualize_results.py\').
5. **Compare Models**: View performance comparisons across models.
6. **Affective Metrics**: Assess engagement metrics (e.g., frustration) via `evaluation/affective_metrics.py`.

## Hosting

The system is hosted on [Streamlit.io](https://streamlit.io) for public access. See `ui/config.toml` for configuration.

## Git Branches

- **main**: Evaluation and assessment code.
- **bkt**: Bayesian Knowledge Tracing model.
- **agent_based**: Agent-Based Models.
- **generative_ai**: Generative AI Models.

## Development

- Add model code to respective branches (`models/<model>/*`).
- Update evaluation scripts in `evaluation/`.
- See `docs/dev_guide.md` for contribution guidelines.

## License

MIT License

## Contact

Victor Deman ([GitHub](https://github.com/victordeman))
