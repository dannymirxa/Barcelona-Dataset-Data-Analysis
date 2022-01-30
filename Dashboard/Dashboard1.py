import pandas as pd
import pyodbc
import matplotlib.pyplot  as plt
import matplotlib.colors as mcolors
import numpy as np
import plotly.express as px  # pip install plotly-express
import streamlit as st  # pip install streamlit



st.set_page_config(page_title="Barcelona Population, Unemployment , Accident breakdown , Immigrant breakdown by nationality", page_icon=":bar_chart:", layout="wide")

cnxn_str = ("DRIVER={Sql Server Native Client 11.0};"
            "SERVER=DESKTOP-7HPUML6;"
            "DATABASE=MassiveInfinity;"
            "TRUSTED_CONNECTION=yes")

cnxn = pyodbc.connect(cnxn_str)

df_population = pd.read_sql("SELECT * FROM population", cnxn)
df_unemployment = pd.read_sql("SELECT * FROM unemployment", cnxn)
df_accidents = pd.read_sql("SELECT * FROM accidents", cnxn)
df_immigrants_nationality = pd.read_sql("SELECT * FROM immigrants_by_nationality", cnxn)
df_immigrants_emigrants_age = pd.read_sql("SELECT * FROM immigrants_emigrants_by_age", cnxn)

##Population Breakdown by Districts
dfp = df_population.groupby(['District_Name']).sum()['Number']

pie_chart1 = px.pie(dfp,
                    title='Population Breakdown by Districts',
                    values='Number',
                    names=dfp.index)
st.plotly_chart(pie_chart1)

##Unemployment by Districts'

dfu = df_unemployment.groupby(['District_Name']).sum()['Number']

pie_chart2 = px.pie(dfu,
                    title='Unemployment by Districts',
                    values='Number',
                    names=dfu.index)

st.plotly_chart(pie_chart2)

##Accidents by Districts'
dfa = df_accidents.groupby(['District_Name']).count()['Id']
pie_chart3 = px.pie(dfa,
                    title='Accidents by Districts',
                    values='Id',
                    names=dfa.index)

st.plotly_chart(pie_chart3)

##Immigrants by Nationality

dfin = df_immigrants_nationality.groupby(['Nationality']).sum()['Number']
barchart1 = px.bar(
    dfin,
    y=dfin.index,
    x="Number",
    orientation='h',
    title="<b>Immigrants by Nationality</b>",
)
st.plotly_chart(barchart1)

dfie = df_immigrants_emigrants_age.groupby(['District Name']).sum()
fig, ax = plt.subplots(figsize=(10,5))
bar_width = 0.5
indx = np.arange(len(dfie))
barImmigrants = ax.bar(indx - bar_width/2, dfie.Immigrants, width = bar_width, color=['tab:red'], label = 'Immigrants')
barEmigrants = ax.bar(indx + bar_width/2, dfie.Emigrants, width = bar_width, color=['tab:blue'], label = 'Emigrants')
plt.title('Immigrants vs Emigrants by Districts')
#ax.set_yticks(np.arange(len(dfu)))
#for i, v in enumerate(dfie.Immigrants):
#    ax.text(v + 5, i -0.30, str(v), color='blue', fontweight='bold')
#for i, v in enumerate(dfie.Emigrants):
#    ax.text(v + 5, i -0.30, str(v), color='blue', fontweight='bold')
ax.set_xticks(indx)
ax.set_xticklabels(dfie.index, fontdict = {'fontsize' : 5})
def insert_data_labels(bars):
    for bar in bars:
        bar_height = bar.get_height()
        ax.annotate('{0:.0f}'.format(bar.get_height()),
        xy=(bar.get_x() + bar.get_width() / 2, bar_height),
        xytext=(0, 3),
        textcoords='offset points',
        ha='center',
        va='bottom'
    )

insert_data_labels(barImmigrants)
insert_data_labels(barEmigrants)

st.pyplot(fig)
