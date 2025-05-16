
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.http import HttpRequest
from .forms import PostForm
from .models import User_Post
# Create your views here.
class MyPostsView(ListView):
    model = User_Post
    template_name = "my_posts_app/my_post_app.html"
    context_object_name = "my_posts"

    def get_queryset(self):
        queryset = User_Post.objects.filter(user= self.request.user)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["popup"] = False
        return context

    def post(self, request: HttpRequest):
        button = request.POST.get('button')
        print(button)
        if button == "startform":
            print(button)
            return render(
                request,
                "my_posts_app/my_post_app.html",
                context = {
                    "form": PostForm,
                    "popup": True,
                    "my_posts": User_Post.objects.filter(user= request.user)
                }
            )
        elif button=="submitform":
            form = PostForm(request.POST, request.FILES)
            
            
            if form.is_valid():
                form.save()
                return render(
                    request,
                    "my_posts_app/my_post_app.html",
                    context = {
                        "form": PostForm,
                        "popup": False,
                        "my_posts": User_Post.objects.filter(user= request.user)
                        }
                )