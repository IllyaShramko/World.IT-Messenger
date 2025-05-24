from django.shortcuts import render
from django.views.generic.list import ListView
from user_app.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from my_posts_app.models import User_Post, Images_Post
# Create your views here.

class MainPageView(LoginRequiredMixin, ListView):
    model = User_Post
    context_object_name = "posts_list"
    template_name = "home_app/home.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_auth'] = User.is_authenticated
        context['images'] = Images_Post.objects.all()
        context['page'] = "home"
        return context