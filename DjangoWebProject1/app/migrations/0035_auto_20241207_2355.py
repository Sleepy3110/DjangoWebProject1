# Generated by Django 2.2.28 on 2024-12-07 20:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0034_auto_20241207_2331'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total_amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Итоговая сумма'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2024, 12, 7, 23, 55, 42, 884785), verbose_name='Опубликована'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2024, 12, 7, 23, 55, 42, 884785), verbose_name='Дата комментария'),
        ),
    ]
