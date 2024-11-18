from fastapi import FastAPI
from pydantic import BaseModel
from model.model import predict

app = FastAPI()

class TextInput(BaseModel):
    text: str

class PredictionOutput(BaseModel):
    language: str

@app.get("/")
def home():
    return {'ping': "ok"}

@app.post("/predict", response_model=PredictionOutput)
def predict_language(input: TextInput):
    return {"language": predict(input.text)}