import streamlit as st
import pandas as pd

st.set_page_config(page_title="Weather Dashboard", layout="wide")
st.title("🌦️ Weather Data Analysis")
@st.cache_data
def load_data():
    df = pd.read_csv("weather_data.csv")
    return df

df = load_data()
st.sidebar.header("Filter")
min_temp = st.sidebar.slider("Min Temperature", 0, 40, 0)
filtered_df = df[df[df.columns[1]] >= min_temp]
st.write("Filtered Data", filtered_df)
st.write("### Data Preview")
st.dataframe(df.head())

st.write("### Temperature Trand")
st.line_chart(df.set_index(df.columns[0])[df.columns[1]])

st.write("### Summary")
st.write(df.describe())
