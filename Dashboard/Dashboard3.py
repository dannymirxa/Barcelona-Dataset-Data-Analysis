import pandas as pd
import pyodbc
import matplotlib.pyplot  as plt
import matplotlib.colors as mcolors
import numpy as np
import plotly.express as px  # pip install plotly-express
import streamlit as st  # pip install streamlit
import altair as alt

st.set_page_config(page_title="Barcelona Average Life Expectancy by Districts", page_icon=":bar_chart:", layout="wide")

cnxn_str = ("DRIVER={Sql Server Native Client 11.0};"
            "SERVER=DESKTOP-7HPUML6;"
            "DATABASE=MassiveInfinity;"
            "TRUSTED_CONNECTION=yes")
cnxn = pyodbc.connect(cnxn_str)

df_life_expectancy = pd.read_sql(
    'SELECT p.District_Name, '
    '[Neighborhood], '
    '[2006-2010], '
    '[2007-2011], '
    '[2008-2012], '
    '[2009-2013], '
    '[2010-2014], '
    'le.[Gender] '
    'FROM [MassiveInfinity].[dbo].[life_expectancy] le '
    'right join population p '
    'on le.Neighborhood = p.Neighborhood_Name ', cnxn)

df_life_expectancy = df_life_expectancy.fillna(value=np.nan)

df_life_expectancy.Neighborhood.fillna(value='Unknown', inplace=True)

df_life_expectancy['2006-2010'].fillna(df_life_expectancy['2006-2010'].mean(), inplace=True)
df_life_expectancy['2007-2011'].fillna(df_life_expectancy['2007-2011'].mean(), inplace=True)
df_life_expectancy['2008-2012'].fillna(df_life_expectancy['2008-2012'].mean(), inplace=True)
df_life_expectancy['2009-2013'].fillna(df_life_expectancy['2009-2013'].mean(), inplace=True)
df_life_expectancy['2010-2014'].fillna(df_life_expectancy['2010-2014'].mean(), inplace=True)

dfle = df_life_expectancy.groupby(['District_Name']).mean()

dfle = dfle.T
dfle['Year']=dfle.index.str.slice(5, 9)
dfle = dfle.melt(['Year'], var_name='District', value_name='Average_Expectancy')
# dfle = dfle.melt()
# c = alt.Chart(dfle).mark_line().encode(
#      x='District', y='Average_Expectancy')

# st.altair_chart(c, use_container_width=True)
print(dfle)
# st.line_chart(dfle)

all_stock_prices = px.line(data_frame=dfle,
    x='Year', y='Average_Expectancy',color='District',
    title="Average Life Expectancy by Districts over Year"
    )

st.plotly_chart(all_stock_prices)
