import os
import pandas_gbq
import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import folium
from streamlit_folium import folium_static

# Establecer la variable de entorno con la ruta al archivo JSON de credenciales
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = ".streamlit/prctica-etl-0a6513e878e5.json"

# Configuración del proyecto de BigQuery
project_id = 'prctica-etl'  
pandas_gbq.context.project = project_id

# Definición de la consulta para el conjunto de datos de GMaps
query_1 = """
SELECT
  *
FROM
  `prctica-etl.Yelp.business` 
"""

query_2 = """
SELECT
  business_id, stars, useful, funny, cool, text, feeling
FROM
  `prctica-etl.Yelp.Reviews`  
LIMIT 10000
"""


# Cargar los datos de Yelp en un DataFrame de Pandas
df_business = pandas_gbq.read_gbq(query_1)
df_reviews = pandas_gbq.read_gbq(query_2)
#st.table(df_business.head(100))  # Muestra la tabla en Streamlit

df_business['latitude'] = pd.to_numeric(df_business['latitude'], errors='coerce')
df_business['longitude'] = pd.to_numeric(df_business['longitude'], errors='coerce')

def user_recommender(business_id= str):#Ingresa el id de negocio calificado por el usuario
    umbral_calificacion = 3 #Se considera bien calificado al local con un puntaje mayor a 3
    rango_error = 2 #Rango error latitud
    local_calificado = df_business[df_business.business_id == business_id]#local de referencia del usuario
    reviews = df_reviews[['business_id','stars','useful', 'funny', 'cool', 'text', 'feeling']].copy()#Accede a las columnas de reviews
    reviews = pd.merge(df_reviews, df_business[['business_id', 'city', 'state', 'categories', 'latitude', 'longitude']], how='right',on='business_id')#Se hace un merge de los datos de reviews con datos relevantes de business para el modelo de ML
    review_max = reviews[reviews.business_id == business_id]#Selecciona las reviews del local
    review_max = review_max.sort_values(by='stars', ascending=False)#Las ordena con el fin de acceder a la mas alta
    reviews = reviews[reviews.state == local_calificado.state.iloc[0]]#Selecciona locales del mismo estado
    reviews = reviews[(reviews.latitude.astype(float) >=
                                                float(local_calificado.latitude.iloc[0]) - rango_error) & 
                                                (reviews.latitude.astype(float) <= 
                                                 float(local_calificado.latitude.iloc[0]) + rango_error)]
    reviews = reviews[(reviews.longitude.astype(float) >=
                                                float(local_calificado.longitude.iloc[0]) - rango_error) & 
                                                (reviews.longitude.astype(float) <= 
                                                 float(local_calificado.longitude.iloc[0]) + rango_error)]
    reviews = reviews[reviews.business_id != business_id]#Selecciona locales del mismo estado
    reviews = pd.concat([review_max.iloc[0].to_frame().T, reviews], ignore_index=True)#La review mas alta del local se ubica en la primera fila del df
    reviews = reviews.head(5000)#Limita el df a 5000 entradas (Se puede limitar en la query de acceso)
    reviews = reviews.astype(str)#Transforma todos los datos del df a str

    #Vectorizar todo el df por filas
    vectorizer = TfidfVectorizer(binary=True)
    X = vectorizer.fit_transform(reviews.apply(lambda x: ' '.join(x), axis=1))
    columnas = vectorizer.get_feature_names_out()
    reviews_vectorizado = pd.DataFrame(X.toarray(), columns=columnas)

    #Calcular similitud entre la fila 0 (nuestra unidad de referencia) y el resto de las filas
    referencia = reviews_vectorizado.iloc[0].values.reshape(1, -1)
    similitud = cosine_similarity(referencia, reviews_vectorizado)
    similitud_serie = pd.Series(similitud[0], index=reviews.index)#Se le asignan los indices de el df original a la matriz de similitudes
    resultado = reviews.loc[similitud_serie.nlargest(50).index]#Se seleccionan los primeros resultados (Margen para trabajar resultados de locales repetidos), la primera fila siempre es la de referencia
    
    #Armado de resultado
    id_array = resultado.business_id.iloc[1:]#Se obtiene un array con los 'business_id' del resultado ignorando la posicion 0 (referencia)
    filas_seleccionadas = df_business[df_business.business_id.isin(id_array)]#Se seleccionan las filas del df business que coincidan con los ID
    filas_seleccionadas = filas_seleccionadas[filas_seleccionadas.stars.astype(float) > umbral_calificacion]#Se seleccionan las filas cuyo puntaje 'stars' este por encima del umbral (para ignorar locales con baja calificacion)
    

    return filas_seleccionadas.head().reset_index(drop=True) #devuelve el df con los primeros 5 resultados

