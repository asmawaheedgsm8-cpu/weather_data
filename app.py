import streamlit as st
import pandas as pd

st.set_page_config(page_title="Weather Dashboard", layout="wide")
st.title("🌦️ Weather Data Analysis")

df = pd.read_csv("Weather Data.csv")

st.write("### Data Preview")
st.dataframe(df.head())

st.write("### Temperature Trand")
st.line_chart(df.set_index(df.columns[0])[df.columns[1]])

st.write("### Summary")
st.write(df.describe())
