from django.db import models

# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    edad = models.IntegerField()
    email = models.CharField(max_length=300, null=False)
    clave = models.CharField(max_length=30, null=False)
    validado = models.BooleanField(default=False)