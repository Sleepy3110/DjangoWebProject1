# Generated by Django 2.2.28 on 2024-12-07 20:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0027_auto_20241205_2257'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='status',
        ),
        migrations.RemoveField(
            model_name='order',
            name='total_price',
        ),
        migrations.AddField(
            model_name='order',
            name='name',
            field=models.CharField(default=1, max_length=100, verbose_name='Имя'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='payment_method',
            field=models.CharField(choices=[('cash', 'Наличные'), ('card', 'Карта')], default='cash', max_length=10, verbose_name='Способ оплаты'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='phone',
            field=models.CharField(default=8800555285, max_length=15, verbose_name='Телефон'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2024, 12, 7, 23, 3, 54, 352183), verbose_name='Опубликована'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2024, 12, 7, 23, 3, 54, 352183), verbose_name='Дата комментария'),
        ),
        migrations.DeleteModel(
            name='OrderStatus',
        ),
    ]