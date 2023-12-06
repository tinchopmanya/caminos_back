from django.db import models

# Create your models here.
class Especalidad( models.Model):
    idEspecialidad = models.AutoField(primary_key=True)
    nombreEspecialidad = models.TextField()
    estadoEspecialidad = models.SmallIntegerField
    fechacreado = models.DateTimeField(auto_now_add=True)

