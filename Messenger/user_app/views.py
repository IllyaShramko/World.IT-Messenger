from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse, HttpRequest
from django.views import View
from django.views.generic.edit import FormView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from user_app.models import User
from .forms import RegistrationForm
from .forms import EmailLoginForm
from django.urls import reverse_lazy
# Create your views here.
code = []

class RegistrationPageView(FormView):
    form_class = RegistrationForm
    template_name = "user_app/signup.html"
    success_url = reverse_lazy("login")
    
    # def get(self, request: HttpRequest):
    #     return render(request, 'registration_app/registration.html', {
    #         'form': RegistrationForm(),
    #         'page' :"reg"
    #     })
    
    def form_valid(self, form):
        form.save(form.cleaned_data["email"], form.cleaned_data["password"])
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type_form"] = "registration"
        return context
    
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

    