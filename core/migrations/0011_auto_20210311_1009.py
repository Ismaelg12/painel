# Generated by Django 3.0.7 on 2021-03-11 13:09

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20210311_1009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diario',
            name='criado_em',
            field=models.DateField(default=datetime.datetime(2021, 3, 11, 13, 9, 5, 567769, tzinfo=utc), verbose_name='Criado em'),
        ),
    ]