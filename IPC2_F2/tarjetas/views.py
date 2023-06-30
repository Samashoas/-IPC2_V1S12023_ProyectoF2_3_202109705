from django.shortcuts import *
from tarjetas.ListaDES import *
import requests

global LE
LE = DoublyLinkedList()

def mostrar_tarjeta(request):
    cards = Trade_card('C:/Users/jpsam/OneDrive/Escritorio/Python/-IPC2_V1S12023_ProyectoF2_3_202109705/IPC2_F2/tarjetas/Tarjetas.xml')
    return render(request, 'tarjetas/mostrar_card.html', {'Tarjeta': cards})

def load_xmlT(request):
    if request.method == 'POST':
        cards = Trade_card('C:/Users/jpsam/OneDrive/Escritorio/Python/-IPC2_V1S12023_ProyectoF2_3_202109705/IPC2_F2/tarjetas/Tarjetas.xml')
        response = requests.get('http://localhost:5007/getTarjetas')
        USER_API = response.json()
        print(USER_API)

        for usuarioChiquito2 in USER_API:
            card = Tarjetas(
                tipo=usuarioChiquito2['tipo'],
                numero=usuarioChiquito2['numero'],
                titular=usuarioChiquito2['titular'],
                fecha=usuarioChiquito2['fecha'],
            )

            cards.insert(card)
    
    return render(request, 'tarjetas/mostrar_card.html', {'Tarjeta': cards})