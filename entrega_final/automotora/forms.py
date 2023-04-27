from django import forms
from .models import Automovil
from ckeditor.widgets import CKEditorWidget

class AutomovilForm(forms.ModelForm):
    class Meta:
        model = Automovil
        fields = ['marca','modelo','anio', 'precio','descripcion', 'url_imagen']
        labels = {
            'marca' : 'Marca',
            'modelo' : 'Modelo',
            'anio'   : 'Anio',
            'precio' : 'Precio',
            'descripcion': 'Descripción',
            'imagen' : 'Imagen'
            
        }
        widgets = {
            'descripcion': forms.CharField(widget=CKEditorWidget())
         }