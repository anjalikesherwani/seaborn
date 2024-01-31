import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('practice.csv')

st.write(df)
st.write(df.describe())

a = plt.figure(figsize=(4,4))
plt.boxplot(df['island'])
st.pyplot(a)


arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

st.pyplot(fig)