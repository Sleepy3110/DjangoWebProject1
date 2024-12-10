"""
Definition of views.
"""
    
from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpRequest
from .forms import AnketaForm 
from django.contrib.auth.forms import UserCreationForm
from django.db import models
from .models import Blog
from .models import Comment # использование модели комментариев
from .forms import CommentForm # использование формы ввода комментария
from .forms import BlogForm # использование формы ввода статьи блога
from django.http import JsonResponse
from .models import Product, Drink, Category
from .forms import ProductForm, DrinkForm



def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Главная',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Контакты',
            'message':'Страница с нашими контактами',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'О нас',
            'year':datetime.now().year,
        }
    )
def links(request):
    return render(request, 'app/links.html')

def anketa(request):
   assert isinstance(request, HttpRequest)
   data = None 
   gender = {'1': 'Женский', '2': 'Мужской'}
   job = {'1': 'учусь', '2': 'работаю',
         '3': 'отдыхаю', '4': 'в поисках себя'} 
   if request.method == 'POST':
       form = AnketaForm(request.POST)
       if form.is_valid():
        data = dict()
        data['name'] = form. cleaned_data['name']
        data['city'] = form.cleaned_data['city']
        data['job'] = job[form.cleaned_data['job'] ]
        data['gender'] = gender[form.cleaned_data['gender'] ] 
        if(form.cleaned_data['notice'] == True):
           data['notice'] = 'Да'
        else: 
           data['notice'] = 'Нет'
        data['email'] = form. cleaned_data['email'] 
        data['message'] = form.cleaned_data['message']
        form = None
   else:
       form = AnketaForm()
   return render(
       request,
       'app/anketa.html',
       {
        'form':form,
        'data': data
        }
   )

def registration(request):
    """Renders the registration page."""

    

    if request.method == "POST": # после отправки формы
        regform = UserCreationForm (request.POST)
        if regform.is_valid(): #валидация полей формы
            reg_f = regform.save(commit=False) # не сохраняем автоматически данные формы
            reg_f.is_staff = False # запрещен вход в административный раздел
            reg_f.is_active = True # активный пользователь
            reg_f.is_superuser = False # не является суперпользователем
            reg_f.date_joined = datetime.now() # дата регистрации
            reg_f.last_login = datetime.now() # дата последней авторизации
            reg_f.save() # сохраняем изменения после добавления данных
            
            return redirect('home') # переадресация на главную страницу после регистрации
    else:
        regform = UserCreationForm() # создание объекта формы для ввода данных нового пользователя
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/registration.html',
        {
            'regform': regform, # передача формы в шаблон веб-страницы
            'year':datetime.now().year,
        }

)

def blog(request):
    """Renders the blog page."""
    posts = Blog.objects.all() # запрос на выбор всех статей блога из модели
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/blog.html',
        {
            'title':'Блог',
            'posts': posts, # передача списка статей в шаблон веб-страницы
            'year':datetime.now().year,
        }

)

def blogpost(request, parametr):
    """Renders the blogpost page."""
    assert isinstance(request, HttpRequest)
    post_1 = Blog.objects.get(id=parametr) # запрос на выбор конкретной статьи по параметру
    comments = Comment.objects.filter(post=parametr)
    if request.method == "POST": # после отправки данных формы на сервер методом POST
        form = CommentForm(request.POST)
        if form.is_valid():
            comment_f = form.save(commit=False)
            comment_f.author = request.user # добавляем (так как этого поля нет в форме) в модель Комментария (Comment) в поле автор авторизованного пользователя
            comment_f.date = datetime.now() # добавляем в модель Комментария (Comment) текущую дату
            comment_f.post = Blog.objects.get(id=parametr) # добавляем в модель Комментария (Comment) статью, для которой данный комментарий
            comment_f.save() # сохраняем изменения после добавления полей
            return redirect('blogpost', parametr=post_1.id) # переадресация на ту же страницу статьи после отправки комментария

    else:
        form = CommentForm() # создание формы для ввода комментария
    return render(
        request,
        'app/blogpost.html',
        {
            'post_1': post_1, # передача конкретной статьи в шаблон веб-страницы
            'comments': comments, # передача всех комментариев к данной статье в шаблон веб-страницы
            'form': form, # передача формы добавления комментария в шаблон веб-страницы
            'year':datetime.now().year,

        }

)

