# Generated by Django 2.2.28 on 2024-10-28 16:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2024, 10, 28, 19, 17, 37, 905924), verbose_name='Опубликована'),
        ),
    ]