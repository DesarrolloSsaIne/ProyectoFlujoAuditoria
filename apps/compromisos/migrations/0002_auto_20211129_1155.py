# Generated by Django 2.2.7 on 2021-11-29 14:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('compromisos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ges_compromisos',
            name='responsable_hallazgo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]