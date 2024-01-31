import streamlit as st
import pandas as pd

df = pd.read_csv('practice'.csv)

st.write(df)
st.write(df.describe())