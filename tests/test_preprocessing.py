# tests/test_preprocessing.py
import pandas as pd
import pytest
from src.preprocessing import clean_data, normalize_column

def test_clean_data_removes_nulls():
    # 1. Arrange: Create dummy dirty data
    raw_data = pd.DataFrame({
        "feature1": [1.0, 2.0, None, 4.0],
        "feature2": ["a", "b", "c", None]
    })
    
    # 2. Act: Apply the function
    clean_df = clean_data(raw_data)
    
    # 3. Assert: Check expectations
    # We expect 2 rows to be removed (index 2 and 3)
    assert len(clean_df) == 2
    assert clean_df.isnull().sum().sum() == 0

def test_normalize_column_max_is_one():
    # 1. Arrange
    df = pd.DataFrame({'test_col': [10, 20, 50, 25]})
    
    # 2. Act
    df_norm = normalize_column(df, 'test_col')
    
    # 3. Assert
    # The max value (50) should become 1.0
    assert df_norm['test_col'].max() == 1.0
    # The min value (10) should become 0.2
    assert df_norm['test_col'].min() == 0.2
