from django.db import models

# Create your models here.

class Entrenador(models.Model):

    dni = models.IntegerField(primary_key=True)
    nombre = models.CharField("Nombre del entrenador", max_length=50)
    apellido = models.CharField("Apellido del entrenador", max_length=50)
    telefono = models.CharField("Telefono del entrenador", max_length=50)

    class Meta:
        verbose_name = ("Entrenador")
        verbose_name_plural = ("Entrenadores")

    def __str__(self):
        return f"{self.nombre} {self.apellido}" 