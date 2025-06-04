from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse, HttpRequest
from django.views import View
from django.views.generic.edit import FormView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.core.mail import send_mail
from .models import CustomAbstractUser, RegistrationCodes
from .forms import RegistrationForm, EmailLoginForm, ConfirmEmailForm
from django.urls import reverse_lazy
import secrets, string, os

# Create your views here.
code = []

class RegistrationPageView(View):
    
    def get(self, request: HttpRequest):
        return render(request, 'user_app/signup.html', {
            'form': RegistrationForm(),
            'page' :"reg"
        })
    def post(self, request: HttpRequest):
        button = request.POST.get('submitform')
        print(button)
        if button == 'mainform':
            form = RegistrationForm(request.POST)
            if form.is_valid():
                if form.cleaned_data['password1'] == form.cleaned_data['password2']:
                    code = ''
                    for number in range(6):
                        code += secrets.choice(string.digits)
                    email=form.cleaned_data['email']

                    RegistrationCodes.objects.create(
                        email=email,
                        code=code
                    )
                    send_mail(
                        'Код підтвердження електронної пошти',
                        f'Дякуємо що користуєтесь World IT Messenger!\nКод підтвердження реєстрації: {code}',
                        None,
                        [email],
                    )
                    response = render(request, 'user_app/signup.html', {
                        'form': ConfirmEmailForm,
                        'email': email,
                        'enter_code': True
                    })
                    response.set_cookie('email', form.cleaned_data['email'])
                    response.set_cookie('password', form.cleaned_data['password1'])

                    return response
                else:
                    form.add_error('confirm_password', 'Паролі не співпадають')
                    return render(
                        request, 'user_app/signup.html',
                        {
                            'form': RegistrationForm(),
                            'enter_code': False
                        })
            else:
                print("error")
                return render(
                    request,
                    'user_app/signup.html',
                    {
                        'form': RegistrationForm(),
                        'enter_code': False
                    }
                    )
        elif button == 'codeform':
            form = ConfirmEmailForm(request.POST)
            if form.is_valid():
                email = request.COOKIES.get('email')
                print(email, RegistrationCodes.objects.filter(email=email).exists())
                if CustomAbstractUser.objects.filter(username=email).exists() == False:
                    auth_code = RegistrationCodes.objects.get(email=email).code
                    entered_code = f"{form.cleaned_data['number_of_code1']}{form.cleaned_data['number_of_code2']}{form.cleaned_data['number_of_code3']}{form.cleaned_data['number_of_code4']}{form.cleaned_data['number_of_code5']}{form.cleaned_data['number_of_code6']}"
                    print(auth_code, entered_code)
                    if entered_code == auth_code:
                        password = request.COOKIES.get('password')
                        print('User Created')
                        CustomAbstractUser.objects.create_user(username=email, email=email, password=password)
                        response = HttpResponseRedirect(reverse_lazy("login"))
                        response.delete_cookie('email')
                        response.delete_cookie('password')
                        return response
class AuthPageView(LoginView):
    template_name = "user_app/login.html"           
    authentication_form = EmailLoginForm
    success_url = "/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type_form"] = "login"
        return context

class CustomLogoutView(LogoutView):
    next_page = "login"

    