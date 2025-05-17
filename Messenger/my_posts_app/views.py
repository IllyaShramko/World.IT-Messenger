
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views import View
from django.http import HttpRequest
from django.urls import reverse_lazy
from .forms import PostForm
from .models import User_Post
import os
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
        context['page'] = "my_posts"
        return context

    def post(self, request: HttpRequest):
        button = request.POST.get('button')
        print(button)
        if button == "startform":
            print(button)
            text = request.POST.get('text')
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
                post = form.save(commit=False)
                post.user = request.user
                post.likes = 0
                post.views = 0
                post.tags = []
                text = form.cleaned_data["text"].split("#")
                del text[0]
                for tag in text:
                    print(tag)
                    post.tags.append(tag)
                post.save()

                
            return render(
                request,
                "my_posts_app/my_post_app.html",
                context = {
                    "form": PostForm,
                    "popup": False,
                    "my_posts": User_Post.objects.filter(user= request.user)
                    }
            )

def delete_post(request, post_id):
    post = User_Post.objects.filter(user = request.user, id = post_id)[0]
    print(post)
    if post:
        os.remove(
            os.path.abspath(
                __file__ + "../../../media/" + str(post.images)
            )
        )
        post.delete()
    return redirect(reverse_lazy("my_posts"))