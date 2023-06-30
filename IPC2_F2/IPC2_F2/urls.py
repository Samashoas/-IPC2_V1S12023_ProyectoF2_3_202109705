"""
URL configuration for IPC2_F2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from usuarios.views import *
from peliculas.views import*
from salas.views import*
from tarjetas.views import*

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', mostrar_usuario, name='mostrar_usuario'),
    path('usuarios/cargar_xml', load_xml, name='load_xml'),
    path('peliculas/', mostrar_peliculas, name='mostrar_peliculas'),
    path('peliculas/cargar_xml', load_xmlP, name='load_xmlP'),
    path('salas/', mostrar_salas, name='mostrar_salas'),
    path('salas/cargar_xml', load_xmlS, name='load_xmlS'),
    path('tarjetas/', mostrar_tarjeta, name='mostrar_tarjeta'),
    path('tarjetas/cargar_xml', load_xmlT, name='load_xmlT'),
]
