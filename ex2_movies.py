import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title('Income by type of place')
df = pd.read_csv('https://raw.githubusercontent.com/iantonios/dsc205/refs/heads/main/CT-towns-income-census-2020.csv')

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(df)

st.markdown('---')
st.subheader('Income by the type of place')

origin = st.radio('Select type of place', ('Town', 'City', 'Borough'))

if origin == 'Town':
    df = df.loc[df['Type']=='town']
elif origin == 'City':
    df = df.loc[df['Type']=='City']
else:
    df = df.loc[df['Type']=='Borough']

fig = plt.figure()
ax = fig.add_subplot()
ax.set_xlabel('Population')
ax.hist(df['Number of Households'])
st.pyplot(fig)
