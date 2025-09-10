import sys
import os

# Dynamically add the project root to Python's path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

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
    
    if uploaded_file is not None:
        # ETL Pipeline
        df = extract_data(uploaded_file)
        if df is not None:
            df = transform_data(df)
            if load_data(df):
                st.success("Data processed successfully!")
                
                # Multi-select for models (your enhancement)
                selected_models = st.multiselect(
                    "Select Models to Evaluate", 
                    ["BKT", "Agent-Based", "Generative AI"], 
                    default=["BKT"]
                )
                
                if st.button("Evaluate and Compare") and selected_models:
                    all_results = []
                    for model_type in selected_models:
                        try:
                            result = evaluate_model(model_type, df)
                            all_results.append(result)
                        except Exception as e:
                            st.error(f"Error evaluating {model_type}: {e}")
                    
                    if all_results:
                        # Display individual results
                        for result in all_results:
                            st.write(result)
                        
                        # Affective metrics (once, since data is shared)
                        st.write(calculate_affective_metrics(df))
                        
                        # Visualize all results
                        visualize_results(all_results)
                        
                        # Display plot if exists
                        plot_path = "data/results/results_plot.png"
                        if os.path.exists(plot_path):
                            st.image(plot_path)
                        else:
                            st.warning("Plot generation failed—check console for errors.")
                        
                        # Compare models
                        comparison = compare_models(all_results)
                        st.subheader("Model Comparison (Sorted by Outcomes)")
                        st.dataframe(comparison)
                    else:
                        st.warning("No results to display. Check model evaluations.")
                elif not selected_models:
                    st.warning("Please select at least one model.")
            else:
                st.error("Failed to load processed data.")
        else:
            st.error("Failed to extract or transform data.")
    else:
        st.info("Please upload a CSV file to get started.")

if __name__ == "__main__":
    main()
