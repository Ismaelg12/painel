# Generated by Django 3.0.3 on 2022-01-18 01:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0043_auto_20211118_1842'),
    ]

    operations = [
        migrations.AddField(
            model_name='diario',
            name='leito_srag',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='diario',
            name='uti_srag',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='boletim',
            name='upload_em',
            field=models.DateField(default=datetime.datetime(2022, 1, 18, 1, 42, 53, 911531, tzinfo=utc), verbose_name='Criado em'),
        ),
        migrations.AlterField(
            model_name='diario',
            name='criado_em',
            field=models.DateField(default=datetime.datetime(2022, 1, 18, 1, 42, 53, 910669, tzinfo=utc), verbose_name='Criado em'),
        ),
    ]
