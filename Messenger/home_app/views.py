from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect, HttpResponse, HttpRequest
from user_app.models import User, Profile
from django.contrib.auth.mixins import LoginRequiredMixin
from my_posts_app.models import User_Post, Images_Post
# Create your views here.

class MainPageView(LoginRequiredMixin, View):
    template_name = "home_app/home.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_auth'] = User.is_authenticated
        context['images'] = Images_Post.objects.all()
        context["posts_list"] = User_Post.objects.all()
        context['page'] = "home"
        return context
    def dispatch(self, request, *args, **kwargs):
        profile = Profile.objects.get(user_id = request.user.id)
        if request.method == "POST":
            first_name = request.POST.get("name")
            last_name = request.POST.get("lastname")
            tag_name = request.POST.get("tagname")
            user = User.objects.get(pk = request.user.id)
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            profile.tag_name = tag_name
            profile.save()
            print(first_name, last_name, tag_name)
            return render(
                request,
                "home_app/home.html",
                {
                    'new_or_not': False  
                }
            )
        elif request.method == "GET":

            if request.user.last_name == "":
                print(1)
                return render(
                    request,
                    "home_app/home.html",
                    {
                        'new_or_not': True  
                    }
                )
            else:
                print(0)
                return render(
                    request, 
                    'home_app/home.html',
                    {
                        "new_or_not": False,
                        "tag_name": profile.tag_name
                    }
                )
        
        