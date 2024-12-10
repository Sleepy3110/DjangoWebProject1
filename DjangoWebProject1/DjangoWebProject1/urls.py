"""
Definition of urls for DjangoWebProject1.
"""

from datetime import datetime
from django.urls import path

from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views

from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns 
from django.conf import settings



urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('login/',
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Log in',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
    path('links/', views.links, name='links'),
    path('anketa/', views.anketa, name='anketa'),
    path('registration/', views. registration, name= 'registration'),
    path('blog/', views.blog, name='blog'),
    path('blogpost/<int:parametr>/', views.blogpost, name='blogpost'),
    path('newpost/', views.newpost, name='newpost'),
    path('videopost/', views.videopost, name='videopost'),
    path('catalog/', views.catalog, name='catalog'),
    path('add_product/', views.add_product, name='add_product'),
    path('add_drink/', views.add_drink, name='add_drink'),
    path('checkout/', views.checkout, name='checkout'),
    path('order_success/', views.order_success, name='order_success'),
    path('my_orders/', views.my_orders, name='my_orders'),
    path('check_auth/', views.check_auth, name='check_auth'),
    path('save_cart/', views.save_cart, name='save_cart'),
    path('cancel_order/<int:order_id>/', views.cancel_order, name='cancel_order'),
    path('manager_orders/', views.manager_orders, name='manager_orders'),
    path('update_order_status/<int:order_id>/', views.update_order_status, name='update_order_status'),
   

]

urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT) 
urlpatterns += staticfiles_urlpatterns()
