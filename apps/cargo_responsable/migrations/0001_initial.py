# Generated by Django 2.2.7 on 2021-09-22 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ges_Cargo_Hallazgo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion_cargo', models.CharField(blank=True, max_length=150, null=True)),
            ],
        ),
    ]