from pyexpat import model
from django.db import models

class Objeto(models.Model):
    nombre = models.CharField(max_length=100)
    tamanio = models.CharField(max_length=100)
    peso = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha = models.DateField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.nombre