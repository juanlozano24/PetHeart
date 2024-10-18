from django.urls import path
from . import views

urlpatterns = [
    path('registrar-mascota/', views.registrar_mascota, name='registrar_mascota'),
    path('registrar-ayuda/', views.registrar_ayuda, name='registrar_ayuda'),
    path('directorio-mascota', views.directorio_mascota, name='directorio_mascota'),
    path('', views.index, name='index'),
]
