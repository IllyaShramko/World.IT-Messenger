
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views import View
from django.http import HttpRequest, HttpResponse
from django.urls import reverse_lazy
from .forms import PostForm
from .models import User_Post, Images_Post
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
        context['images'] = Images_Post.objects.all()
        return context
    
    def post(self, request: HttpRequest):
        button = request.POST.get('button')
        print(button)
        if button == "startform":
            print(button)
            text = request.POST.get('text')
            form = PostForm()
            form.initial.setdefault(
                "text",
                text
            )
            return render(
                request,
                "my_posts_app/my_post_app.html",
                context = {
                    "form": form,
                    "popup": True,
                    "post_modal": "create",
                    "page": "my_posts",
                    "images": Images_Post.objects.all(),
                    "my_posts": User_Post.objects.filter(user= request.user)
                }
            )
        elif button=="submitFormCreate":
            form = PostForm(request.POST, request.FILES)
            if form.is_valid():
                images = request.FILES.getlist("images")
                post = form.save(commit=False)
                post.user = request.user
                post.likes = 0
                post.views = 0
                post.tags = []
                text = form.cleaned_data["text"].split("#")
                post.text = text[0]
                del text[0]
                for tag in text:
                    print(tag)
                    post.tags.append(tag)
                post.save()
                for image in images:
                    Images_Post.objects.create(
                        image = image,
                        post = post
                    )

                
            return render(
                request,
                "my_posts_app/my_post_app.html",
                context = {
                    "form": PostForm,
                    "popup": False,
                    "page": "my_posts",
                    "images": Images_Post.objects.all(),
                    "my_posts": User_Post.objects.filter(user= request.user)
                    }
            )
        elif button =="submitFormEdit":
            form = PostForm(request.POST, request.FILES)
            if form.is_valid():
                post = User_Post.objects.get(pk = form.data["post_pk"])
                post.title = form.data["title"]
                post.topic = form.data["topic"]
                text = form.data["text"].split("#")
                post.text = text[0]
                del text[0]
                for tag in text:
                    print(tag)
                    post.tags.append(tag)

                if request.FILES.getlist("images"):
                    for image in request.FILES.getlist("images"):
                        Images_Post.objects.create(
                            image = image,
                            post = post
                        )
                post.save()

            return render(
                request,
                "my_posts_app/my_post_app.html",
                context = {
                    "form": PostForm,
                    "popup": False,
                    "page": "my_posts",
                    "images": Images_Post.objects.all(),
                    "my_posts": User_Post.objects.filter(user= request.user)
                    }
            )    
                

def delete_post(request, post_id):
    post = User_Post.objects.get(user = request.user, id = post_id)
    print(post)
    if post:
        try:
            os.remove(
                os.path.abspath(
                    __file__ + "../../../media/" + str(post.images)
                )
            )
        except:
            print(Exception)
        post.delete()
    return redirect(reverse_lazy("my_posts"))

def get_post(request, post_id):
    post = User_Post.objects.get(user = request.user, id = post_id)
    form = PostForm()
    form.initial.setdefault(
        "title",
        post.title
    )
    form.initial.setdefault(
        "topic",
        post.topic
    )
    form.initial.setdefault(
        "text",
        post.text
    )
    form.initial.setdefault(
        "links",
        post.links
    )
    images = Images_Post.objects.filter(post_id = post_id)
    if post:
        if images:
            return render(
                request,
                "my_posts_app/form_edit.html",
                context = {
                    "form": form,
                    "popup": True,
                    "post_modal": "edit",            
                    "post_pk": post_id,
                    "images": images,
                    "my_posts": User_Post.objects.filter(user= request.user)
                    })
        
        else:
            return render(
                request,
                "my_posts_app/form_edit.html",
                context = {
                    "form": form,
                    "popup": True,
                    "post_modal": "edit",            
                    "post_pk": post_id,
                    "my_posts": User_Post.objects.filter(user= request.user)
                    })
                
            