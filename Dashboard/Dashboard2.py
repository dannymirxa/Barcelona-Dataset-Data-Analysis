import pandas as pd
import pyodbc
import matplotlib.pyplot  as plt
import matplotlib.colors as mcolors
import numpy as np
import plotly.express as px  # pip install plotly-express
import streamlit as st  # pip install streamlit

st.set_page_config(page_title="Barcelona Population , Birth, Death, Unemployment by Districts", page_icon=":bar_chart:", layout="wide")

cnxn_str = ("DRIVER={Sql Server Native Client 11.0};"
            "SERVER=DESKTOP-7HPUML6;"
            "DATABASE=MassiveInfinity;"
            "TRUSTED_CONNECTION=yes")

cnxn = pyodbc.connect(cnxn_str)

df_population = pd.read_sql("SELECT * FROM population", cnxn)
df_births = pd.read_sql("SELECT * FROM births", cnxn)
df_deaths = pd.read_sql("SELECT * FROM deaths", cnxn)
df_unemployment = pd.read_sql("SELECT * FROM unemployment", cnxn)
df_immigrants_emigrants_age = pd.read_sql("SELECT * FROM immigrants_emigrants_by_age", cnxn)


##Population Breakdown by Districts
dfp = df_population.groupby(['District_Name']).sum()['Number']
##dfp = dfp.sort_values('Number')

barchart1 = px.bar(
    dfp,
    y=dfp.index,
    x="Number",
    orientation='h',
    title="<b>Population Breakdown by Districts</b>",
)
st.plotly_chart(barchart1)

##Births Breakdown by Districts
dfb = df_births.groupby(['District_Name']).sum()['Number']

barchart2 = px.bar(
    dfb,
    y=dfb.index,
    x="Number",
    orientation='h',
    title="<b>Births Breakdown by Districts</b>",
)
st.plotly_chart(barchart2)

##Deaths Breakdown by Districts
dfd = df_deaths.groupby(['District_Name']).sum()

barchart3 = px.bar(
    dfd,
    y=dfd.index,
    x="Number",
    orientation='h',
    title="<b>Deaths Breakdown by Districts</b>",
)
st.plotly_chart(barchart3)

##Unemployment Breakdown by Districts
dfu = df_unemployment.groupby(['District_Name']).sum()['Number']

barchart4 = px.bar(
    dfu,
    y=dfu.index,
    x="Number",
    orientation='h',
    title="<b>Unemployment Breakdown by Districts</b>",
)
st.plotly_chart(barchart4)