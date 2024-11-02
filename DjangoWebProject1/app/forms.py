"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from django.db import models
from .models import Comment

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))

   

class AnketaForm(forms.Form):
    name = forms.CharField(label='Вашe имя', min_length=2, max_length=100)
    city = forms.CharField(label='Ваш город', min_length=2, max_length=100)
    gender = forms.ChoiceField(label='Ваш пол',
                               choices=[('1', 'Женский'), ('2', 'Мужской')],
                               widget=forms.RadioSelect, initial=1)
    job = forms.ChoiceField(label='Ваш род занятий',
                            choices=(('1', 'учусь'),
                                     ('2', 'работаю'),
                                     ('3', 'отдыхаю'),
                                     ('4', 'в поисках себя')), initial=1)
    notice = forms.BooleanField(label='Получать новости о нас на e-mail?',
                                required=False)
    email = forms.EmailField(label='Ваш e-mail (для связи с Вами)', min_length=7)
    message = forms.CharField(label='Нам интересно узнать о Вас что-то новое. Если Вы не против, расскажите о себе.И расскажите,понравилось ли Вам у нас',
                              widget=forms.Textarea(attrs={'rows': 12, 'cols': 20}))



class CommentForm (forms.ModelForm):
    class Meta:
        model = Comment # используемая модель
        fields = ('text',) # требуется заполнить только поле text
        labels = {'text': "Комментарий"} # метка к полю формы text

