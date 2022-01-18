# Generated by Django 3.0.3 on 2022-01-18 01:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0044_auto_20220117_2243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boletim',
            name='upload_em',
            field=models.DateField(default=datetime.datetime(2022, 1, 18, 1, 43, 7, 14650, tzinfo=utc), verbose_name='Criado em'),
        ),
        migrations.AlterField(
            model_name='diario',
            name='criado_em',
            field=models.DateField(default=datetime.datetime(2022, 1, 18, 1, 43, 7, 13791, tzinfo=utc), verbose_name='Criado em'),
        ),
    ]
