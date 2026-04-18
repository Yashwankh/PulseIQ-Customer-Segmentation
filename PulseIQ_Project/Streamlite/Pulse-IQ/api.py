from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# Load model & scaler
model = joblib.load("churn_model.pkl")
scaler = joblib.load("scaler.pkl")

app = FastAPI()

# Input schema
class CustomerData(BaseModel):
    Recency: float
    Frequency: float
    Monetary: float
    Total_Amount: float

# Root check
@app.get("/")
def home():
    return {"message": "Churn Prediction API is running"}

# Prediction endpoint
@app.post("/predict")
def predict(data: CustomerData):
    input_data = np.array([[ 
        data.Recency,
        data.Frequency,
        data.Monetary,
        data.Total_Amount
    ]])

    scaled = scaler.transform(input_data)
    prediction = model.predict(scaled)[0]

    return {
        "prediction": int(prediction),
        "result": "Churn" if prediction == 1 else "Not Churn"
    }
