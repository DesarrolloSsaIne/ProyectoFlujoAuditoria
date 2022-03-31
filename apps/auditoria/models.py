from django.db import models
from apps.estado_auditoria.models import Glo_EstadoAuditoria, Glo_autoria_tipo
from django.contrib.auth.models import User
from apps.jefaturas.models import Ges_Jefatura



# Create your models here.


class Ges_auditoria(models.Model):
    cod_auditoria= models.CharField(max_length=14)
    jefatura_id = models.ForeignKey(Ges_Jefatura, on_delete=models.PROTECT, null=True, blank=True )
    anio_auditoria= models.IntegerField()
    descripcion_auditoria = models.CharField(max_length=250)
    alcance_auditoria = models.CharField(max_length=250)
    tipo_auditoria =models.ForeignKey(Glo_autoria_tipo, on_delete=models.PROTECT, null=True, blank=True)
    estado_auditoria= models.ForeignKey(Glo_EstadoAuditoria, on_delete=models.PROTECT, null=True, blank=True)
    fecha_inicio_auditoria= models.DateField()
    fecha_termino_auditoria=models.DateField(null=True, blank=True)


class Glo_autoria_auditor(models.Model):
    id_auditoria = models.ForeignKey(Ges_auditoria, on_delete=models.PROTECT, null=True, blank=True)
    id_auditor = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True)

