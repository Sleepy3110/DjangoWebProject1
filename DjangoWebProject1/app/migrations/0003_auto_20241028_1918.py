# Generated by Django 2.2.28 on 2024-10-28 16:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20241028_1917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2024, 10, 28, 19, 18, 26, 806695), verbose_name='Опубликована'),
        ),
    ]