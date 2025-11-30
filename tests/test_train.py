# tests/test_train.py
import pytest
from src.train import train_model

def test_train_model_runs():
    """Smoke test: Does training finish and return a valid model?"""
    model, accuracy = train_model(n_estimators=10) # Use small N for speed
    
    assert accuracy > 0.5  # Iris is easy, accuracy should be high
    assert hasattr(model, "predict") # Check if it's a real model object
