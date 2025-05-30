from django.shortcuts import render
from django.views import View
from user_app.models import Profile
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