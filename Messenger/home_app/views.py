from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect, HttpResponse, HttpRequest
from user_app.models import CustomAbstractUser
from my_posts_app.models import User_Post, Images_Post
from django.urls import reverse_lazy
# Create your views here.

class MainPageView(View):
    template_name = "home_app/home.html"
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy('login'))
        if request.method == "POST":
            first_name = request.POST.get("name")
            last_name = request.POST.get("lastname")
            tag_name = request.POST.get("tagname")
            user = request.user
            user.first_name = first_name
            user.last_name = last_name
            user.tag_name = tag_name
            user.save()
            print(first_name, last_name, tag_name)
            return render(
                request,
                "home_app/home.html",
                {
                    'new_or_not': False,
                    "tag_name": request.user.tag_name,
                    "images": Images_Post.objects.all(),
                    "posts_list": User_Post.objects.all(),
                    "page": "home"
                }
            )
        elif request.method == "GET":

            if request.user.last_name == "":
                print(1)
                return render(
                    request,
                    "home_app/home.html",
                    {
                        'new_or_not': True,
                        "images": Images_Post.objects.all(),
                        "posts_list": User_Post.objects.all(),
                        "page": "home"
                    }
                )
            else:
                print(0)
                return render(
                    request, 
                    'home_app/home.html',
                    {
                        "new_or_not": False,
                        "tag_name": request.user.tag_name,
                        "images": Images_Post.objects.all(),
                        "posts_list": User_Post.objects.all(),
                        "page": "home"
                    }
                )
        
        