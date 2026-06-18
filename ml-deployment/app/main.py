from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI()

model = joblib.load("app/winning_model.joblib")
id2label = joblib.load("app/id2label.joblib")

class MedicalNote(BaseModel):
    text: str

@app.get("/")
def home():
    return {"message": "Medical Specialty Prediction API"}

@app.post("/predict")
def predict(note: MedicalNote):

    prediction_id = model.predict([note.text])[0]

    prediction_label = id2label[prediction_id]

    return {
        "predicted_specialty": prediction_label
    }