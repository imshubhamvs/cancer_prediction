from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
import pandas as pd  # Import pandas for DataFrame creation
from fastapi.middleware.cors import CORSMiddleware

# Load the trained model and scaler
model = joblib.load('random_forest_model.joblib')
scaler = joblib.load('scaler.joblib')

# Initialize FastAPI app
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (you can specify the frontend's URL here)
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)
# Define input data structure
class CancerInput(BaseModel):
    Age: float
    Gender: int
    BMI: float
    Smoking: int
    GeneticRisk: int
    PhysicalActivity: float
    AlcoholIntake: float
    CancerHistory: int

# Column names used during training
column_names = ['Age', 'Gender', 'BMI', 'Smoking', 'GeneticRisk', 'PhysicalActivity', 'AlcoholIntake', 'CancerHistory']

# Endpoint for cancer prediction
@app.post("/predict")
def predict_cancer(data: CancerInput):
    # Prepare the input data for prediction
    input_data = np.array([[data.Age, data.Gender, data.BMI, data.Smoking, data.GeneticRisk,
                            data.PhysicalActivity, data.AlcoholIntake, data.CancerHistory]])
    
    # Convert input data to a DataFrame with the correct column names
    input_df = pd.DataFrame(input_data, columns=column_names)
    
    # Scale the input data using the loaded scaler
    scaled_input = scaler.transform(input_df)
    
    # Make prediction using the trained model
    prediction = model.predict(scaled_input)
    
    # Return the result (1 = Cancer, 0 = No Cancer)
    result = "Cancer" if prediction[0] == 1 else "No Cancer"
    return {"Prediction": result}
