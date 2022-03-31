from django.db import models
from django.contrib.auth.models import User
from apps.cargo_responsable.models import Ges_Cargo_Hallazgo
from apps.estados_hallazgo.models import Glo_EstadosHallazgo
from apps.jefaturas.models import Ges_Jefatura
from apps.auditoria.models import Ges_auditoria
# Create your models here.- Número total de hallazgos.

# - Proceso/Subproceso/Etapa/Proyecto/Otro
# - Número del hallazgo
# - Naturaleza del Trabajo
# - Descripción del Hallazgo (Condición)
# - Opinión Criticidad Micro
# - Criterios
# - Causas
# - Efectos
# - ¿Se solicita procedimiento sumarial?
# - Descripción Recomendación
# - Plazo Estimado


class Ges_Hallazgo(models.Model):
    jefatura_id = models.ForeignKey(Ges_Jefatura, on_delete=models.PROTECT, null=True, blank=True)
    id_auditoria = models.ForeignKey(Ges_auditoria, on_delete=models.PROTECT, null=True)
    numero_hallazgo = models.CharField(max_length=5, null=True, blank=True)
    proceso = models.CharField(max_length=200, null=True, blank=True)
    naturaleza = models.CharField(max_length=150, null=True, blank=True)
    descripcion_hallazgo = models.CharField(max_length=2500)
    criterios =models.CharField(max_length=1500, null=True, blank=True)
    causas = models.CharField(max_length=1000, null=True, blank=True)
    efectos = models.CharField(max_length=1000, null=True, blank=True)
    sumario = models.CharField(max_length=150, null=True, blank=True)
    recomendacion = models.CharField(max_length=1500, null=True, blank=True)
    plazo =  models.DateTimeField(blank=True, null=True)
    opinion = models.CharField(max_length=150, null=True, blank=True)
    id_estadoshallazgo = models.ForeignKey(Glo_EstadosHallazgo, on_delete=models.PROTECT, null=True)
    document = models.FileField(null=True, blank=True)
    cargo_responsable_id = models.ForeignKey(Ges_Cargo_Hallazgo, on_delete=models.PROTECT, null=True)
    enc_gestion_id = models.ForeignKey(User, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return '{}'.format(self.descripcion_hallazgo)
