from fastapi import FastAPI
import joblib
import numpy as np

# Load the trained model
model = joblib.load("model.joblib")

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the ML API!"}

@app.post("/predict")
def predict(features: list):
    # Convert the input list to a numpy array
    features_array = np.array(features).reshape(1, -1)
    
    # Predict using the trained model
    prediction = model.predict(features_array)
    
    return {"prediction": prediction.tolist()}
