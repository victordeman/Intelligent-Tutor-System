import matplotlib.pyplot as plt

def visualize_results(results, output_path='data/results/results_plot.png'):
    """Visualizes evaluation results."""
    df = pd.DataFrame(results)
    df.plot(x='model', y=['outcomes', 'engagement.interactions'], kind='bar')
    plt.savefig(output_path)
    plt.close()
