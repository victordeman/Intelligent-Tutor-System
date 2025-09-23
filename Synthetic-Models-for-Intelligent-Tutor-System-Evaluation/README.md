# Synthetic Models for Intelligent Tutor System Evaluation

This project evaluates Intelligent Tutoring Systems (ITS) for Python/SQL learning using synthetic models: **Bayesian Knowledge Tracing (BKT)**, **Agent-Based Models**, and **Generative AI Models**. It focuses on **learning outcomes** (e.g., code accuracy) and **learning engagement** (e.g., interaction frequency), with engagement data driving learner simulations. The project integrates **Cognitive Load Theory (CLT)** and **Zone of Proximal Development (ZPD)** to optimize ITS performance.

## Repository Structure
```
Synthetic-Models-for-Intelligent-Tutor-System-Evaluation/
├── src/                            # Core scripts for ETL and utilities
│   ├── etl/                       # ETL pipeline components
│   │   ├── extract.py             # Extracts data from synthetic CSV
│   │   ├── transform.py           # Transforms data for model input
│   │   └── load.py                # Loads processed data for evaluation
│   └── utils/                     # Utility functions
│       ├── data_processing.py     # Data preprocessing and validation
│       └── metrics.py             # Learning outcomes and engagement metrics
├── models/                         # Model implementations
│   ├── bkt/                       # Bayesian Knowledge Tracing
│   │   ├── bkt_model.py           # BKT model definition and training
│   │   └── simulate_bkt.py        # Simulate learner interactions with BKT
│   ├── agent_based/               # Agent-Based Models
│   │   ├── agent_model.py         # Agent model definition
│   │   └── simulate_agents.py     # Simulate agent-based learner interactions
│   ├── generative_ai/             # Generative AI Models
│   │   ├── generative_model.py    # Generative AI model definition
│   │   └── generate_synthetic.py  # Generate synthetic learner data
├── evaluation/                     # Evaluation and comparison code
│   ├── evaluate_models.py         # Evaluates models against tasks
│   ├── compare_results.py         # Compares performance across models
│   ├── visualize_results.py       # Visualizes data and results
│   └── affective_metrics.py       # Affective engagement metrics (e.g., frustration)
├── data/                           # Data storage (not tracked)
│   ├── raw/                       # Raw synthetic CSV files
│   ├── processed/                 # Processed data for models
│   └── results/                   # Evaluation results
├── ui/                             # Streamlit user interface
│   ├── app.py                     # Streamlit app for CSV upload and evaluation
│   └── config.toml                # Streamlit configuration
├── config/                         # Configuration files
│   └── etl_config.yaml            # ETL pipeline configuration
├── docs/                           # Documentation
│   ├── user_guide.md              # User instructions for running the app
│   ├── dev_guide.md               # Developer guide for extending the project
│   └── requirements.txt           # Project dependencies
├── README.md                       # Project overview and setup instructions
└── .gitignore                      # Git ignore file
```

## Prerequisites

- Python 3.8+
- Streamlit
- Dependencies listed in `docs/requirements.txt`

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/victordeman/Intelligent-Tutor-System.git
   cd Synthetic-Models-for-Intelligent-Tutor-System-Evaluation
   ```

2. Install dependencies from root:
   ```bash
   pip install -r docs/requirements.txt
   ```

3. Run the Streamlit app from root:
   ```bash
  
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
