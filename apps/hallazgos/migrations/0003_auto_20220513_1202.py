# Generated by Django 2.2.7 on 2022-05-13 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hallazgos', '0002_auto_20211125_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ges_hallazgo',
            name='numero_hallazgo',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
