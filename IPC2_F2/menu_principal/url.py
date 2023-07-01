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
    path('registro/', registro, name='registro'),
    path('login/IndexAdmin/', IndexAdmin, name="IndexAdmin"),
    path('login/IndexAdmin/usuarios/', mostrar_usuario, name='mostrar_usuario'),
    path('login/IndexAdmin/usuarios/cargar_xml', load_xml, name='load_xml'),
    path('login/IndexAdmin/peliculas/', mostrar_peliculas, name='mostrar_peliculas'),
    path('login/IndexAdmin/peliculas/cargar_xml', load_xmlP, name='load_xmlP'),
    path('login/IndexAdmin/salas/', mostrar_salas, name='mostrar_salas'),
    path('login/IndexAdmin/salas/cargar_xml', load_xmlS, name='load_xmlS'),
    path('login/IndexAdmin/tarjetas/', mostrar_tarjeta, name='mostrar_tarjeta'),
    path('login/IndexAdmin/tarjetas/cargar_xml', load_xmlT, name='load_xmlT'),
]
