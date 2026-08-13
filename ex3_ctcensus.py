import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data
url = "https://raw.githubusercontent.com/iantonios/dsc205/refs/heads/main/CT-towns-income-census-2020.csv"

df = pd.read_csv(url)

# Convert median household income from text to numbers
df["Median household income"] = (
    df["Median household income"]
    .astype(str)
    .str.replace("$", "", regex=False)
    .str.replace(",", "", regex=False)
    .str.strip()
)

df["Median household income"] = pd.to_numeric(
    df["Median household income"],
    errors="coerce"
)

# --------------------------------------------------
# TITLE
# --------------------------------------------------

st.title("Connecticut Towns Census Data - 2020")

# --------------------------------------------------
# COUNTY SELECTBOX
# --------------------------------------------------

st.header("Cities and Towns by County")

counties = sorted(df["County"].unique())

selected_county = st.selectbox(
    "Select a county:",
    counties
)

county_data = df[df["County"] == selected_county]

st.dataframe(
    county_data[["Place", "Median household income"]],
    width=800,
    height=200
)

# --------------------------------------------------
# INCOME SLIDER
# --------------------------------------------------

st.header("Cities and Towns by Median Household Income")

minimum = int(df["Median household income"].min())
maximum = int(df["Median household income"].max())

income_range = st.slider(
    "Select a minimum and maximum income:",
    min_value=minimum,
    max_value=maximum,
    value=(minimum, maximum),
    step=1000,
    format="$%d"
)

min_income = income_range[0]
max_income = income_range[1]

filtered_data = df[
    (df["Median household income"] >= min_income)
    &
    (df["Median household income"] <= max_income)
]

st.dataframe(
    filtered_data[["Place", "Median household income"]],
    width=800,
    height=200
)

# --------------------------------------------------
# TOP 5 AND BOTTOM 5
# --------------------------------------------------

st.header("5 Highest and 5 Lowest Median Household Incomes")

lowest_5 = df.nsmallest(
    5,
    "Median household income"
)

highest_5 = df.nlargest(
    5,
    "Median household income"
)

bar_data = pd.concat([
    lowest_5,
    highest_5
])

# --------------------------------------------------
# BAR GRAPH
# --------------------------------------------------

fig, ax = plt.subplots(figsize=(10, 5))

ax.bar(
    bar_data["Place"],
    bar_data["Median household income"]
)

ax.set_xlabel("City/Town")
ax.set_ylabel("Median Household Income ($)")

ax.set_title(
    "5 Highest and 5 Lowest Median Household Income"
)

plt.xticks(
    rotation=45,
    ha="right"
)

plt.tight_layout()

st.pyplot(fig)
