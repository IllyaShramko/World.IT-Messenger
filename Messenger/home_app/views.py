from django.shortcuts import render
from django.views.generic.list import ListView
from user_app.models import User
# Create your views here.

class MainPageView(ListView):
    model = User
    context_object_name = "user"
    template_name = "home_app/home.html"
    def get_queryset(self):
        queryset = User.objects.all()
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_auth'] = User.is_authenticated
        return context