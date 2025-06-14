from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect, HttpResponse, HttpRequest
from user_app.models import CustomAbstractUser
from my_posts_app.models import User_Post, Images_Post
from my_posts_app.forms import PostForm
from django.urls import reverse_lazy
# Create your views here.

class MainPageView(View):
    template_name = "home_app/home.html"
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy('login'))
        if request.method == "POST":
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
                    "home_app/home.html",
                    context = {
                        "form": form,
                        "popup": True,
                        "post_modal": "create",
                        "page": "my_posts",
                        "images": Images_Post.objects.all(),
                        "posts_list": User_Post.objects.all().reverse(),
                        "viewers": request.user.viewers,
                        "friends_count": request.user.friends.count(),
                        "posts_count": User_Post.objects.filter(user = request.user).count(),
                        "page": "home"
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
                    text = request.POST.get("text")
                    post.text = text

                    post.tags = request.POST.get("tags").split(",")
                    post.links = request.POST.get("links").split(",")
                    post.save()
                    print("картинки:", images)
                    for image in images:
                        Images_Post.objects.create(
                            image = image,
                            post = post,
                            author = request.user
                        )

                    
                return render(
                    request,
                    "home_app/home.html",
                    context = {
                        "form": PostForm,
                        "popup": False,
                        "page": "my_posts",
                        "images": Images_Post.objects.all(),
                        "posts_list": User_Post.objects.all().reverse(),
                        "viewers": request.user.viewers,
                        "friends_count": request.user.friends.count(),
                        "posts_count": User_Post.objects.filter(user = request.user).count(),
                        "page": "home"
                        }
                )

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
                    "posts_list": User_Post.objects.all().reverse(),
                    "viewers": request.user.viewers,
                    "friends_count": request.user.friends.count(),
                    "posts_count": User_Post.objects.filter(user = request.user).count(),
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
                        "posts_list": User_Post.objects.all().reverse(),
                        "viewers": request.user.viewers,
                        "friends_count": request.user.friends.count(),
                        "posts_count": User_Post.objects.filter(user = request.user).count(),
                        "page": "home"
                    }
                )
            else:
                print(request.user.friends.count(), User_Post.objects.filter(user = request.user).count())
                return render(
                    request, 
                    'home_app/home.html',
                    {
                        "new_or_not": False,
                        "images": Images_Post.objects.all(),
                        "posts_list": User_Post.objects.all().reverse(),
                        "viewers": request.user.viewers,
                        "friends_count": request.user.friends.count(),
                        "posts_count": User_Post.objects.filter(user = request.user).count(),
                        "page": "home"
                    }
                )
        
        