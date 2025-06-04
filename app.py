import pandas as pd
import plotly.express as px
import streamlit as st
     
st.header('Análisis de venta de vehículos usados') # encabezado de la aplicación

car_data = pd.read_csv('vehicles_us.csv') # leer los datos

hist_button = st.button('Construir histograma de kilometraje') # crear un botón


if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)


# crear una casilla de verificación
build_histogram = st.checkbox('Construir evolución de precios de vehículos usados')

if build_histogram: # si la casilla de verificación está seleccionada

    st.write('Evolución de precio promedio según condición del vehículo')
    fig2 = px.histogram(car_data, x="date_posted", y="price", color='condition', title='Evolución de precios de vehículos usados')

    st.plotly_chart(fig2, use_container_width=True)