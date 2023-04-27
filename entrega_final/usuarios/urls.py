from django.urls import path
from django.contrib.auth.views import LogoutView
from usuarios import views

app_name = 'usuarios'

urlpatterns = [
    path('iniciar_sesion/', views.iniciar_sesion, name='iniciar_sesion'),
    path('registro/', views.registro, name='registro'),
    path('perfil/editar/', views.editar_perfil, name='ver_perfil'),
    path('perfil/editar/cambiar_contrasenia', views.CambiarContrasenia.as_view(), name='cambiar_contrasenia'),
    path('cerrar_sesion/', LogoutView.as_view(template_name='usuarios/logout.html'), name='logout')
]
