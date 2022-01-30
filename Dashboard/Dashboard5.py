import pandas as pd
import pyodbc
import numpy as np
import plotly.express as px  # pip install plotly-express
import streamlit as st  # pip install streamlit

st.set_page_config(page_title="Barcelona Bus Stops", page_icon=":bar_chart:", layout="wide")

cnxn_str = ("DRIVER={Sql Server Native Client 11.0};"
            "SERVER=DESKTOP-7HPUML6;"
            "DATABASE=MassiveInfinity;"
            "TRUSTED_CONNECTION=yes")

cnxn = pyodbc.connect(cnxn_str)

df_bus_stops = pd.read_sql("SELECT * FROM bus_stops", cnxn)


df_bus_stops = df_bus_stops.rename(columns={'Latitude': 'latitude', 'Longitude': 'longitude'})

#px.set_mapbox_access_token(open(".mapbox_token").read())
#print(df_bus_stops[['latitude', 'longitude']])
st.map(df_bus_stops[['latitude', 'longitude']])

# fig = px.scatter_mapbox(df_bus_stops,
#                         lat='latitude',
#                         lon='longitude',
#                         color="Bus_Stop")
# st.plotly_chart(fig)
# fig.show()