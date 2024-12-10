# Generated by Django 2.2.28 on 2024-12-08 12:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0046_auto_20241208_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2024, 12, 8, 15, 54, 55, 134749), verbose_name='Опубликована'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2024, 12, 8, 15, 54, 55, 135745), verbose_name='Дата комментария'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('created', 'Создан'), ('in_transit', 'В пути'), ('received', 'Получен'), ('cancelled', 'Отменен')], default='created', max_length=20, verbose_name='Статус заказа'),
        ),
    ]