import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('./notebooks/vehicles_us.csv') 

st.header('Graficos de aununcios ventas de coches')

hist_button = st.button('Construir histograma') # crear un botón

if hist_button: # al hacer clic en el botón
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

dis_button = st.button('Construir un grafico de dispesion')
if dis_button:
    st.write('Creación de una grafica de Dispersion para el conjunto de datos de anuncios de venta de coches')
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True) 

 
  