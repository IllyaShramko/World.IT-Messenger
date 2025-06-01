from django.shortcuts import render
from django.views import View
from user_app.models import Profile
from my_posts_app.models import Images_Post
from .models import Album
# Create your views here.

class SettingsView(View):

    def dispatch(self, request, *args, **kwargs):
        profile = Profile.objects.get(user_id = request.user.id)
        print(profile.birthday)
        if request.method == "GET":
            if request.user.last_name == "":
                print(1)
                return render(
                    request,
                    "settings_app/settings.html",
                    {
                        "profile": profile,
                        "birthday": profile.birthday,
                        "page":"settings"
                    }
                )
            else:
                print(0)
                return render(
                    request, 
                    "settings_app/settings.html",
                    {
                        "profile": profile,
                        "birthday": f"{profile.birthday}",
                        "tag_name": profile.tag_name,
                        "page":"settings"
                    }
                )
        else:
            name = request.POST.get("name")
            last_name = request.POST.get("surname")
            birthday = request.POST.get("birthday")
            email = request.POST.get("email")
            try:
                user = request.user
                user.first_name = name
                user.last_name = last_name
                user.username = email
                user.email = email
                user.save()
                profile.birthday = birthday
                profile.save()
            except:
                print(Exception)
            return render(
                request, 
                "settings_app/settings.html",
                {
                    "profile": profile,
                    "birthday": f"{profile.birthday}",
                    "tag_name": profile.tag_name,
                    "page":"settings"
                }
            )

class AlbumsSettingsView(View):
    def dispatch(self, request, *args, **kwargs):
        images = Images_Post.objects.filter(author_id = request.user.id)
        if request.method == "POST":
            button = request.POST.get("button")
            if button == "album_create_1":
                return render(
                    request,
                    "settings_app/album.html",
                    context = {
                        "images": images,
                        "popup": True,
                        "page": "settings"
                    }
                )
            elif button == "submitAlbum":
                title = request.POST.get("title")
                subtitle = request.POST.get("subtitle")
                date = request.POST.get("date")
                album= Album.objects.create(
                    title = title,
                    subtitle = subtitle,
                    author = request.user
                )
                return render(
                    request,
                    "settings_app/album.html",
                    context = {
                        "images": images,
                        "popup": False,
                        'album': album,
                        "page": "settings"
                    }
                )
        else:
            album = None
            try:
                album = Album.objects.get(author_id = request.user.id)
            except:
                print(Exception)
            return render(
                request,
                "settings_app/album.html",
                context = {
                    "images": images,
                    'album': album,
                    "page": "settings"
                }
            )
