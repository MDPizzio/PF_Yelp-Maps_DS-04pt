import os
import pandas_gbq
import streamlit as st
import folium
from streamlit_folium import folium_static
import pandas as pd

# Establecer la variable de entorno con la ruta al archivo JSON de credenciales
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = ".streamlit/prctica-etl-0a6513e878e5.json"

# Configuración del proyecto de BigQuery
project_id = 'prctica-etl'  
pandas_gbq.context.project = project_id

# Definición de la consulta para el conjunto de datos de Yelp
query_1 = """
SELECT
  *
FROM
  `prctica-etl.Yelp.business` 
"""
# Cargar los datos de Yelp en un DataFrame de Pandas
df_business = pandas_gbq.read_gbq(query_1)


# Lista de columnas que deseas convertir
df_business['latitude'] = pd.to_numeric(df_business['latitude'], errors='coerce')
df_business['longitude'] = pd.to_numeric(df_business['longitude'], errors='coerce')
df_business['stars'] = pd.to_numeric(df_business['stars'], errors='coerce')
df_business['review_count'] = pd.to_numeric(df_business['review_count'], errors='coerce')

# Streamlit App
st.title("Recomendacion de locales por Estado")

st.markdown('''
Con el objetivo de atender de manera eficiente las necesidades de nuestro cliente, nos hemos propuesto anticipar las áreas de mayor crecimiento en los distintos sectores del mercado. Esta iniciativa tiene como fin identificar estratégicamente los emplazamientos más propicios para la apertura de nuevos locales.

En este sentido, hemos llevado a cabo un exhaustivo estudio que combina las valiosas opiniones de los usuarios en plataformas como Yelp, con la información proporcionada en Google Maps. Este análisis integral nos ha permitido trazar un panorama detallado de las tendencias actuales en el mercado, facilitando así la toma de decisiones informadas.
            ''')


# Sección para seleccionar el estado
estado_seleccionado_codigo = st.selectbox("Selecciona el estado", ['California', 'Delaware', 'Idaho', 'Louisiana', 'Missouri', 'Illinois'])

# Definir límites según el estado seleccionado
if estado_seleccionado_codigo == 'California':
    limites_estado = {'lat_min': 32.5, 'lat_max': 35.0, 'lon_min': -120.0, 'lon_max': -114.0}
elif estado_seleccionado_codigo == 'Delaware':
    limites_estado = {'lat_min': 38.4, 'lat_max': 39.8, 'lon_min': -75.8, 'lon_max': -75.0}
elif estado_seleccionado_codigo == 'Idaho':
    limites_estado = {'lat_min': 35.9, 'lat_max': 49.0, 'lon_min': -117.2, 'lon_max': -111.0}
elif estado_seleccionado_codigo == 'Louisiana':
    limites_estado = {'lat_min': 28.9, 'lat_max': 33.0, 'lon_min': -94.0, 'lon_max': -88.8}
elif estado_seleccionado_codigo == 'Missouri':
    limites_estado = {'lat_min': 35.9, 'lat_max': 40.6, 'lon_min': -95.8, 'lon_max': -89.1}
elif estado_seleccionado_codigo == 'Illinois':
    limites_estado = {'lat_min': 36.9, 'lat_max': 42.5, 'lon_min': -91.5, 'lon_max': -87.5}

# Filtrar el DataFrame por latitud y longitud según el estado seleccionado
df_estado_seleccionado = df_business[
    (df_business['latitude'] >= limites_estado['lat_min']) & (df_business['latitude'] <= limites_estado['lat_max']) &
    (df_business['longitude'] >= limites_estado['lon_min']) & (df_business['longitude'] <= limites_estado['lon_max'])
]

df_estado_mejores = df_estado_seleccionado[(df_estado_seleccionado['review_count'] > 0) & (df_estado_seleccionado['stars'] > 4.0)]
df_estado_mejor = df_estado_mejores.sort_values(by=['stars', 'review_count'], ascending=[True, False])

# Mostrar resultados
st.header(f"Resultados para {estado_seleccionado_codigo}")
st.table(df_estado_mejor[['name', 'categories', 'city']].head(4).reset_index(drop=True))

# Mostrar el mapa en Streamlit
st.header("Ubicaciones en el Mapa")

# Crear mapa con Folium
mapa = folium.Map(location=[df_estado_mejor['latitude'].mean(), df_estado_mejor['longitude'].mean()], zoom_start=10)

# Añadir marcadores al mapa
for index, row in df_estado_mejor.head(4).iterrows():
    folium.Marker([row['latitude'], row['longitude']], popup=row['name']).add_to(mapa)

# Mostrar mapa en la aplicación Streamlit
folium_static(mapa)