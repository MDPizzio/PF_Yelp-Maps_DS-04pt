# Data Analytics

## Contexto

Para esta fase, se llevó a cabo el siguiente procedimiento con los datos: se almacenaron los archivos en Cloud Storage, se ejecutó el proceso de ETL de forma automatizada mediante Cloud Functions y, por último, se guardaron las bases de datos resultantes en BigQuery. Finalmente, nos encontramos en la etapa de análisis de los datos, donde se presentará el EDA y un Dashboard interactivo realizado con Looker Studio.


<p align = 'center'>
<img src = img/sprint3.PNG height = '400'>
</p>

Recordamos una vez más que el alcance de nuestros datos, obtenidos de las plataformas Google Maps y Yelp, se limita a los sectores gastronómicos, abordando los 3 estados con el PBI per cápita más alto (California, Illinois y Delaware) y los 3 con el PBI per cápita más bajo (Misuri, Idaho y Luisiana), en un intervalo que abarca los años 2018 a 2021.

## Objetivo

En esta etapa tenemos como objetivo presentar nuestros datos en un Dashboard interactivo, donde se podrán visualizar aquellas características relevantes para la toma de decisiones de nuestros clientes, y los indicadores clave de rendimiento (KPIs):

- Aumentar mensualmente el porcentaje de negocios con valoraciones de 4-5 estrellas.
- Alcanzar mensualmente una tasa de respuesta al usuario de mínimo el 80%.
- Incrementar la participación de los usuarios en un 5% de manera trimestral.
- Incrementar mensualmente la cantidad de check-in en un 5%.
- Aumentar mensualmente la cantidad de negocios en áreas desabastecidas en un 1%.
