# Generated by Django 3.0.7 on 2021-03-18 13:58

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_auto_20210312_0107'),
    ]

    operations = [
        migrations.AddField(
            model_name='conf_mes',
            name='criado_em',
            field=models.DateField(default=datetime.datetime(2021, 3, 18, 13, 58, 10, 301578, tzinfo=utc), verbose_name='Criado em'),
        ),
        migrations.AddField(
            model_name='obitos_mes',
            name='criado_em',
            field=models.DateField(default=datetime.datetime(2021, 3, 18, 13, 58, 10, 300928, tzinfo=utc), verbose_name='Criado em'),
        ),
        migrations.AlterField(
            model_name='diario',
            name='criado_em',
            field=models.DateField(default=datetime.datetime(2021, 3, 18, 13, 58, 10, 299042, tzinfo=utc), verbose_name='Criado em'),
        ),
    ]