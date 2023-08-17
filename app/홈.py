import streamlit as st
import pandas as pd

df = pd.read_csv("./power_sum.csv")

def pre(a):
    return "{:02d}".format(a)

df["월"] = df["월"].apply(pre)
df["일"] = df["일"].apply(pre)
df["날짜"] = "22"+ df["월"] + df["일"]
df.drop(columns=["월","일"],inplace=True)
st.image("https://cdn.lecturernews.com/news/photo/201811/9102_22180_354.jpg")


col1,col2 = st.columns([1,1])
with col1:
    st.line_chart(df,x="날짜")
with col2:
    st.dataframe(df)