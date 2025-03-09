import pandas as pd

def read_excel(path="./data/challenge.xlsx"):
    return pd.read_excel(path, index_col=None)