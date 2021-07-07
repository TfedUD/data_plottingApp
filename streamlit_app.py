import plotly.express as px
import streamlit as st
import pandas as pd

df = pd.read_csv('appOuts.csv')
df1= df.drop('Unnamed: 0', axis=1)





st.title('AHU I/O Node Data')

fig = px.line(df1, x='Date/Time', y=df1.columns, width=3000, height=800)

st.plotly_chart(fig)