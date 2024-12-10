# Generated by Django 2.2.28 on 2024-12-07 20:30

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0032_auto_20241207_2320'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('pending', 'В ожидании'), ('processing', 'В обработке'), ('completed', 'Завершен'), ('cancelled', 'Отменен')], default='pending', max_length=20, verbose_name='Статус заказа'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2024, 12, 7, 23, 30, 57, 813999), verbose_name='Опубликована'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2024, 12, 7, 23, 30, 57, 814996), verbose_name='Дата комментария'),
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='app.Order')),
            ],
            options={
                'verbose_name': 'Элемент заказа',
                'verbose_name_plural': 'Элементы заказа',
            },
        ),
    ]
