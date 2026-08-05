import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('https://raw.githubusercontent.com/iantonios/dsc205/refs/heads/main/CT-towns-income-census-2020.csv')

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(df)

st.markdown('---')
st.subheader('Income difference')

origin = st.radio('Select Income type', ('Population', 'Median Household Income','Median Family Income'))

if origin == 'Population':
    df = df.loc[df['origin']=='Per Capita Income']
elif origin == 'Median Household Income':
    df = df.loc[df['origin']=='Median Household Income']
else:
    df = df.loc[df['origin']=='Median Family Income']

fig = plt.figure()
ax = fig.add_subplot()
ax.set_xlabel('Median household Income')
ax.hist(df['Per Capita Income'])
st.pyplot(fig)
