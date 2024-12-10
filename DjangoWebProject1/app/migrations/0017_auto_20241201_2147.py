# Generated by Django 2.2.28 on 2024-12-01 18:47

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_auto_20241201_1916'),
    ]

    operations = [
        migrations.CreateModel(
            name='Drink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('image', models.FileField(upload_to='products/', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Напиток',
                'verbose_name_plural': 'Напитки',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('image', models.FileField(upload_to='products/', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2024, 12, 1, 21, 47, 1, 991107), verbose_name='Опубликована'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2024, 12, 1, 21, 47, 1, 991107), verbose_name='Дата комментария'),
        ),
        migrations.CreateModel(
            name='DrinkVolume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('volume', models.CharField(max_length=10, verbose_name='Объем')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('drink', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='volumes', to='app.Drink', verbose_name='Напиток')),
            ],
            options={
                'verbose_name': 'Объем напитка',
                'verbose_name_plural': 'Объемы напитков',
            },
        ),
    ]
