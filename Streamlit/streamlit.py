import streamlit as st
import requests
st.title("Emotion Analyzer")

name = st.text_input("Enter your name")
age = st.text_input("Enter your age")
emotion = st.text_input("How are you feeling?")

if st.button("Submit") :
    st.write(f"Hello {name} your emotion {emotion} is submitted")
    data = requests.get("http://127.0.0.1:8000") #random data from fastapi
    st.write(data.json())


