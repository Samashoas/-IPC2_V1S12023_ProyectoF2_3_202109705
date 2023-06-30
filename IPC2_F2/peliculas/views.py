from django.shortcuts import *
from peliculas.ListaDE import *
import requests

global DE
DE = DoublyCircularLinkedList()

def mostrar_peliculas(request):
    filmes = Es_cine('C:/Users/jpsam/OneDrive/Escritorio/Python/-IPC2_V1S12023_ProyectoF2_3_202109705/IPC2_F2/peliculas/Pelis.xml')
    return render(request, 'peliculas/mostrar_pelis.html', {'Peliculas': filmes})

def load_xmlP(request):
    if request.method == 'POST':
        filmes = Es_cine('C:/Users/jpsam/OneDrive/Escritorio/Python/-IPC2_V1S12023_ProyectoF2_3_202109705/IPC2_F2/peliculas/Pelis.xml')
        response = requests.get('http://localhost:5007/getPelis')
        PELI_API = response.json()
        print(PELI_API)

        for usuarioChiquito2 in PELI_API:
            peli = Movie(
                categoria=usuarioChiquito2['Categoria'],
                titulo=usuarioChiquito2['titulo'],
                director=usuarioChiquito2['director'],
                anio=usuarioChiquito2['anio'],
                fecha=usuarioChiquito2['fecha'],
                hora=usuarioChiquito2['hora'],
                imagen=usuarioChiquito2['imagen'],
                precio= usuarioChiquito2['precio']
            )

            filmes.insert(peli)
    
    return render(request, 'peliculas/mostrar_pelis.html', {'Peliculas': filmes})