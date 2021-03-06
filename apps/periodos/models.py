from django.db import models

# Create your models here.

class Glo_EstadoPeriodo(models.Model):
    estado= models.IntegerField()
    descripcion_periodo= models.CharField(max_length=100)

    def __str__(self):
        return '{}'.format(self.descripcion_periodo)


class Glo_Periodos(models.Model):
    descripcion_periodo = models.CharField(max_length=100)
    anio_periodo= models.IntegerField()
    fecha_inicio=models.DateField(blank=True, null=True)
    fecha_termino=models.DateField(blank=True, null=True)
    id_estado = models.ForeignKey(Glo_EstadoPeriodo, on_delete=models.PROTECT, null=True)