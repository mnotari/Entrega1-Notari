from django import forms
from .models import Objeto

class ObjetoForm(forms.ModelForm):
    class Meta:
        model = Objeto
        fields = ['nombre','tamanio','peso','descripcion']
        labels = {
            'nombre' : 'Nombre',
            'tamanio' : 'Tamaño',
            'peso'   : 'Peso',
            'descripcion': 'Descripción'
        }
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 3}),
        }
