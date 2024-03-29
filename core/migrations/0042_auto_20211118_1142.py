# Generated by Django 3.0.3 on 2021-11-18 14:42

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0041_auto_20211117_1432'),
    ]

    operations = [
        migrations.CreateModel(
            name='Boletim',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('boletim', models.ImageField(upload_to='media')),
                ('upload_em', models.DateField(default=datetime.datetime(2021, 11, 18, 14, 42, 18, 301824, tzinfo=utc), verbose_name='Criado em')),
                ('status', models.BooleanField(blank=True, default=True, verbose_name='Status')),
            ],
            options={
                'verbose_name': 'Boletim',
                'verbose_name_plural': 'Boletins',
            },
        ),
        migrations.AlterField(
            model_name='diario',
            name='criado_em',
            field=models.DateField(default=datetime.datetime(2021, 11, 18, 14, 42, 18, 301282, tzinfo=utc), verbose_name='Criado em'),
        ),
    ]
