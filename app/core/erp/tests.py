from django.test import TestCase
from config.wsgi import *
from core.erp.models import Type

# Listar

# select * from tabla
query = Type.objects.all()
print(query)