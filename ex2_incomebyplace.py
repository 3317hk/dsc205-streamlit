import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

st.title("Income by type of place")

df = pd.read_csv(
    "https://raw.githubusercontent.com/iantonios/dsc205/refs/heads/main/CT-towns-income-census-2020.csv"
)

if st.checkbox("Show raw data"):
    st.subheader("Raw data")
    st.write(df)

st.markdown("---")
st.subheader("Income by the type of place")

origin = st.radio(
    "Select type of place",
    ("Town", "City", "Borough")
)


df = df.loc[df["Type"] == origin]


fig, ax = plt.subplots()

ax.set_xlabel("Per Capita Income")
ax.set_ylabel("Number of Places")

ax.hist(df["Per capita income"].str.replace("$", "").str.replace(",", "").astype(float))

st.pyplot(fig)
