
from django.db import models
from django.contrib.auth.models import User
from apps.cargo_responsable.models import Ges_Cargo_Hallazgo
from apps.jefaturas.models import Ges_Jefatura
from apps.hallazgos.models import Ges_Hallazgo
from apps.estado_compromiso.models import Glo_Estado_Compromiso

# Create your models here.


class Ges_Compromisos(models.Model):
    descripcion_compromiso = models.CharField(max_length=1500, blank=True, null=True)
    medio_verificacion = models.CharField(max_length=1000, blank=True, null=True)
    plazo_implementacion = models.DateTimeField(blank=True, null=True)
    responsable_hallazgo = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    comentario_compromiso = models.CharField(max_length=1000, blank=True, null=True)
    comentario_auditor = models.CharField(max_length=1500, blank=True, null=True)
    cargo_responsable_id= models.ForeignKey(Ges_Cargo_Hallazgo, on_delete=models.PROTECT, null=True)
    hallazgo_id = models.ForeignKey(Ges_Hallazgo, on_delete=models.PROTECT, null=True)
    estado_compromiso= models.ForeignKey(Glo_Estado_Compromiso, on_delete=models.PROTECT, null=True )



class Ges_Observaciones_Compromiso_Enc(models.Model):
    descripcion_Observacion = models.CharField(max_length=1500, blank=True, null=True)
    fecha_observacion = models.DateTimeField(blank=True, null=True)
    usuario_observacion = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    visto = models.IntegerField(blank=True, null=True)
    compromiso_observacion = models.ForeignKey(Ges_Compromisos, on_delete=models.PROTECT, null=True)