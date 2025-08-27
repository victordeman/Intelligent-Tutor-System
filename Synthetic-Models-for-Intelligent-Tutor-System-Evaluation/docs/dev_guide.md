# Developer Guide

## Adding a New Model

1. Create a new branch (e.g., `git checkout -b new_model`).
2. Add model code to `models/new_model/`.
3. Update `evaluation/evaluate_models.py` to include the new model.

## Extending Evaluation

- Modify `evaluation/affective_metrics.py` for new engagement metrics.
- Update `evaluation/visualize_results.py` for custom visualizations.
