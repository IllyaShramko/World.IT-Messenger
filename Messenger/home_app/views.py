from django.shortcuts import render
from django.views.generic.list import ListView
from user_app.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class MainPageView(LoginRequiredMixin, ListView):
    model = User
    context_object_name = "user"
    template_name = "home_app/home.html"
    def get_queryset(self):
        queryset = User.objects.all()
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_auth'] = User.is_authenticated
        context['page'] = "home"
        return context