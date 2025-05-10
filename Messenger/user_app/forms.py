from django import forms
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.forms import AuthenticationForm

class RegistrationForm(forms.Form):
    
    email = forms.EmailField(widget= forms.TextInput(attrs={
        "placeholder": "you@example.com",
        "class": "email-input"
    }))
    password = forms.CharField(widget= forms.TextInput(attrs={
        "placeholder": "Напиши пароль",
        "class": "password-input",
        "type": "password"
    }))
    confirm_password = forms.CharField(max_length=255,widget=forms.TextInput(attrs={
        "placeholder":"Повтори пароль"
    }))

    def save(self, email: str, password):
        self.cleaned_data['username'] = self.cleaned_data['email']
        if not User.objects.filter(username=email).exists():
            Profile.objects.create(
                user = User.objects.create_user(username=email, email=email, password=password)
            )
        else:
            raise forms.ValidationError("User with this email already exists")
        

class EmailLoginForm(AuthenticationForm):
    username = forms.EmailField(label="Email",widget= forms.TextInput(attrs={
        "type": "email"
    }))

    def clean(self):
        cleaned_data = super().clean()
        email = self.cleaned_data.get("username")
        if email:
            self.cleaned_data["username"] = email.split("@")[0]
        return self.cleaned_data

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
            
    