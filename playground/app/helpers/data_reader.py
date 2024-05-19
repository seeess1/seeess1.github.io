import pandas as pd

def read_data_csv(filename):
    """
    Read data from a CSV file, clean up column names, and return a pandas DataFrame.
    """
    df = pd.read_csv(filename)
    
    # Clean up column names
    df.columns = df.columns.str.strip().str.title().str.replace('_', ' ')

    return df
