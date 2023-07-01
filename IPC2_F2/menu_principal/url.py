from django.contrib import admin
from django.urls import path, include
from usuarios.views import *
from peliculas.views import*
from salas.views import*
from tarjetas.views import*
from menu_principal.views import*

urlpatterns = [
    path('', index, name="index"),
    path('login/', login, name='login'),
    path('usuarios/', mostrar_usuario, name='mostrar_usuario'),
    path('usuarios/cargar_xml', load_xml, name='load_xml'),
    path('peliculas/', mostrar_peliculas, name='mostrar_peliculas'),
    path('peliculas/cargar_xml', load_xmlP, name='load_xmlP'),
    path('salas/', mostrar_salas, name='mostrar_salas'),
    path('salas/cargar_xml', load_xmlS, name='load_xmlS'),
    path('tarjetas/', mostrar_tarjeta, name='mostrar_tarjeta'),
    path('tarjetas/cargar_xml', load_xmlT, name='load_xmlT'),
]
