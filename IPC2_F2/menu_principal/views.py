from django.shortcuts import render
import requests

def index(request):
    return render(request, 'menu_principal/menu.html')

def login(request):
    return render(request,'menu_principal/login.html')

def registro(request):
    return render(request,'menu_principal/registro.html')

def IndexAdmin(request):
    return render(request,'menu_principal/menu_admin.html') 