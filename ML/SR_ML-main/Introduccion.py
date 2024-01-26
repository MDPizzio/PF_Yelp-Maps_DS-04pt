import os
import pandas_gbq
import streamlit as st
from streamlit_folium import folium_static
import folium

st.title("PROYECTO GRUPAL - Google Maps & Yelp")

# Cargar la imagen
imagen_url = "https://github.com/mpereyro/PF_Yelp-Maps_DS-04pt/raw/main/img/logo%20merydian.jpeg"
st.markdown(
    f'<div style="display: flex; justify-content: center;"><img src="{imagen_url}" alt="Centrando una Imagen"></div>',
    unsafe_allow_html=True
)

st.markdown('## Introducción')

st.markdown('''
Como parte de una consultora de data, nos han contratado para poder realizar un análisis del mercado estadounidense. 
Nuestro cliente es parte de un conglomerado de empresas desean tener un análisis detallado de la opinión de los usuarios en Yelp y cruzarlos con los de Google Maps.
Además, desean saber dónde es conveniente emplazar los nuevos locales de restaurantes y afines, y desean poder tener un sistema de recomendación de restaurantes para los usuarios para darles por ejemplo la posibilidad de poder conocer nuevos sabores basados en sus experiencias previas.
            
            ''')

st.markdown('## Alcance de datos')

st.markdown('''
Con el objetivo de diversificar los datos en función a los Estados, seleccionamos los mismos siguiendo el criterio de los tres Estados que posean mayor PBI per cápita y los tres Estados que posean menor PBI per cápita, verificando disponer de datos suficientes sobre los mismos en ambas fuentes.           
            ''')

# Crear un mapa centrado en los Estados Unidos
m = folium.Map(location=[37.0902, -95.7129], zoom_start=4)

# Definir coordenadas y colores para los estados
states = {
    'California': {'coordinates': [36.7783, -119.4179], 'color': 'green'},
    'Delaware': {'coordinates': [38.9108, -75.5277], 'color': 'green'},
    'Idaho': {'coordinates': [44.0682, -114.7420], 'color': 'blue'},
    'Louisiana': {'coordinates': [30.9843, -91.9623], 'color': 'blue'},
    'Missouri': {'coordinates': [37.9643, -91.8318], 'color': 'blue'},
    'Illinois': {'coordinates': [40.6331, -89.3985], 'color': 'green'}
}

# Crear un mapa con folium
m = folium.Map(location=[36.7783, -119.4179], zoom_start=5)

# Marcar los estados en el mapa con nombres e iniciales
for state, info in states.items():
    folium.Marker(
        location=info['coordinates'],
        tooltip=f"{state} ({state[:2]})",
        icon=folium.Icon(color=info['color'])
    ).add_to(m)

# Mostrar el mapa en Streamlit
st.header("Estados en el Mapa")
folium_static(m)