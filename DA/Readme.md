# Data Analytics

## Contexto

Para esta fase, se llevó a cabo el siguiente procedimiento con los datos: se almacenaron los archivos en Cloud Storage, se ejecutó el proceso de ETL de forma automatizada mediante Cloud Functions y, por último, se guardaron las bases de datos resultantes en BigQuery. Finalmente, nos encontramos en la etapa de análisis de los datos, donde se presentará el EDA y un Dashboard interactivo realizado con Looker Studio.


<p align = 'center'>
<img src = img/sprint3.PNG height = '400'>
</p>

Recordamos una vez más que el alcance de nuestros datos, obtenidos de las plataformas Google Maps y Yelp, se limita a los sectores gastronómicos, abordando los 3 estados con el PBI per cápita más alto (California, Illinois y Delaware) y los 3 con el PBI per cápita más bajo (Misuri, Idaho y Luisiana), en un intervalo que abarca los años 2018 a 2021.

## Objetivo

Enfocándonos en las necesidades específicas de las empresas del rubro gastronómico interesadas en mejorar la experiencia de sus usuarios, nuestro dashboard proporciona una visión detallada de los puntos clave que influyen en la calidad de los servicios ofrecidos. Con un total de 5 KPIs seleccionados, destacamos aquellos aspectos críticos que demandan atención y acción por parte de los gestores y propietarios de estos establecimientos.

- Aumentar mensualmente el porcentaje de negocios con valoraciones de 4-5 estrellas.
- Alcanzar mensualmente una tasa de respuesta al usuario de mínimo el 80%.
- Incrementar la participación de los usuarios en un 5% de manera trimestral.
- Incrementar mensualmente la cantidad de check-in en un 5%.
- Incrementar un 30% trimestral la cantidad de comentarios positivos.

## Dashboard
Nuestro dashboard no solo presenta información relevante y oportuna, sino que también se posiciona como una herramienta poderosa para impulsar la toma de decisiones informadas y estratégicas en el sector gastronómico, permitiendo a las empresas identificar áreas de mejora y optimización para satisfacer las demandas y expectativas de sus clientes de manera efectiva.

La elección de la plataforma Google Cloud para nuestro proyecto se basó en su capacidad para integrar de manera eficiente los datos almacenados en el data warehouse de BigQuery con Looker Studio. Esta integración nos permitió aprovechar un entorno unificado para el análisis y la visualización de datos, lo que resultó fundamental para la coherencia y la eficacia de nuestro trabajo.

Para una presentación más clara y organizada de los KPIs seleccionados, dividimos nuestro dashboard en dos páginas, cada una diseñada para mostrar los indicadores relevantes dentro de diferentes intervalos de tiempo.

En la primera página, nos enfocamos en los intervalos de tiempo mensuales:

En la segunda página, nos centramos en la presentación de los indicadores de manera trimestral:




