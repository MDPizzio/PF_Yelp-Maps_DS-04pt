## ETL AUTOMATIZADO Y CARGA INCREMENTAL DE DATOS
<p>
La combinación de la automatización ETL y la carga incremental no solo mejora la eficiencia operativa, sino que también garantiza que la información esté siempre actualizada y disponible para la toma de decisiones en tiempo real.
</p>

## Diagrama ER
Un diagrama ER (Entidad-Relacion) es una representación visual que describe las relaciones entre diferentes entidades en un sistema de información o base de datos. Este tipo de diagrama es fundamental para modelar la estructura de una base de datos y comprender cómo las distintas entidades interactúan entre sí.

<p align="center">
    <img src="img/diagramaER.jpg" height="500">
</p>

## Procesamiento de datos
Mostraremos el esquema del tratamiento de los datos:

<p align="center">
    <img src = 'img/Workflow.png' height = '500'>
</p>

<br><br>

## Data Lake
La parte inicial de este proyecto es cargar los datos sin procesar que se nos proporcionaron y almacenarlos en nuestro Data Lake.

<p>Un Data Lake es un entorno de almacenamiento de datos que facilita la retención de grandes volúmenes de información en su formato original, sin requerir una estructuración previa. Este enfoque permite un acceso más ágil y flexible a los datos. En este contexto, optaremos por Google Cloud Storage para almacenar los datos sin procesar provenientes de fuentes como Google y Yelp.

<p align="center">
    <img src = 'img/bucket.png' height = '300'>
</p>

## Transformación de datos - Cloud Functions

El servicio Google Cloud Functions por medio de funciones se encargará de extraer los datos del Data Lake, transformarlos/limpiarlos y cargarlos en nuestro Data Warehouse.

<p>Utilizamos Cloud Functions para automatizar el proceso de ETL (Extract, Transform, Load). Las funciones almacenadas en Cloud Functions están asociadas a un disparador, el cual detecta la carga de nuevos archivos en nuestro Data Lake, encargándose de limpiar y transformar los datos sin procesar. Posteriormente, los datos procesados se almacenan en nuestro Data Warehouse.

<p>Este enfoque automatiza no solo la transformación inicial sino también la adición de nuevos datos. Una de las funciones específicas se encarga de limpiar y transformar estos nuevos datos externos, ejecutando además una consulta en Google BigQuery para actualizar la información actual en el almacén de datos.

<p align="center">
    <img src = 'img/functions.png' height = '200'>
</p>

## Data Warehouse

Google BigQuery es un servicio de Data Warehouse de Google que vamos a utilizar para almacenar y estructurar nuestros datos procesados. El Data Warehouse podrá actualizarse con los nuevos datos que ingresen mediante la automatización. 

<p align="center">
    <img src = 'img/bigquery.png' height = '350'>
</p>

## Tecnologías

- Google Cloud Storage
- Google Cloud Function
- Big Query
- Python
- Pandas

<br><br>
<p>A continuación, mostramos el funcionamiento de la carga incremental:

<p align="center">
    <video height="500" controls>
    <source src='img/VID-20240111-WA0055.mp4' type="video/mp4">
    </p>