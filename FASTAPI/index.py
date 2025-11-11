from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Emotion(BaseModel):
    id: int
    name: str
    emotion: str

emotions: List[Emotion] = []

@app.get("/")
def root ():
    return{"message": "Hello"}
    
@app.get("/emotions")
def getAllEmotions():
    return emotions


@app.post("/emotion")
def addEmotion(emotion):
    emotions.append(emotion)
    print("Added")
    return emotions