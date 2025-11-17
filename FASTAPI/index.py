from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from sqlite import insert,view
from textblob import TextBlob
app = FastAPI()

# # init_db()
class Emotion(BaseModel):
    text: str
    name: str

emotions: List[Emotion] = []


def textblob_sentiment (text):
    blob = TextBlob(text)
    polarity = round(blob.sentiment.polarity,4)
    subjectivity = round(blob.sentiment.subjectivity,4)
    if polarity >= 0.3 : 
        emotion = "Positive"
    elif polarity <= -0.3 :
        emotion = "Negative"
    else :
        emotion = "Neutral"
    return {"polarity": polarity, "subjectivity": subjectivity, "emotion": emotion}

@app.get("/")
def root ():
    return{"message": "Hello"}
    
@app.get("/emotions")
def getAllEmotions():
    data= view()
    return data


@app.post("/emotion")
def addEmotion(entry: Emotion):
    text = entry.text
    sentiment = textblob_sentiment(text)
    data = insert(entry.name, sentiment,text)
    # print("Added")
    # return view()
    return data
