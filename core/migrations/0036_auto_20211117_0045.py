# Generated by Django 3.0.3 on 2021-11-17 03:45

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0035_auto_20211117_0045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diario',
            name='criado_em',
            field=models.DateField(default=datetime.datetime(2021, 11, 17, 3, 45, 50, 277987, tzinfo=utc), verbose_name='Criado em'),
        ),
    ]
