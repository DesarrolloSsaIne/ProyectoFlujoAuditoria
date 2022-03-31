from django.db import models

# Create your models here.
class Glo_EstadoAuditoria(models.Model):
    descripcion_estado = models.CharField(max_length=100)

    def __str__(self):
        return '{}'.format(self.descripcion_estado)


class Glo_autoria_tipo(models.Model):
    descripcion_tipo = models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.descripcion_tipo)
