# Generated by Django 2.2.7 on 2021-09-22 20:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('periodos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ges_CuartoNivel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion_nivel', models.CharField(max_length=100)),
                ('estado', models.BooleanField()),
                ('id_periodo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='periodos.Glo_Periodos')),
            ],
        ),
        migrations.CreateModel(
            name='Ges_PrimerNivel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion_nivel', models.CharField(max_length=80)),
                ('estado', models.BooleanField()),
                ('id_periodo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='periodos.Glo_Periodos')),
            ],
        ),
        migrations.CreateModel(
            name='Ges_SegundoNivel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion_nivel', models.CharField(max_length=80)),
                ('estado', models.BooleanField()),
                ('id_periodo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='periodos.Glo_Periodos')),
                ('primer_nivel', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='estructura_jerarquica.Ges_PrimerNivel')),
            ],
        ),
        migrations.CreateModel(
            name='Ges_TercerNivel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion_nivel', models.CharField(max_length=80)),
                ('estado', models.BooleanField()),
                ('id_periodo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='periodos.Glo_Periodos')),
                ('segundo_nivel', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='estructura_jerarquica.Ges_SegundoNivel')),
            ],
        ),
        migrations.CreateModel(
            name='Ges_Niveles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orden_nivel', models.IntegerField()),
                ('descripcion_nivel', models.CharField(max_length=150)),
                ('estado', models.BooleanField()),
                ('id_cuarto_nivel', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='estructura_jerarquica.Ges_CuartoNivel')),
                ('id_periodo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='periodos.Glo_Periodos')),
                ('id_primer_nivel', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='estructura_jerarquica.Ges_PrimerNivel')),
                ('id_segundo_nivel', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='estructura_jerarquica.Ges_SegundoNivel')),
                ('id_tercer_nivel', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='estructura_jerarquica.Ges_TercerNivel')),
            ],
        ),
        migrations.AddField(
            model_name='ges_cuartonivel',
            name='tercer_nivel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='estructura_jerarquica.Ges_TercerNivel'),
        ),
    ]