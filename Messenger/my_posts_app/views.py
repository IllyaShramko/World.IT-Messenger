
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views import View
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from .forms import PostForm
from .models import Post, Image, Tag
from user_app.models import Profile, Friendship, Avatar
from django.contrib.auth import get_user_model
from .models import Album, Image
import os
# Create your views here.
class MyPostsView(ListView):
    model = Post
    template_name = "my_posts_app/my_post_app.html"
    context_object_name = "my_posts"

    def get_queryset(self):
        queryset = Post.objects.filter(author= Profile.objects.get(user = self.request.user))
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["popup"] = False
        context['page'] = "my_posts"
        context['images'] = Image.objects.all()
        context["viewers"] = Post.objects.filter(author= Profile.objects.get(user = self.request.user)).count()
        context["posts_count"] = Post.objects.filter(author= Profile.objects.get(user = self.request.user)).count()
        context["friends_count"] = Friendship.objects.filter(accepted = True).filter(profile1 = Profile.objects.get(user= self.request.user)).count()
        context["tag_name"] = Profile.objects.get(user = self.request.user).tag_name
        profile = Profile.objects.get(user = self.request.user)
        context["avatar"] = Avatar.objects.filter(profile = profile).filter(active = True).first()
        return context
    
    def post(self, request: HttpRequest):
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
                "my_posts_app/my_post_app.html",
                context = {
                    "form": form,
                    "popup": True,
                    "post_modal": "create",
                    "page": "my_posts",
                    "avatar": Avatar.objects.filter(profile = profile).filter(active = True).first(),
                    "images": Image.objects.all(),
                    "viewers": Post.objects.filter(author= Profile.objects.get(user = self.request.user)).count(),
                    "tag_name": Profile.objects.get(user = request.user).tag_name,
                    "friends_count": Friendship.objects.filter(accepted = True).filter(profile1 = Profile.objects.get(user= self.request.user)).count(),
                    "my_posts": Post.objects.filter(author= Profile.objects.get(user = self.request.user)),
                    "posts_count": Post.objects.filter(author= Profile.objects.get(user = self.request.user)).count(),
                    "tags": tags,
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
                "my_posts_app/my_post_app.html",
                context = {
                    "form": PostForm,
                    "popup": False,
                    "page": "my_posts",
                    "images": Image.objects.all(),
                    "avatar": Avatar.objects.filter(profile = profile).filter(active = True).first(),
                    "viewers": Post.objects.filter(author= Profile.objects.get(user = self.request.user)).count(),
                    "tag_name": Profile.objects.get(user = request.user).tag_name,
                    "friends_count": Friendship.objects.filter(accepted = True).filter(profile1 = Profile.objects.get(user= self.request.user)).count(),
                    "my_posts": Post.objects.filter(author= Profile.objects.get(user = self.request.user)),
                    "posts_count": Post.objects.filter(author= Profile.objects.get(user = self.request.user)).count(),
                    }
            )
        elif button =="submitFormEdit":
            form = PostForm(request.POST, request.FILES)
            if form.is_valid():
                deleted_images = request.POST.get("deleted_images")
                if deleted_images:
                    deleted_images = deleted_images.split(",")
                    for imgdel in deleted_images:
                        img = Image.objects.get(pk = imgdel)
                        img.delete()
                post = Post.objects.get(pk = form.data["post_pk"])
                post.title = form.data["title"]
                post.topic = form.data["topic"]
                text = form.data["text"]
                post.text = text
                print(request.POST.get("tags"))
                post.tags = request.POST.get("tags").split(",")

                if request.FILES.getlist("images"):
                    for image in request.FILES.getlist("images"):
                        Image.objects.create(
                            image = image,
                            post = post,
                            author = request.user,
                        )
                post.save()

            return render(
                request,
                "my_posts_app/my_post_app.html",
                context = {
                    "form": PostForm,
                    "popup": False,
                    "page": "my_posts",
                    "images": Image.objects.all(),
                    "avatar": Avatar.objects.filter(profile = profile).filter(active = True).first(),
                    "viewers": Post.objects.filter(author= Profile.objects.get(user = self.request.user)).count(),
                    "tag_name": Profile.objects.get(user = request.user).tag_name,
                    "friends_count": Friendship.objects.filter(accepted = True).filter(profile1 = Profile.objects.get(user= self.request.user)).count(),
                    "my_posts": Post.objects.filter(author= Profile.objects.get(user = self.request.user)),
                    "posts_count": Post.objects.filter(user = request.user).count(),
                    }
            )    
                

def delete_post(request, post_id):
    post = Post.objects.get(author =Profile.objects.get(user= request.user), id = post_id)
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
    post = Post.objects.filter(author= Profile.objects.get(user = request.user), pk = post_id),
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
    images = Image.objects.filter(post_id = post_id)
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
                    "tag_name": Profile.objects.get(user = request.user).tag_name,
                    "post_tags": post.tags,
                    "my_posts": Post.objects.filter(user= request.user)
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
                    "post_tags": post.tags,
                    "my_posts": Post.objects.filter(user= request.user)
                    })
                

class UsersPostsView(ListView):
    model = Post
    template_name = 'my_posts_app/user_posts.html'
    context_object_name = "posts"

    def get_queryset(self):
        queryset = Post.objects.filter(user_id = self.kwargs["user_pk"])    
        return queryset
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page"] = 'friends'
        user = get_user_model().objects.get(pk = self.kwargs["user_pk"])
        context["user"] = user
        if user in self.request.user.friends.all():
            context["is_friend"] = True
        else:
            context["is_friend"] = False
        context['images'] = Image.objects.all()

        album = Album.objects.filter(author_id = user.id).first()
        print(album)
        context['album'] = album
        if album:
            context["album_images"] = Image.objects.filter(album_id = album.pk)
        return context
    def post(self, request: HttpRequest, user_pk):
        button = request.POST.get("button").split("-")
        if button[0] == "add":
            user = get_user_model().objects.get(pk = request.POST.get("button").split('-')[1])
            request.user.friends.add(user)
        elif button[0] == "delete":
            user = get_user_model().objects.get(pk = request.POST.get("button").split('-')[1])
            request.user.friends.remove(user)
        
        user = get_user_model().objects.get(pk = user_pk)
        if user in self.request.user.friends.all():
            friend = True
        else:
            friend = False

        return render(request, 'my_posts_app/user_posts.html', {
            'page' : "friends",
            'user' : user,
            'is_friend': friend,
            "images": Image.objects.all(),
            "posts": Post.objects.filter(user_id = user_pk),
            "tag_name": Profile.objects.get(user = request.user).tag_name,
        })
    
def delete_img(request, image_pk):
    img = Image.objects.get(pk = image_pk)
    img.delete()

    return HttpResponseRedirect(reverse_lazy("albums"))
