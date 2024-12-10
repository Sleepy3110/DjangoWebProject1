# Generated by Django 2.2.28 on 2024-12-08 11:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0043_auto_20241208_0034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2024, 12, 8, 14, 21, 14, 662818), verbose_name='Опубликована'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2024, 12, 8, 14, 21, 14, 663815), verbose_name='Дата комментария'),
        ),
    ]
