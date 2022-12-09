# PROYECTO INDIVIDUAL DE DATA ENGINEERING

<p align=center><img src=https://d31uz8lwfmyn8g.cloudfront.net/Assets/logo-henry-white-lg.png><p>
  
## **Introducción**
La idea de este proyecto, es situarse en el rol de un ***Data Engineer***.

El proyecto consiste en realizar una ingesta de datos de diferentes extensiones, como *csv* o *json*. Luego se realiza un EDA (Exploratory Data Analysis) en cada dataset, para luego aplicar las transformaciones mediante funciones, en este caso, eliminación de duplicados y tratamiento de datos nulos.
  
  Luego disponibilizamos los datos limpios y relacionamos los datasets para su consulta a través de una API (Application Programming Interface), ésta es una interfaz que permite que dos aplicaciones se comuniquen entre sí, independientemente de la infraestructura subyacente. Esta API esta construida en un entorno virtual dockerizado.

## Tecnologías 

Para la elaboración de este proyecto se utilizó principalmente **Python** con las siguiente librerías: 
- *Jupyter* - Interfaz 
- *Pandas* - Para manipulación de datos
- *Pathlib* - Para gestión de path 
  
Para la elaboración y ejecución de la API:
- *Docker* - 
- *FastAPI* - Framework
  
## Consultas a realizar:

- Máxima duración según tipo de film (película/serie), por plataforma y por año.
  
     Request: *get_max_duration(año, plataforma, [min o season])*

- Cantidad de películas y series (separado) por plataforma.
  
     Request: *get_count_plataform(plataforma)*  
  
- Cantidad de veces que se repite un género y plataforma con mayor frecuencia del mismo.
  
     Request: *get_listedin('genero')*

- Actor que más se repite según plataforma y año.
  
    Request: *get_actor(plataforma, año)*

