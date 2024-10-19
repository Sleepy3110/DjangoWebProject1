"""
Definition of views.
"""
    
from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from .forms import AnketaForm 

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
   gender = {'1': 'Женщина', '2': 'Мужчина'}
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