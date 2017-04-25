# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-02-28 15:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0003_auto_20170120_1733'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_profile',
            name='area',
            field=models.CharField(choices=[('Electricidad', 'Electricidad'), ('Electr\xf3nica', 'Electr\xf3nica'), ('Mantenimiento y Redes de Computadores', 'Mantenimiento y Redes de Computadores'), ('Transversales', 'Transversales'), ('Telecomunicaciones', 'Telecomunicaciones'), ('Confecciones', 'Confecciones'), ('Actividad F\xedsica', 'Actividad F\xedsica'), ('Ebanister\xeda', 'Ebanister\xeda'), ('Marroquiner\xeda', 'Marroquiner\xeda'), ('Joyer\xeda', 'Joyer\xeda'), ('Ingl\xe9s', 'Ingl\xe9s'), ('Construcci\xf3n', 'Construcci\xf3n'), ('Desarrollo de Software', 'Desarrollo de Software'), ('Industrias Creativas', 'Industrias Creativas'), ('Gesti\xf3n Empresarial', 'Gesti\xf3n Empresarial'), ('Mec\xe1nica', 'Mec\xe1nica'), ('Miner\xeda', 'Miner\xeda'), ('Ambiental', 'Ambiental'), ('Soldadura ', 'Soldadura '), ('No tiene', 'No tiene')], default='', max_length=50),
        ),
        migrations.AddField(
            model_name='user_profile',
            name='lider_area',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user_profile',
            name='supervisor',
            field=models.CharField(choices=[('Julio Prado', 'Julio Prado '), ('Maria del Carmen', 'Maria del Carmen'), ('Janeth Patricia', 'Janeth Patricia'), ('No tiene', 'No tiene')], default='', max_length=50),
        ),
    ]