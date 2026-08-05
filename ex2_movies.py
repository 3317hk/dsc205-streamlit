import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('https://raw.githubusercontent.com/iantonios/dsc205/refs/heads/main/movies.csv')

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(df)

st.markdown('---')
st.subheader('Movies by genre of origin')

origin = st.radio('Select Genre of origin', ('Adventure', 'Children', 'Animation','Drama','Comedy','Fantasy','Crime','Action','Thriller','Horror','Romance'))

if origin == 'US':
    df = df.loc[df['origin']=='usa']
elif origin == 'Europe':
    df = df.loc[df['origin']=='europe']
else:
    df = df.loc[df['origin']=='japan']

fig = plt.figure()
ax = fig.add_subplot()
ax.set_xlabel('mpg')
ax.hist(df['mpg'])
st.pyplot(fig)
