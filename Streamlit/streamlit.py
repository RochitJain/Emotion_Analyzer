import streamlit as st
import requests
import pandas as pd
st.title("Emotion Analyzer")


BACKEND = st.sidebar.text_input("Backend URL", "")
name = st.text_input("Enter your name")
age = st.text_input("Enter your age")
journal = st.text_area("How are you feeling?")

if st.button("Submit") :
    payload = {"text": journal, "name": name}
    res= requests.post("http://127.0.0.1:8000/emotion", json=payload)
    if(res.status_code == 200):
        st.write(f"Hello {name},{age} your entry is submitted")
    else :
        print(res.status_code)

if st.button("Get All Emotions"):
    res = requests.get("http://127.0.0.1:8000/emotions")
    if res.status_code == 200:
        entries = res.json()
        if entries : 
            df = pd.DataFrame(entries)
            df['created_at'] = pd.to_datetime(df['created_at'],utc=True, errors='coerce')
            df['polarity'] = pd.to_numeric(df['polarity'], errors='coerce')
            # df = df.sort_values('created_at')
            # df = df.set_index('created_at')
            # st.write("Columns:", list(df.columns))
            st.subheader("Recent entries")
            st.dataframe(df.head(20))

            # simple weekly trend: average polarity per day
            # df_trend = df.set_index('created_at').resample('D').polarity.mean().fillna(0)
            # st.subheader("Daily average polarity (trend)")
            # st.line_chart(df_trend)

