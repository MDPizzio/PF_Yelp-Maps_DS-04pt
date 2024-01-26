# Marchine Learning - Sistema de Recomendación

Bienvenido a la documentación de la aplicación Streamlit. Esta aplicación utiliza Streamlit para crear una interfaz web interactiva para describir brevemente la funcionalidad.

<img src = 'SR_ML-main\img\streamlit.PNG'>

## Estructura del proyecto

Descripción breve de la estructura del proyecto y el propósito de cada carpeta/archivo.

- Archivos:

    Introduccion.py: El archivo principal que contiene la lógica de la aplicación Streamlit.

    requirements.txt: Lista de dependencias necesarias para ejecutar la aplicación.

    id_business: Contiene id para probar el Sistema de Recomendacion de Usuarios

- Carpetas:

    /pages: Contiene las pestaas creadas para cada Sistema de Recomendacion.

    /sist_venv: Es el sistema de entorno virtual creado para trabajar con streamlit.

    /.streamlit: Contiene los archivos necesarios para correr la app.

# Feature Engineering

### BIBLIOTECAS UTILIZADAS:

- Pandas
- Scikit-Learn

### DESCRIPCIÓN: 
Se define una función llamada “user_recommender” la cual toma como parámetro el business_id de un local calificado por el usuario y realiza recomendaciones de otros locales similares en función de los parámetros mencionados en la descripción del código:

### Preprocesamiento de Datos:

Se selecciona el local de referencia (local_calificado) del dataframe df_business basándose en el business_id proporcionado.
Se extraen las columnas relevantes de reseñas (df_reviews) y se realiza un merge con información importante de negocios (df_business).

### Filtrado por Ubicación:

Se filtran las reseñas para incluir solo locales del mismo estado que el local de referencia.
Se aplica un filtro adicional para restringir los locales basándose en la latitud y longitud dentro de un rango de error predefinido.

### Vectorización de texto y cálculo de similitud:

Se utiliza la técnica TF-IDF (Term Frequency-Inverse Document Frequency) para vectorizar el texto de las reseñas junto con los metadatos y convertirlo en características numéricas.
Se calcula la similitud de coseno entre la primera fila (local de referencia) y todas las demás filas vectorizadas.

### Selección de Resultados:

Se seleccionan los locales más similares en función de la similitud de coseno.
Se filtran los resultados basándose en el umbral de calificación establecido para descartar establecimientos con bajo puntaje.

### Armado y Retorno del Resultado:

Se construye un dataframe de resultados cruzando los índices de filas tanto de la matriz de similitud, como el dataframe vectorizado y el dataframe de reviews descartando siempre la primera fila de referencia.
Se extraen las business_id de los primeros resultados arrojados descartando el primer elemento correspondiente a la fila de referencia.
Se extraen los datos de locales del dataframe ‘business’ a partir del array de identificadores obtenido en el punto anterior.
Se devuelven 5 filas diferentes con los establecimientos sugeridos.

# Enlace a la aplicación

👉    https://introduccionpy-3pyggfyo28jwp9xovgawgb.streamlit.app/
