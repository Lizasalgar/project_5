import pandas as pd
import plotly.express as px
import streamlit as st
import altair.vegalite.v4 as alt

st.header('Análisis del conjunto de datos de anuncios de venta de autos, mediante la construcción de un histograma y un gráfico de dispersión')
        
car_data = pd.read_csv('vehicles_us.csv') # leer los datos
hist_button = st.button('Construir histograma') # crear un botón
disp_button = st.button('Construir gráfico de dispersión') # crear otro botón
       
if hist_button: # al hacer clic en el botón
            # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de autos')
            
            # crear un histograma
    fig = px.histogram(car_data, x="odometer")
        
            # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
    
if disp_button: # al hacer clic en el botón
            # escribir un mensaje
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de autos')
            
            # crear un gráfico de dispersión
    fig = px.scatter(car_data, x="odometer", y="price")
        
            # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
    
    