from django.db import models

# Create your models here.

class Ges_Cargo_Hallazgo(models.Model):
    descripcion_cargo = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.descripcion_cargo)