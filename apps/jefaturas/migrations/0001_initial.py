# Generated by Django 2.2.7 on 2021-09-22 20:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('periodos', '0001_initial'),
        ('estructura_jerarquica', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ges_Jefatura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_nivel', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='estructura_jerarquica.Ges_Niveles')),
                ('id_periodo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='periodos.Glo_Periodos')),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
