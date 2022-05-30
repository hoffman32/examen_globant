# Examen_globant
Examen de proceso de globant

# Infraestructura
La herramienta se desarrollo con las siguientes tecnologias:
1) python
2) Flask
3) Pandas
4) Docker
5) Postgresql
6) Postman
7) Virtualenv

# Actividades realizadas

1) Mover data historica en formato csv a la nueva base de datos.
2) Creacion de Api service con flask para recibir nueva data.
3) Publicacion de repositorio en GitHub.
4) Csvs localizados en la /home/glbnt/csvs en el container.
5) Base de datos relacional PostgreSQL instalada en el dockerfile.
6) CSVs separados por comas importados directamente en el dockerfile.
7) API post y get publicadas con Flask.
8) Markdow de archivo README.md
9) BlindSQL injection en sentencias postgres de insercion en python.
10) Uso de Github para seguimiento de despliegue.
11) Python, SQL, DockerFile.
12) Todos los campos registrados con estructuras en PostgreSQL con DockerFile.
13) Ejercicio numero 1 del challenge 2 dispuesto en Flask con nombre metrica_1.
14) Ejercicio numero 2 del challenge 2 dispuesto en Flask con nombre metrica_2.

# Para Desplegar

ctrl+shif+p en visualstudio
terminal
-->pip install virtualenv
-->virtualenv "nombre de la carpeta del entorno virtual"

1) Montar entorno virtual.
2) Instalar dependencias de desarrollo.--> pip freeze > requirements.txt
3) Inicializar el docker build. --> docker build -t flaskapp .
4) Inicializar el contenedor --> docker run -it -p 7000:4000 -p 5432:5432 flaskapp /bin/sh
5) En container inicializar bd de postgres --> service postgresql start
6) En container inicializar Servidor flask --> python /home/glbnt/scripts/examen_globant/Scripts/servidor_flask.py

# Solicitudes en Postman

# Inserciones API POST
1) http://localhost:7000/hired_employees
json_body===
{"hired_employees":[{"name":"Jorge Salazar",
    "datetime":"2021-10-01T13:04:21Z",
    "department_id":"34",
    "job_id":"52"},
    {"name":"Angie Bejar",
    "datetime":"2021-10-22T13:04:21Z",
    "department_id":"33",
    "job_id":"55"}]}

2) http://localhost:7000/departments
json_body ===
{"departments":[{"department":"San andres"},
        {"department":"Norte de santander"}]}

3) http://localhost:7000/jobs
json_body ===
{"jobs":[{"job":"engineering"},
        {"job":"matematico"}]}

# Challenge numero 2
Ejercicio 1:http://localhost:7000/metrica_1
Ejercicio 2:http://localhost:7000/metrica_2