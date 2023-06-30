from django.db import models

class User(models.Model):
    index = models.IntegerField()
    rol = models.TextField(max_length=15)
    nombre = models.TextField(max_length=100)
    apellido = models.TextField(max_length=100)
    telefono = models.IntegerField()
    correo = models.TextField(max_length=100)
    contrasena = models.CharField(max_length=100)