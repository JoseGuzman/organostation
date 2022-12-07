import pandas as pd

def read_csv(path: str) -> pd.DataFrame:
    """
    Loads data from a CSV file
    """
    data = pd.read_csv(path)
    return data