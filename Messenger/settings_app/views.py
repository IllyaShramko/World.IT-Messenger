from django.shortcuts import render
from django.views import View
from user_app.models import Profile, Avatar
from my_posts_app.models import Image, Album, Tag
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse_lazy
# Create your views here.

class SettingsView(View):

    def dispatch(self, request, *args, **kwargs):
        profile = Profile.objects.get(user = request.user)
        if request.method == "GET":
        
            print(Avatar.objects.filter(profile = profile).filter(active = True).first())
            return render(
                request, 
                "settings_app/settings.html",
                {
                    "profile": request.user,
                    "birthday": f"{Profile.objects.get(user = request.user)}",
                    "tag_name": f"{profile.tag_name}",
                    "avatar": Avatar.objects.filter(profile = profile).filter(active = True).first(),
                    "page":"settings"
                }
            )
        else:
            button = request.POST.get("button")
            if button == "change-avatar-save":
                avatar = request.FILES.get("avatar")
                print(avatar)
                if avatar:
                    Avatar.objects.filter(profile = profile).delete()
                    Avatar.objects.create(
                        image = avatar,
                        profile = profile
                    )
                    
            else:
                button = request.POST.get("button")
                print(button)
                if button == "save":
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
                    except:
                        print(Exception)
                elif button == "savepass":
                    password1 = request.POST.get("password")
                    password2 = request.POST.get("passwordconfirm")
                    print(password1, password2)
                    if password1 == password2:
                        user = request.user
                        user.set_password(password1)
                        user.save()
                        print("SUCCESS")
                    else:
                        pass    
            return render(
                request, 
                "settings_app/settings.html",
                {
                    "profile": request.user,
                    "birthday": f"{Profile.objects.get(user = request.user)}",
                    "tag_name": f"{profile.tag_name}",
                    "page":"settings",
                    "avatar": Avatar.objects.filter(profile = profile).filter(active = True).first(),
                }
            )

class AlbumsSettingsView(View):
    def dispatch(self, request, *args, **kwargs):
        # images = Image.objects.filter(author_id = request.user.id)
        if request.method == "POST":
            button = request.POST.get("button")
            if button == "album_create_1":
                albums = Album.objects.filter(author_id = Profile.objects.get(user = request.user))
                return render(
                    request,
                    "settings_app/album.html",
                    context = {
                        # "images": images,
                        "popup": True,
                        'albums': albums,
                        "tags": Tag.objects.all(),
                        "page": "settings"
                    }
                )
            elif button == "submitAlbum":
                title = request.POST.get("title")
                subtitle_pk = request.POST.get("topic")
                print(subtitle_pk)
                topic = Tag.objects.get(pk = subtitle_pk)
                date = request.POST.get("date")
                print(date)
                album= Album.objects.create(
                    name = title,
                    author = Profile.objects.get(user= request.user),
                    topic = topic
                )
                albums = Album.objects.filter(author_id = Profile.objects.get(user = request.user))
                return render(
                    request,
                    "settings_app/album.html",
                    context = {
                        # "images": images,
                        "popup": False,
                        'albums': albums,
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
                album_images = Image.objects.filter(album_id = album.id)
                return render(
                    request,
                    "settings_app/album.html",
                    context = {
                        # "images": images,
                        "popup": False,
                        'album': album,
                        "album_images": album_images,
                        "page": "settings"
                    }
                )
                
        else:
            album = None
            try:
                album = Album.objects.filter(author_id = Profile.objects.get(user = request.user))
            except:
                print(Exception)
            return render(
                request,
                "settings_app/album.html",
                context = {
                    'albums': album,
                    "page": "settings",
                }
            )


@csrf_exempt
def upload_images(request):
    if request.method == 'POST':
        album = Album.objects.get(pk = request.POST.get("album_id"))
        images = request.FILES.getlist('images')
        for img in images:
            img_db = Image.objects.create(filename="123", file = img)
            album.images.add(img_db)
        return JsonResponse({'status': 'ok', 'album_id': album.id})

def delete_image(request, img_pk):
    image = Image.objects.get(pk = img_pk)
    image.delete()
    return HttpResponseRedirect(reverse_lazy("albums"))

def delete_album(request, album_pk):
    album = Album.objects.get(pk= album_pk)
    # if request.user == album.author:
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

def edit_private_album(request, album_pk):
    album = Album.objects.get(pk= album_pk)
    text= ""
    print(1)
    if request.user == album.author:
        print(1)
        if album.publish:
            print(1)
            text = "Цей альбом бачите тільки ви"
        else:
            print(1)
            text = "Зробити приватним"
        album.publish = not album.publish
        album.save()

    
    print(1)
    return JsonResponse({
        "text": text,
        "publish": album.publish
    })