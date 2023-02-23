from django.db import models
from applications.Entrenador.models import Entrenador
from applications.Rutina.models import Rutina

# Create your models here.
class Alumno(models.Model):

    dni = models.IntegerField(primary_key=True)
    nombre = models.CharField("Nombre", max_length=50)
    apellido = models.CharField("Apellido", max_length=50)
    edad = models.IntegerField()
    peso = models.IntegerField()
    altura = models.IntegerField()
    telefono = models.CharField("Telefono", max_length=50)
    fecha_de_inicio = models.DateField("Fecha de inicio", auto_now=False, auto_now_add=False)
    fecha_abonada = models.DateField("Fecha hasta la cual abono inscripcion", auto_now=False, auto_now_add=False)
    plan = models.CharField("Tipo de plan", max_length=50)
    dias_de_entrenamiento = models.CharField("Dias de entrenamiento segun la inscripcion", max_length=50)
    entrenador = models.ForeignKey(Entrenador, on_delete=models.CASCADE)
    rutina = models.ForeignKey(Rutina, on_delete=models.CASCADE, null=True)


    class Meta:
        verbose_name = ("Alumno")
        verbose_name_plural = ("Alumnos")

    def __str__(self):
        return f"{self.dni}, {self.nombre} {self.apellido}, {self.telefono}"