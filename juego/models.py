from django.db import models

# Create your models here.

class Holken(models.Model):
    num_holken = models.CharField(primary_key=True, max_length=5)
    nombre_holken = models.CharField(max_length=50)
    equipo = models.CharField(max_length= 50)
    rol = models.CharField(max_length=50)
    puntos = models.IntegerField()
    #campo para las imagenes
    avatar = models.ImageField(upload_to="holken/", null=True)

    def __str__(self):
        return self.nombre_holken

class meta:
    db_tabla='Holken'
    