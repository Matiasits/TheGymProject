from django.db import models

class Rutina(models.Model):

    identificador_rutina = models.IntegerField(primary_key=True)
    tipo = models.CharField("tipo de ejercicios", max_length=50)
    lunes = models.CharField("lunes", max_length=1000,default='Sin ejercicio')
    martes = models.CharField("martes", max_length=1000,default='Sin ejercicio')
    miercoles = models.CharField("miercoles", max_length=1000,default='Sin ejercicio')
    jueves = models.CharField("jueves", max_length=1000,default='Sin ejercicio')
    viernes = models.CharField("viernes", max_length=1000,default='Sin ejercicio')
    sabado = models.CharField("sabado", max_length=1000,default='Sin ejercicio')
    
    class Meta:
        verbose_name = ("Rutina")
        verbose_name_plural = ("Rutinas")

    def __str__(self):
        return f" {self.identificador_rutina} {self.tipo}"
                           

