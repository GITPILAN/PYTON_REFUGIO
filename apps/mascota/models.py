from django.db import models
# importamos el modelo persona de app.adopcion.persona
from apps.adopcion.models import Persona

# Create your models here. tablas

class Vacunas(models.Model):
    nombre_vacuna=models.CharField(max_length=50)
    fecha_aplicacion=models.DateField()

    def __str__(self):
        return '{}'.format(self.nombre_vacuna)


class Mascota(models.Model):
    nombre= models.CharField(max_length=50)
    sexo= models.CharField(max_length=10)
    edad_aproximada= models.IntegerField()
    fecha_rescate=models.DateField()
    persona=models.ForeignKey(Persona,null=True,blank=True, on_delete=models.CASCADE)
    vacuna=models.ManyToManyField(Vacunas)
    objects = models.Manager()

    def __str__(self):
        return '{}'.format(self.nombre)
