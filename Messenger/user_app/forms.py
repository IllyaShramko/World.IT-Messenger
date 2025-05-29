from django import forms
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import Profile

class RegistrationForm(UserCreationForm):
    username = forms.CharField(required= False, widget= forms.TextInput(attrs={
        "type": "hidden"
    }))

    email = forms.EmailField(widget= forms.TextInput(attrs={
        "placeholder": "you@example.com",
        "class": "email-input"
    }))
    password1 = forms.CharField(widget= forms.TextInput(attrs={
        "placeholder": "Напиши пароль",
        "class": "password-input",
        "type": "password",
        "id": "password-input"
    }))
    password2 = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder":"Повтори пароль",
        "class": "password-confirm-input",
        "type": "password",
        "id": "password-confirm-input"
    }))
        

class EmailLoginForm(AuthenticationForm):
    username = forms.EmailField(label="Email",widget= forms.TextInput(attrs={
        "type": "email"
    }))


class ConfirmEmailForm(forms.Form):
    number_of_code1 = forms.CharField(max_length = 1, widget = forms.TextInput(attrs = {
        "placeholder": "_",
        "class": "input-number"
    }))
    number_of_code2= forms.CharField(max_length = 1, widget = forms.TextInput(attrs = {
        "placeholder": "_",
        "class": "input-number"
    }))
    number_of_code3= forms.CharField(max_length = 1, widget = forms.TextInput(attrs = {
        "placeholder": "_",
        "class": "input-number"
    }))
    number_of_code4= forms.CharField(max_length = 1, widget = forms.TextInput(attrs = {
        "placeholder": "_",
        "class": "input-number"
    }))
    number_of_code5= forms.CharField(max_length = 1, widget = forms.TextInput(attrs = {
        "placeholder": "_",
        "class": "input-number"
    }))
    number_of_code6=forms.CharField(max_length = 1, widget = forms.TextInput(attrs = {
        "placeholder": "_",
        "class": "input-number"
    }))

    def verify_code(self, code: list, numbers_of_code: list):
        index = 0
        for number in numbers_of_code:
            if number == code[index]:
                index += 1
            else:
                if index == 5:
                    return HttpResponseRedirect("/")
                else:
                    return HttpResponse({'error': 'error'})
            
    