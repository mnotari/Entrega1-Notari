from django.db import models
from ckeditor.fields import RichTextField


class Automovil(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    anio = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = RichTextField()
    fecha_ingreso = models.DateField(auto_now=True, auto_now_add=False)
    url_imagen = models.ImageField(upload_to='media', null=True, blank=True)

    def __str__(self):
        return f"{self.modelo} - {self.marca}"