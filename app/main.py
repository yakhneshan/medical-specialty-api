from fastapi import FastAPI, HTTPException, Header
from pydantic import BaseModel
import joblib

app = FastAPI()

model = joblib.load("app/winning_model.joblib")
id2label = joblib.load("app/id2label.joblib")

API_KEY = "seneca2026"

class MedicalNote(BaseModel):
    text: str

@app.get("/")
def home():
    return {"message": "Medical Specialty Prediction API"}

@app.post("/predict")
def predict(
    note: MedicalNote,
    x_api_key: str = Header(None)
):
     if x_api_key != API_KEY:
        raise HTTPException(
            status_code=401,
            detail="Invalid API Key"
        )
     prediction_id = model.predict([note.text])[0]
     
     prediction_label = id2label[prediction_id]
     
     return {
        "predicted_specialty": prediction_label
    }