st.title("Sistema de Recomendación de Usuarios")
st.markdown('''
La función de recomendación utiliza las reseñas y características de negocios para ofrecer a los usuarios sugerencias adaptadas a sus preferencias individuales. La combinación de técnicas de procesamiento de texto y similitud de contenido permite identificar y recomendar negocios que comparten similitudes con aquellos que un usuario ya ha calificado positivamente. Este enfoque proporciona una experiencia de recomendación personalizada, aprovechando tanto la información del usuario como las características específicas de los elementos recomendados.
            ''')

import streamlit as st

# Crear un expansor (expander) para las especificaciones
with st.expander("Especificaciones de la función"):
    # Contenido escondido dentro del expansor
    st.write("""
    **BIBLIOTECAS UTILIZADAS:**
    - Pandas
    - Scikit-Learn
    
    **DESCRIPCIÓN:**
    Se define una función llamada “user_recommender” la cual toma como parámetro el business_id de un local calificado por el usuario y realiza recomendaciones de otros locales similares en función de los parámetros mencionados en la descripción del código:
    
    **Preprocesamiento de Datos:**
    - Se selecciona el local de referencia (local_calificado) del dataframe df_business basándose en el business_id proporcionado.
    - Se extraen las columnas relevantes de reseñas (df_reviews) y se realiza un merge con información importante de negocios (df_business).
    
    **Filtrado por Ubicación:**
    - Se filtran las reseñas para incluir solo locales del mismo estado que el local de referencia.
    - Se aplica un filtro adicional para restringir los locales basándose en la latitud y longitud dentro de un rango de error predefinido.
    
    **Vectorización de texto y cálculo de similitud:**
    - Se utiliza la técnica TF-IDF (Term Frequency-Inverse Document Frequency) para vectorizar el texto de las reseñas junto con los metadatos y convertirlo en características numéricas.
    - Se calcula la similitud de coseno entre la primera fila (local de referencia) y todas las demás filas vectorizadas.
    
    **Selección de Resultados:**
    - Se seleccionan los locales más similares en función de la similitud de coseno.
    - Se filtran los resultados basándose en el umbral de calificación establecido para descartar establecimientos con bajo puntaje.
    
    **Armado y Retorno del Resultado:**
    - Se construye un dataframe de resultados cruzando los índices de filas tanto de la matriz de similitud, como el dataframe vectorizado y el dataframe de reviews descartando siempre la primera fila de referencia.
    - Se extraen las business_id de los primeros resultados arrojados descartando el primer elemento correspondiente a la fila de referencia.
    - Se extraen los datos de locales del dataframe ‘business’ a partir del array de identificadores obtenido en el punto anterior.
    - Se devuelven 5 filas diferentes con los establecimientos sugeridos.
    """)

# Sección para ingresar el ID de negocio
business_id_input = st.text_input("Ingresa el ID de negocio:")

# Botón para ejecutar la recomendación
if st.button("Obtener Recomendaciones"):
    if business_id_input:
        try:
            # Ejecutar la función user_recommender con el ID ingresado
            recomendaciones = user_recommender(business_id_input)

            # Mostrar los resultados en Streamlit
            st.header("Resultados de Recomendación:")
            st.table(recomendaciones[['name','business_id', 'address', 'city', 'stars', 'categories']])

            # Crear un mapa con folium
            m = folium.Map(location=[recomendaciones['latitude'].mean(), recomendaciones['longitude'].mean()], zoom_start=12)

            # Agregar marcadores al mapa
            for index, row in recomendaciones.iterrows():
                folium.Marker(location=[row['latitude'], row['longitude']], popup=row['name']).add_to(m)

            # Mostrar el mapa en Streamlit
            st.header("Ubicaciones en el Mapa")
            folium_static(m)



        except Exception as e:
            st.error(f"Ocurrió un error: {str(e)}")
    else:
        st.warning("Por favor, ingresa un ID de negocio.")