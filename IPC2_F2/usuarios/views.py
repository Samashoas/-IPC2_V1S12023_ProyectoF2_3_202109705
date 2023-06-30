from django.shortcuts import *
from usuarios.ListaSE import *
import requests

global LE
LE = LinkedList()

def mostrar_usuario(request):
    users = load_users_from_xml('C:/Users/jpsam/OneDrive/Escritorio/Python/-IPC2_V1S12023_ProyectoF2_3_202109705/IPC2_F2/usuarios/Usuarios.xml')
    return render(request, 'usuarios/Mostrar.html', {'Usuario': users})

def load_xml(request):
    if request.method == 'POST':
        users = load_users_from_xml('C:/Users/jpsam/OneDrive/Escritorio/Python/-IPC2_V1S12023_ProyectoF2_3_202109705/IPC2_F2/usuarios/Usuarios.xml')
        response = requests.get('http://localhost:5007/getUsuarios')
        USER_API = response.json()
        print(USER_API)

        for usuarioChiquito2 in USER_API:
            user = User(
                index=users.get_next_index(),
                rol=usuarioChiquito2['rol'],
                nombre=usuarioChiquito2['nombre'],
                apellido=usuarioChiquito2['apellido'],
                telefono=usuarioChiquito2['telefono'],
                correo=usuarioChiquito2['correo'],
                contrasena=usuarioChiquito2['contrasena']
            )

            users.append(user)
    
    return render(request, 'usuarios/Mostrar.html', {'Usuario': users})