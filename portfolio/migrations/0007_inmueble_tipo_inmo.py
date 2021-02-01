# Generated by Django 3.1.2 on 2021-01-20 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_auto_20210119_1746'),
    ]

    operations = [
        migrations.AddField(
            model_name='inmueble',
            name='tipo_inmo',
            field=models.IntegerField(choices=[(1, 'Apartamento'), (2, 'Casa'), (3, 'Local'), (4, 'Solar'), (5, 'Edificio')], default=1, verbose_name='Planta electrica'),
        ),
    ]