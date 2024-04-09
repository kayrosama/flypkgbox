# flypkgbox
Exportacion - Importacion

Control y Tracking de documentos, paquetes y cajas.

# Instalando el Sistema

El proyecto atendera la necesidad de aplicar controles y tracking de los documentos, paqueteria y cajas que son exportadas e importadas.

# Instaladores

| Nombre                   | Instalador                                                                                                                                                                                                                     |
|:-------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `Compilador`             | [Python3](https://www.python.org/downloads/release/python-396/ "Python3")                                                                                                                                                      |
| `IDE de programación`    | [Visual Studio Code](https://code.visualstudio.com/ "Visual Studio Code"), [Sublime Text](https://www.sublimetext.com/ "Sublime Text") |
| `Motor de base de datos` | [Sqlite Studio](https://github.com/pawelsalawa/sqlitestudio/releases "Sqlite Studio"), [PostgreSQL](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads "PostgreSQL"), [MariaDB](https://mariadb.org "MariaDB") |
| `DevOps` | [Docker](https://www.docker.com "Docker"), [DockerHub](https://hub.docker.com "DockerHub") |


# Pasos de instalación

##### 1) Descomprimir el proyecto en una carpeta de tu sistema operativo

##### 2) Crear un entorno virtual para posteriormente instalar las librerias del proyecto

Para Linux:

```bash
python3 -m venv .venv/flypkgbox
```

##### 3) Instalando y configurando el complemento de [weasyprint](https://weasyprint.org/ "weasyprint")

Linux - Instalar las [librerias](https://doc.courtbouillon.org/weasyprint/stable/first_steps.html#linux "librerias") correspondientes a la distribución que tenga instalado en su computador y/o imagen Docker.

##### 4) Activando el entorno virtual del proyecto

Para Linux:

```bash
source .venv/flypkgbox/bin/active
```

##### 6) Creando tablas del sistema

```bash
python manage.py migrate
```

##### 9) Iniciando el servicio

```bash
python manage.py runserver 0:8000 o python manage.py runserver 0.0.0.0:8000
```

------------

#  Gracias 

**Colaboradores**
gschama

***KSM***

