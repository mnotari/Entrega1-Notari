from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('listar/', views.lista_objetos, name='lista_objetos'),
    path('agregar/', views.agregar_objeto, name='agregar_objeto'),
    path('buscar/', views.buscar_objetos, name='buscar_objetos'),
    path('editar/<int:pk>/', views.editar_objeto, name='editar_objeto'),
    path('eliminar/<int:pk>/', views.eliminar_objeto, name='eliminar_objeto'),
]
