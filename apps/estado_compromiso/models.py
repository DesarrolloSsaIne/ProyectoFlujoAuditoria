from django.db import models

# Create your models here.


class Glo_Estado_Compromiso(models.Model):
    descripcion_estado_compromiso = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.descripcion_estado_compromiso)