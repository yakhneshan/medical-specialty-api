# Medical specialty classification API

This project deploys a machine learning model that predicts the medical specialty of a clinicl transcription note. The application is built using FastAPI, containerized with Docker, and deployed on Google Cloud Run. 

The model was trained using the MTSamples Medical Transcription dataset and can classify notes into medical specialities such as Surgery, Radiology, Neurology, Orthopedic, General Medicine, and Others. 

In the capstone_assignment.ipynb notebook, the model was developed and evaluated. Two different machine learning models were trained and compared:

1. TF-IDF + Logistic Regression
2. TF-IDF + Random Forest

The Logistic Regression model achieved the best overall performance and was selected for deployment. The trained model and label mappings were saved using Joblib so that predictions can be converted back into their corresponding medical specialty names.

# Running  Locally
Install dependancies: 

pip install -r requirement.txt

Naviagate to the project folder and start the API: 

uvicorn app.main:app --reload

Open:

http://localhost:8000/docs

# Docker Deployment

Before running the application with Docker, ensure Docker Desktop is installed. 

Build the Docker image:

docker build -t medical-specialty-api .

Run the container:

docker run -p 8000:8000 medical-specialty-api

Access the API:

http://localhost:8000/docs

# API Authentication 

Basic API key authentication is implemented for the prediction endpoint. The Requests must include x-api-key header. Unauthorized requests will return:

{
  "detail": "Invalid API Key"
}

# API Usage

### Endpoint

POST /predict

### Example Request

{ "text": "Radiology Report: Chest x-ray was performed. The lungs are clear." }

### Example Response 

{ "predicted_specialty": "Radiology" }

# Cloud Deployment 

The application is deployed on Google Cloud Run and can be accessed using the following URL:

https://medical-specialty-api-844084609529.us-central1.run.app/docs

# Technologies Used
Python
Scikit-Learn
FastAPI
Docker
Google Cloud Run
GitHub
Joblib
