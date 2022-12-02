# Realizar el ejercicio con yfinance
import streamlit as st
import yfinance as yf
import pandas as pd

# 1) Poner la pantalla en modo apaisado (que ocupe todo el espacio)
st.set_page_config(page_title="Ejercicio 1", layout="wide")

st.title("Gráfica con Streamlit para cotizacion en bolsa de varias empresas")

empresas = ("GOOGL", "AAPL", "TSLA", "MSFT", "NFLX")

opcion = st.selectbox("Selecciona una de estas empresas:",
                      empresas)
st.write("Has elegido: ", opcion)

años = st.slider("Numeros de años que quieres mostrar: ",
                 1, 5, 1)
st.write("Has elegido: ", años, ' años')

año_final = 2015 + años
st.write("año final: ", año_final)


# 2) Mostrar los datos de la tabla usando la opcion de streamlit dataframe

data = yf.download(opcion, "2015-1-1",
                  f"{año_final}-12-31")

st.dataframe(data)

# 3) Escoger para mostrar la tabla y el gráfico la columna 
# que quiera el usario usando un radio button

columnas = tuple(data.columns)
#columna =["Close"]
columna = st.radio(("Selecciona la columna que quieres mostrar:"), (columnas))


# 4) Visualizar la información usando plotly: 
import plotly.figure_factory as ff

data_close = data[columna]
data_close = data_close.rename_axis("Date").reset_index()

st.dataframe(data_close.head())


# Create distplot with custom bin_size
import matplotlib.pyplot as plt

#Especificando la figura a plot 
fig,ax=plt.subplots(1,1,figsize=(12,3.6),dpi=100)

# Datos
ax.plot(data_close["Date"],data_close[columna])

# Titulo
titulo = "Cotización de :" + opcion
ax.set_title(titulo, loc = "center", fontdict = {'fontsize':14, 'fontweight':'bold', 'color':'tab:blue'})

# Textos eje
ax.label_xt="Fecha"
ax.label_yt=columna

#displaying data
#st.pyplot(fig)


titulo = "Cotización de :" + opcion

import plotly.express as px


fig = px.line(data_close, x="Date", y=columna, title=titulo)

st.plotly_chart(fig, use_container_width=True)
# Plotly



