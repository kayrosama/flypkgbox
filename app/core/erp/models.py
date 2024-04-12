from django.db import models
from datetime import datetime

class Employee(models.Model):
    names = models.CharField(max_length=150, verbose_name='Nombres')
    dpi = models.CharField(max_length=13, unique=True, verbose_name='DPI')
    date_joined = models.DateField(default=datetime.now, verbose_name='fecha de registro')
    date_creation = models.DateTimeField(auto_now=True)
    date_updated = models.DateTimeField(auto_now_add=True)
    age = models.PositiveIntegerField(default=0)
    salary = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    state = models.BooleanField(default=True)
    gender = models.CharField(max_length=50)
    avatar = models.ImageField(upload_to='avatar/%y/%m/%d', null=True, blank=True)
    cvitae = models.FileField(upload_to='cvitae/%y/%m/%d', null=True, blank=True)
    
    def __str__(self):
        return self.names
    
    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        db_table = 'empleado'
        ordering = ['id']
