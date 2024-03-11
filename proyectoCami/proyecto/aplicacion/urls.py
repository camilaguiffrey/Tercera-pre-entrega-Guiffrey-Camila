from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('usuario/', usuario, name="usuario"),
    path('alojamientos/', alojamiento, name="alojamiento"),
    path('review/', review, name="review"),
    #_________________________________________________ URL de cada alojamiento en especifico
    path('alojamiento/<int:alojamiento_id>/', detalle_alojamiento, name='detalle_alojamiento'),
    #_________________________________________________ URLs de los formularios
    path('nuevo_alojamiento/', nuevo_alojamiento, name="nuevo_alojamiento"),
    path('nuevo_review/', nuevo_review, name="nuevo_review"),
    path('nuevo_usuario/', nuevo_usuario, name="nuevo_usuario"),
    #_________________________________________________ URLs de la búsqueda
    path('buscar_alojamiento/', buscar_alojamiento, name="buscar_alojamiento"),
    path('encontrar_alojamiento/', encontrar_alojamiento, name="encontrar_alojamiento"),
]
