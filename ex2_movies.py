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

# Match the exact casing in your CSV ('town', 'City', 'Borough')
origin = st.radio("Select type of place", ("town", "City", "Borough"))

# Filter using the matching case
df_filtered = df.loc[df["Type"] == origin]

fig, ax = plt.subplots()
ax.set_xlabel("Type")
# Use a numeric or categorical column for the histogram, or bar chart if counting
ax.hist(df_filtered["Per Capita Income"])  # Assuming you want to plot income
st.pyplot(fig)
