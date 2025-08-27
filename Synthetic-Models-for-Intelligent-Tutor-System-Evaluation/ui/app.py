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
