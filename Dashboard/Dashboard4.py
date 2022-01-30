import pandas as pd
import pyodbc
import numpy as np
import plotly.express as px  # pip install plotly-express
import streamlit as st  # pip install streamlit

st.set_page_config(page_title="Barcelona Accidents Distributions by Months and Days", page_icon=":bar_chart:", layout="wide")

cnxn_str = ("DRIVER={Sql Server Native Client 11.0};"
            "SERVER=DESKTOP-7HPUML6;"
            "DATABASE=MassiveInfinity;"
            "TRUSTED_CONNECTION=yes")

cnxn = pyodbc.connect(cnxn_str)

df_accidents = pd.read_sql("SELECT * FROM accidents", cnxn)

##accident distribution by month
dfam = df_accidents.groupby(['Month']).count()['Id']

barchart1 = px.bar(
    dfam,
    x=dfam.index,
    y="Id",
    title="<b>Accident Distribution by Month</b>",
)
st.plotly_chart(barchart1)

##accident distribution by day

dfaw = df_accidents.groupby(['Weekday']).count()['Id']
barchart2 = px.bar(
    dfaw,
    x=dfaw.index,
    y="Id",
    title="<b>Accident Distribution by Day</b>",
)
st.plotly_chart(barchart2)