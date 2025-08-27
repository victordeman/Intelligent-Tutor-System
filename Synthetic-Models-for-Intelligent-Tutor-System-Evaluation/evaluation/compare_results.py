import pandas as pd

def compare_models(results):
    """Compares performance across models."""
    df = pd.DataFrame(results)
    return df.sort_values(by='outcomes', ascending=False)
