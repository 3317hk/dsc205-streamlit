import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------------------------------------
# Load the CT Census 2020 dataset
# ---------------------------------------------------------
url = "https://raw.githubusercontent.com/iantonios/dsc205/refs/heads/main/CT-towns-income-census-2020.csv"

df = pd.read_csv(url)

# Display the column names if needed for debugging
# st.write(df.columns)

# ---------------------------------------------------------
# Clean column names
# ---------------------------------------------------------
df.columns = df.columns.str.strip()

# Change these names if your CSV uses slightly different names
county_col = "County"
town_col = "Town"
income_col = "Median household income"

# Convert income to numeric
df[income_col] = (
    df['Median household income']
    .astype(str)
    .str.replace("$", "", regex=False)
    .str.replace(",", "", regex=False)
)

df[income_col] = pd.to_numeric(df[income_col], errors="coerce")

# Remove rows with missing values
df = df.dropna(subset=[county_col, town_col, income_col])

# ---------------------------------------------------------
# Streamlit title
# ---------------------------------------------------------
st.title("Connecticut Towns Census Data - 2020")

st.write(
    "Explore Connecticut cities and towns using county and "
    "median household income filters."
)

# =========================================================
# PART 1: County Selectbox
# =========================================================

st.header("Cities and Towns by County")

counties = sorted(df[county_col].unique())

selected_county = st.selectbox(
    "Select a county:",
    counties
)

county_df = df[df[county_col] == selected_county]

st.dataframe(
    county_df[[town_col, income_col]],
    width=800,
    height=200
)

# =========================================================
# PART 2: Income Slider
# =========================================================

st.header("Cities and Towns by Median Household Income")

minimum_income = int(df[income_col].min())
maximum_income = int(df[income_col].max())

income_range = st.slider(
    "Select a minimum and maximum household income:",
    min_value=minimum_income,
    max_value=maximum_income,
    value=(minimum_income, maximum_income),
    step=1000,
    format="$%d"
)

min_income, max_income = income_range

income_df = df[
    (df[income_col] >= min_income) &
    (df[income_col] <= max_income)
]

st.dataframe(
    income_df[[town_col, income_col]],
    width=800,
    height=200
)

# =========================================================
# PART 3: Top 5 and Bottom 5
# =========================================================

st.header("Highest and Lowest Median Household Income")

# Get the 5 highest-income towns
highest_5 = df.nlargest(5, income_col)

# Get the 5 lowest-income towns
lowest_5 = df.nsmallest(5, income_col)

# Combine them
top_bottom = pd.concat([lowest_5, highest_5])

# Sort for the graph
top_bottom = top_bottom.sort_values(income_col)

# ---------------------------------------------------------
# Create bar graph
# ---------------------------------------------------------

fig, ax = plt.subplots(figsize=(10, 5))

ax.bar(
    top_bottom[town_col],
    top_bottom[income_col]
)

ax.set_xlabel("City/Town")
ax.set_ylabel("Median Household Income ($)")
ax.set_title(
    "5 Cities/Towns with Highest and Lowest Median Household Income"
)

plt.xticks(rotation=45, ha="right")

plt.tight_layout()

st.pyplot(fig)
