# Generated by Django 4.2.4 on 2024-05-08 20:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema_store', '0002_film_hall_session'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='session',
            name='show_at',
        ),
        migrations.AddField(
            model_name='session',
            name='date',
            field=models.DateField(default=datetime.datetime(2024, 5, 8, 23, 54, 2, 668997)),
        ),
        migrations.AddField(
            model_name='session',
            name='time',
            field=models.TimeField(default=datetime.datetime(2024, 5, 8, 9, 0)),
        ),
    ]