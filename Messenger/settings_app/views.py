from django.shortcuts import render
from django.views import View
from user_app.models import CustomAbstractUser
from my_posts_app.models import Images_Post
from .models import Album
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from .models import AlbumImage
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
                print(date)
                album= Album.objects.create(
                    title = title,
                    subtitle = subtitle,
                    author = request.user,
                    date = date
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
            elif button == "editAlbum":
                title = request.POST.get("title")
                subtitle = request.POST.get("subtitle")
                date = request.POST.get("date")
                album_pk = request.POST.get("albumpk")
                album = Album.objects.get(pk = album_pk) 
                album.title = title
                album.subtitle = subtitle
                album.date = date
                album.save()
                album_images = AlbumImage.objects.filter(album_id = album.id)
                return render(
                    request,
                    "settings_app/album.html",
                    context = {
                        "images": images,
                        "popup": False,
                        'album': album,
                        "album_images": album_images,
                        "page": "settings"
                    }
                )
                
        else:
            album = None
            album_images = None
            try:
                album = Album.objects.get(author_id = request.user.id)
                album_images = AlbumImage.objects.filter(album_id = album.id)
            except:
                print(Exception)
            return render(
                request,
                "settings_app/album.html",
                context = {
                    "images": images,
                    'album': album,
                    "page": "settings",
                    "album_images": album_images,
                }
            )


@csrf_exempt
def upload_images(request):
    if request.method == 'POST':
        album = Album.objects.get(pk = request.POST.get("album_id"))
        images = request.FILES.getlist('images')
        for img in images:
            AlbumImage.objects.create(album=album, image=img)
        return JsonResponse({'status': 'ok', 'album_id': album.id})

def delete_image(request, img_pk):
    image = AlbumImage.objects.get(pk = img_pk)
    image.delete()
    return HttpResponseRedirect(reverse_lazy("albums"))

def delete_album(request, album_pk):
    album = Album.objects.get(pk= album_pk)
    if request.user == album.author:
        album.delete()
    return HttpResponseRedirect(reverse_lazy("albums"))

def edit_album(request, album_pk):
    album = Album.objects.get(pk= album_pk)
    title = album.title
    subtitle = album.subtitle
    return render(request, template_name="settings_app/form_album.html", context={
        "title": title,
        "subtitle": subtitle,
        "album_pk": album_pk,
        "date": f"{album.date}"
    })