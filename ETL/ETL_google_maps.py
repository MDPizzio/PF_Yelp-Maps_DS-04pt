import pandas as pd
import numpy as np
import time
import os

def extraer_MISC(dato):
    if type(dato) == dict:
        if 'Accessibility' in dato:
            return dato['Accessibility']
    return []

def binario(dato):
    if type(dato) == list:
        if len(dato) > 0:
            return 1
        else:
            return 0
    else:
        return 0

inicio = time.time()#Inicia temporizador

#EXTRACCION

#Nombre de la carpeta donde estan alojados los archivos
carpeta = 'C:/Users/eduen/Desktop/PF_Yelp-Maps_DS-04pt/metadata_google'
ruta = 'ETL\metadata_google.parquet'#Ruta donde se almacena el parquet

lista_df = []

for archivo in os.listdir(carpeta):
   
    df = pd.read_json(f'{carpeta}/{archivo}', lines=True)#Carga el df
    lista_df.append(df)#Lo guarda en la lista para concatenar

df = pd.concat(lista_df, ignore_index=True)#Concatenacion de todos los df

#TRANSFORMACION
df['category'] = df['category'].astype(str)#Transformar category en string

#Eliminar duplicados por 'gmap_id'

df = df.drop_duplicates(subset='gmap_id')

#Eliminar columnas 'price', 'state', 'hours'

df = df.drop(['price', 'state', 'hours', 'relative_results', 'description',  ], axis=1)

df_reducido = df[df['category'].str.contains('restaurant|food|cafe|delivery|bar|pizza|sandwich|bakery|grill', case=False)]#Reducir el df por palabras claves


#Desintegrar el campo 'address' en 'postal_code', 'city', 'state'

#El componente nombre del string contiene comas entreveradas
df_address = df_reducido['address'].str[::-1].str.rsplit(',', expand=True)#Se invierte el string y se splitea
df_address = df_address.iloc[:, :3]#Se seleccionan las primeras 3 columnas
df_address = df_address.apply(lambda x: x.str[::-1])#Se invierte el string en cada columna
df_address.columns = ['postal_code', 'city', 'number_and_street']#Se nombran las columnas

df_reducido = pd.concat([df_reducido, df_address], axis=1)#Conctenar
df_reducido = df_reducido.drop('address', axis=1)#Eliminar columna address

#Extraer 'Accessibility' de MISC en columna 'accessibility'
df_reducido['accessibility'] = df_reducido['MISC'].apply(extraer_MISC)

#Convertir 'accessibility' en columna binaria, criterio: Si contiene datos se considera como accesible (1),
#Si no contiene datos se considera como no accesible (0)
df_reducido['accessibility'] = df_reducido['accessibility'].apply(binario)

df_reducido = df_reducido.drop('MISC', axis=1)#Eliminar columna address

#Manejo de nulos categoricos
df_reducido['name'] = df_reducido['name'].fillna('Dato desconocido')
df_reducido['category'] = df_reducido['category'].fillna('Dato desconocido')
df_reducido['url'] = df_reducido['url'].fillna('Dato desconocido')
df_reducido['postal_code'] = df_reducido['postal_code'].fillna('Dato desconocido')
df_reducido['city'] = df_reducido['city'].fillna('Dato desconocido')
df_reducido['number_and_street'] = df_reducido['number_and_street'].fillna('Dato desconocido')

#Manejo de nulos numericos
df_reducido['avg_rating'] = df_reducido['avg_rating'].fillna(0)
df_reducido['num_of_reviews'] = df_reducido['num_of_reviews'].fillna(0)

df_reducido.to_parquet(ruta)

fin = time.time()#Finaliza temporizador
tiempo_ejecucion = fin - inicio
print(f"Tiempo de ejecución: {round(tiempo_ejecucion, 2)} segundos")