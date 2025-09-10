import pandas as pd
import matplotlib.pyplot as plt
import os

def visualize_results(results, output_path='data/results/results_plot.png'):
    """Visualizes evaluation results."""
    if not results:
        print("No results to visualize.")
        return
    
    df = pd.DataFrame(results)
    # Flatten engagement for plotting (extract interactions)
    if 'engagement' in df.columns and isinstance(df['engagement'].iloc[0], dict):
        df['interactions'] = df['engagement'].apply(lambda x: x.get('interactions', 0))
    
    # Plot outcomes and interactions (drop engagement column if present)
    plot_df = df[['model', 'outcomes', 'interactions']].copy()
    plot_df.plot(x='model', y=['outcomes', 'interactions'], kind='bar', title='Model Evaluation: Outcomes vs Interactions')
    plt.xlabel('Model')
    plt.ylabel('Metrics')
    plt.legend()
    
    # Ensure output directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.savefig(output_path)
    plt.close()
    print(f"Plot saved to {output_path}")
