import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


url = "https://raw.githubusercontent.com/iantonios/dsc205/refs/heads/main/CT-towns-income-census-2020.csv"

df = pd.read_csv(url)


df["Median household income"] = (
    df["Median household income"]
    .str.replace("$", "")
    .str.replace(",", "")
    .astype(int)
)

st.title("Connecticut Town Census Data")



st.header("Cities and Towns by County")

county = st.selectbox(
    "Select a county:",
    df["County"].unique()
)

county_data = df[df["County"] == county]

st.dataframe(
    county_data[["Place", "Median household income"]],
    width=800,
    height=200
)



st.header("Cities and Towns by Income")

income = st.slider(
    "Select income range:",
    int(df["Median household income"].min()),
    int(df["Median household income"].max()),
    (
        int(df["Median household income"].min()),
        int(df["Median household income"].max())
    )
)

income_data = df[
    (df["Median household income"] >= income[0]) &
    (df["Median household income"] <= income[1])
]

st.dataframe(
    income_data[["Place", "Median household income"]],
    width=800,
    height=200
)



st.header("5 Highest and 5 Lowest Median Household Incomes")

lowest = df.nsmallest(5, "Median household income")
highest = df.nlargest(5, "Median household income")

graph_data = pd.concat([lowest, highest])

plt.figure(figsize=(10, 5))

plt.bar(
    graph_data["Place"],
    graph_data["Median household income"]
)

plt.xlabel("City/Town")
plt.ylabel("Median Household Income")
plt.xticks(rotation=45)

plt.tight_layout()

st.pyplot(plt)
