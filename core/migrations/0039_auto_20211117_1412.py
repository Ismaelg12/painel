# Generated by Django 3.0.3 on 2021-11-17 17:12

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0038_auto_20211117_0046'),
    ]

    operations = [
        migrations.RenameField(
            model_name='diario',
            old_name='desacartado',
            new_name='descartado',
        ),
        migrations.AlterField(
            model_name='diario',
            name='criado_em',
            field=models.DateField(default=datetime.datetime(2021, 11, 17, 17, 12, 49, 876731, tzinfo=utc), verbose_name='Criado em'),
        ),
    ]
