"""
Definition of models.
"""

from django.db import models
from django.contrib import admin
from datetime import datetime
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Blog(models. Model):
    title = models.CharField(max_length = 100, unique_for_date = "posted", verbose_name = "Заголовок")
    description = models.TextField(verbose_name = "Краткое содержание")
    content = models.TextField(verbose_name = "Полное содержание")
    posted = models.DateTimeField(default = datetime.now(), db_index = True, verbose_name = "Опубликована")
    author = models.ForeignKey(User, null=True, blank=True, on_delete = models.SET_NULL, verbose_name = "Автор")
    image = models.FileField(default = "temp.jpg", verbose_name= "Путь картинкe")
    #Методы класса:
    def get_absolute_url(self): # метод возвращает строку с URL-адресом записи
        return reverse("blogpost", args=[str(self.id)])
    def __str__(self): #метод возвращает название, используемое для представления отдельных записей в административном разделе
        return self.title
    #Метаданные - вложенный класс, который задает дополнительные параметры модели 
    class Meta:
        db_table = "Posts" #имя таблицы для модели
        ordering = ["-posted"] #порядок сортировки данных в модели ("-" означает по убыванию)
        verbose_name = "статья блога" # имя, под которым модель будет отображаться в административном разделе (для одной статьи блога)
        verbose_name_plural = "статьи блога" # тоже для всех статей блога

admin.site.register(Blog)
class Comment (models.Model):
    text = models.TextField(verbose_name = "Текст комментария")
    date = models.DateTimeField(default = datetime.now(), db_index = True, verbose_name = "Дата комментария") 
    author = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name = "Автор комментария") 
    post = models.ForeignKey(Blog, on_delete = models.CASCADE, verbose_name = "Статья комментария")
    #Методы класса:
    def __str__(self): #метод возвращает название, используемое для представления отдельных записей в административном разделе
        return 'Комментарий %d %s к  %s' %(self.id, self.author, self.post)
    #Метаданные - вложенный класс, который задает дополнительные параметры модели
    class Meta:
        db_table = "Comment"
        ordering = ["-date"]
        verbose_name = "Комментарии к статье блога"
        verbose_name_plural = "Комментарии к статьям блога"

admin.site.register(Comment)





# models.py




from django.db import models
from django.contrib import admin

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название категории")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    image = models.FileField(upload_to='products/', verbose_name="Изображение")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

class Drink(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    image = models.FileField(upload_to='products/', verbose_name="Изображение")
    volume = models.CharField(max_length=10, verbose_name="Объем")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Напиток"
        verbose_name_plural = "Напитки"

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Drink)



from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import User

class Order(models.Model):
    STATUS_CHOICES = [
        ('created', 'Создан'),
        ('in_transit', 'В пути'),
        ('received', 'Получен'),
        ('cancelled', 'Отменен'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    name = models.CharField(max_length=100, verbose_name="Имя")
    phone = models.CharField(max_length=15, verbose_name="Телефон")
    payment_method = models.CharField(max_length=10, choices=[('cash', 'Наличные'), ('card', 'Карта')], verbose_name="Способ оплаты")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='created', verbose_name="Статус заказа")
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Итоговая сумма")

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE, verbose_name="Заказ")
    product_name = models.CharField(max_length=100, verbose_name="Название товара")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    quantity = models.PositiveIntegerField(default=1, verbose_name="Количество")

    def __str__(self):
        return f"{self.quantity} x {self.product_name}"

    class Meta:
        verbose_name = "Элемент заказа"
        verbose_name_plural = "Элементы заказа"

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1
    fields = ('product_name', 'price', 'quantity')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'name', 'phone', 'payment_method', 'created_at', 'status', 'total_amount')
    list_filter = ('status', 'payment_method', 'created_at')
    search_fields = ('user__username', 'name', 'phone')
    inlines = [OrderItemInline]



admin.site.register(Order, OrderAdmin)