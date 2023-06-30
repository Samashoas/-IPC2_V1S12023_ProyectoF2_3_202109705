from django.shortcuts import *
from salas.ListaDES import *
import requests

global DES
DES = DoublyLinkedList()

def mostrar_salas(request):
    rooms = Salon('C:/Users/jpsam/OneDrive/Escritorio/Python/-IPC2_V1S12023_ProyectoF2_3_202109705/IPC2_F2/salas/Salas.xml')
    return render(request, 'salas/mostrar_salas.html', {'Salas': rooms})

def load_xmlS(request):
    if request.method == 'POST':
        rooms = Salon('C:/Users/jpsam/OneDrive/Escritorio/Python/-IPC2_V1S12023_ProyectoF2_3_202109705/IPC2_F2/salas/Salas.xml')
        response = requests.get('http://localhost:5007/getSalas')
        SALA_API = response.json()
        print(SALA_API)

        for usuarioChiquito2 in SALA_API:
            sal = Salas(
                cine=usuarioChiquito2['cine'],
                numero=usuarioChiquito2['numero'],
                asientos=usuarioChiquito2['asientos'],
            )

            rooms.insert(sal)
    
    return render(request, 'salas/mostrar_salas.html', {'Salas': rooms})