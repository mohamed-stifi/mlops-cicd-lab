# src/app.py
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# 1. Define Input Schema (Data Validation)
class IrisInput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

# 2. Load Model
app = FastAPI(title="Iris Prediction API")
model = joblib.load("model.joblib")

# 3. Define Endpoint
@app.post("/predict")
def predict(data: IrisInput):
    # Convert input to numpy array
    features = np.array([[
        data.sepal_length, 
        data.sepal_width, 
        data.petal_length, 
        data.petal_width
    ]])
    
    # Make prediction
    prediction = model.predict(features)
    return {"class": int(prediction[0])}