def newpost(request):
    """Renders the newpost page."""
    assert isinstance(request, HttpRequest)
    if request.method == "POST":        # после отправки формы:
        blogform = BlogForm(request.POST, request.FILES) 
        if blogform.is_valid():
            blog_f = blogform.save(commit=False)
            blog_f.posted = datetime.now()
            blog_f.autor = request.user
            blog_f.save()               # сохраняем изменения после добавления полей
            
            return redirect('blog')     # переадресация на страницу Блог после создания статьи Блога
    else:
        blogform= BlogForm()            # создание объекта формы для ввода данных
    return render(
        request,
        'app/newpost.html',
        {
            'blogform': blogform,       # передача формы в шаблон веб-страницы
            'title': 'Добавить статью блога',
            'year': datetime.now().year,
            }
    )

def videopost(request):
    """Renders the videopost  page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/videopost.html',
        {
            'title':'Видео',
            'year':datetime.now().year,
        }
    )













# views.py






from django.conf import settings
from django.core.serializers import serialize
import json
from django.shortcuts import render, redirect
from .models import Category, Product, Drink
from .forms import ProductForm, DrinkForm

def catalog(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    drinks = Drink.objects.all()

    # Преобразуем QuerySet в список словарей и добавим поле 'model'
    products_list = json.loads(serialize('json', products))
    drinks_list = json.loads(serialize('json', drinks))

    for product in products_list:
        product['fields']['model'] = 'product'

    for drink in drinks_list:
        drink['fields']['model'] = 'drink'

    print(f"Categories: {categories}")
    print(f"Products: {products_list}")
    print(f"Drinks: {drinks_list}")

    return render(
        request,
        'app/catalog.html',
        {
            'categories': categories,
            'products': products_list,
            'drinks': drinks_list,
            'title': 'Каталог',
            'MEDIA_URL': settings.MEDIA_URL,
        }
    )

def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('catalog')
    else:
        form = ProductForm()
    return render(
        request,
        'app/add_product.html',
        {
            'form': form,
            'title': 'Добавить товар',
        }
    )

def add_drink(request):
    if request.method == "POST":
        form = DrinkForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('catalog')
    else:
        form = DrinkForm()
    return render(
        request,
        'app/add_drink.html',
        {
            'form': form,
            'title': 'Добавить напиток',
        }
    )





from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import OrderForm
from .models import Order, OrderItem
from django.views.decorators.csrf import csrf_exempt

@login_required
def checkout(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.total_amount = request.GET.get('total', 0)  # Получаем итоговую сумму из запроса
            order.save()

            # Сохраняем элементы заказа
            cart = request.session.get('cart', [])
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product_name=item['name'],
                    price=item['price'],
                    quantity=item['quantity']
                )

            return redirect('order_success')
    else:
        form = OrderForm()
    return render(request, 'app/checkout.html', {'form': form})


def order_success(request):
    return render(request, 'app/order_success.html')


from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Order

@login_required
def my_orders(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'app/my_orders.html', {'orders': orders})

from django.http import JsonResponse

def check_auth(request):
    return JsonResponse({'is_authenticated': request.user.is_authenticated})

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Order, OrderItem

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def save_cart(request):
    if request.method == 'POST':
        cart = json.loads(request.body)
        request.session['cart'] = cart
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Order

@csrf_exempt
def cancel_order(request, order_id):
    if request.method == 'POST':
        try:
            order = Order.objects.get(id=order_id, user=request.user)
            order.delete()
            return JsonResponse({'success': True})
        except Order.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Заказ не найден.'})
    return JsonResponse({'success': False, 'error': 'Неверный метод запроса.'})






from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def manager_orders(request):
    orders = Order.objects.all()
    return render(request, 'app/manager_orders.html', {'orders': orders})

@csrf_exempt
def update_order_status(request, order_id):
    if request.method == 'POST':
        try:
            order = Order.objects.get(id=order_id)
            data = json.loads(request.body)
            order.status = data.get('status')
            order.save()
            return JsonResponse({'success': True})
        except Order.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Заказ не найден.'})
    return JsonResponse({'success': False, 'error': 'Неверный метод запроса.'})
