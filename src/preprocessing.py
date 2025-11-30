# src/preprocessing.py
import pandas as pd

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Removes rows with missing values and resets index.
    """
    df_clean = df.dropna().reset_index(drop=True)
    return df_clean

def normalize_column(df: pd.DataFrame, col_name: str) -> pd.DataFrame:
    """Divides a column by its maximum value."""
    # Avoid Division by Zero edge case in real life, but kept simple for now
    if df[col_name].max() != 0:
        df[col_name] = df[col_name] / df[col_name].max()
    return df
