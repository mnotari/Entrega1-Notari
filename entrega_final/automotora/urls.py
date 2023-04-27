from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('acerca_de/', views.acerca_de, name='acerca_de'),
    path('automoviles/', views.lista_Automoviles, name='lista_Automoviles'),
    path('automoviles/agregar/', views.agregar_Automovil, name='agregar_Automovil'),
    path('automoviles/buscar/', views.buscar_Automoviles, name='buscar_Automoviles'),
    path('automoviles/detalles/<int:pk>/', views.detalle_Automovil.as_view(), name='detalle_Automovil'),
    path('automoviles/editar/<int:pk>/', views.editar_Automovil.as_view(), name='editar_Automovil'),
    path('automoviles/eliminar/<int:pk>/', views.eliminar_Automovil, name='eliminar_Automovil'),
]
