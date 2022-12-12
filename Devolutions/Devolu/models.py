from django.db import models
from django.contrib.auth.models import AbstractUser

class AdminUser(AbstractUser):
    rut = models.CharField(max_length=10)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    celular = models.PositiveIntegerField(blank=True, null=True)
    
class Cliente(models.Model):
    rut = models.CharField(max_length=10)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    celular = models.PositiveIntegerField()
   
class Devolucion(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    cantidad = models.CharField(max_length=100)
    producto = models.CharField(max_length=100)
    codigo = models.CharField(max_length=100)
    vendedor = models.CharField(max_length=100)
    distribuidor = models.CharField(max_length=100)
    comentario = models.CharField(max_length=100)

