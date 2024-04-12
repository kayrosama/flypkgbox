import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SQLITE = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db/sqlite/db.sqlite3'),
    }
}

POSTGRESQL = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'nombre_base_de_datos',
        'USER': 'nombre_usuario',
        'PASSWORD': 'tu_contraseña',
        'HOST': 'localhost',  # O la dirección IP o el hostname de tu servidor de base de datos
        'PORT': '5432',       # El puerto por defecto de PostgreSQL
    }
}

MARIADB = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'hades_db',
        'USER': 'root',
        'PASSWORD': 'admin123',
        'HOST': 'localhost',  # O la dirección IP o el hostname de tu servidor de base de datos
        'PORT': '3306',       # El puerto por defecto de MariaDB
    }
}