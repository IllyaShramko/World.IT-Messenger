from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect, HttpResponse, HttpRequest, JsonResponse
from user_app.models import Profile, Friendship, Avatar
from my_posts_app.models import Post, Image, Tag
from my_posts_app.forms import PostForm
from django.urls import reverse_lazy
# Create your views here.

class MainPageView(View):
    template_name = "home_app/home.html"
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy('login'))
        if request.method == "POST":
            profile = Profile.objects.get(user = request.user)
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
                tags = Tag.objects.all()
                return render(
                    request,
                    "home_app/home.html",
                    context = {
                        "form": form,
                        "popup": True,
                        "post_modal": "create",
                        "page": "my_posts",
                        "avatar": Avatar.objects.filter(profile = profile).filter(active = True).first(),
                        "tag_name": Profile.objects.get(user = request.user).tag_name,
                        "images": Image.objects.all(),
                        "tags": tags,
                        "posts_list": Post.objects.all().reverse(),
                        "viewers": Post.objects.filter(author = Profile.objects.get(user = request.user)).count(),
                        "friends_count": Friendship.objects.filter(profile2 = Profile.objects.get(user = request.user)).count(),
                        "posts_count": Post.objects.filter(author = Profile.objects.get(user = request.user)).count(),
                        "page": "home"
                    }
                )
            elif button=="submitFormCreate":
                form = PostForm(request.POST, request.FILES)
                if form.is_valid():
                    images = request.FILES.getlist("images")
                    post = form.save(commit=False)
                    post.author = Profile.objects.get(user = self.request.user)
                    post.content = form.cleaned_data["content"]
                    post.save()
                    tags_ids = request.POST.getlist("tags")
                    del tags_ids[-1]
                    print(tags_ids)
                    tags = Tag.objects.filter(pk__in = tags_ids)
                    print(tags)
                    for tag in tags:
                        print(tag)
                        post.tags.add(tag)
                        post.save()

                    print("картинки:", images)
                    for image in images:

                        # post1 = Post.objects.get(pk = 5)
                        # post1.images.
                        img_db = Image.objects.create(
                            filename = image.name,
                            file = image
                        )
                        post.images.add(img_db)
                        post.save()
                return render(
                    request,
                    "home_app/home.html",
                    context = {
                        "form": PostForm,
                        "popup": False,
                        "page": "my_posts",
                        "avatar": Avatar.objects.filter(profile = profile).filter(active = True).first(),
                        "tag_name": Profile.objects.get(user = request.user).tag_name,
                        "images": Image.objects.all(),
                        "posts_list": Post.objects.all().reverse(),
                        "viewers": Post.objects.filter(author = Profile.objects.get(user = request.user)).count(),
                        "friends_count": Friendship.objects.filter(profile2 = Profile.objects.get(user = request.user)).count(),
                        "posts_count": Post.objects.filter(author = Profile.objects.get(user = request.user)).count(),
                        "page": "home"
                        }
                )

            first_name = request.POST.get("name")
            last_name = request.POST.get("lastname")
            tag_name = request.POST.get("tagname")
            user = request.user
            user.first_name = first_name
            user.last_name = last_name
            profile = Profile.objects.get(user = request.user)
            profile.tag_name = tag_name
            profile.save()
            user.save()
            print(first_name, last_name, tag_name)
            return render(
                request,
                "home_app/home.html",
                {
                    'new_or_not': False,
                    "tag_name": Profile.objects.get(user = request.user).tag_name,
                    "images": Image.objects.all(),
                    "avatar": Avatar.objects.filter(profile = profile).filter(active = True).first(),
                    "posts_list": Post.objects.all().reverse(),
                    "viewers": Post.objects.filter(author = Profile.objects.get(user = request.user)).count(),
                    "friends_count": Friendship.objects.filter(profile2 = Profile.objects.get(user = request.user)).count(),
                    "posts_count": Post.objects.filter(author = Profile.objects.get(user = request.user)).count(),
                    "page": "home"
                }
            )
        elif request.method == "GET":
            profile = Profile.objects.get(user = request.user)
            if request.user.last_name == "":
                print(1)
                return render(
                    request,
                    "home_app/home.html",
                    {
                        'new_or_not': True,
                        "viewers": Post.objects.filter(author = Profile.objects.get(user = request.user)).count(),
                        "friends_count": Friendship.objects.filter(profile2 = Profile.objects.get(user = request.user)).count(),
                        "posts_count": Post.objects.filter(author = Profile.objects.get(user = request.user)).count(),
                        "page": "home"
                    }
                )
            else:
                return render(
                    request, 
                    'home_app/home.html',
                    {
                        "new_or_not": False,
                        "tag_name": Profile.objects.get(user = request.user).tag_name,
                        "viewers": Post.objects.filter(author = Profile.objects.get(user = request.user)).count(),
                        "friends_count": Friendship.objects.filter(profile2 = Profile.objects.get(user = request.user)).count(),
                        "posts_count": Post.objects.filter(author = Profile.objects.get(user = request.user)).count(),
                        "page": "home"
                    }
                )
        
def get_avatar(request: HttpRequest):
    profile = Profile.objects.get(user = request.user)
    avatar = Avatar.objects.filter(active = True).filter(profile = profile).first()
    return JsonResponse({"avatar": avatar.image.url})

def getposts(request: HttpRequest):
    
    return JsonResponse