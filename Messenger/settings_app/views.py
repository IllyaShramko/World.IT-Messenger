from django.shortcuts import render
from django.views import View
from user_app.models import Profile
# Create your views here.

class SettingsView(View):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = 'settings'
        return context
    def dispatch(self, request, *args, **kwargs):
        profile = Profile.objects.get(user_id = request.user.id)
        if request.method == "GET":
            if request.user.last_name == "":
                print(1)
                return render(
                    request,
                    "settings_app/settings.html"
                )
            else:
                print(0)
                return render(
                    request, 
                    "settings_app/settings.html",
                    {
                        "tag_name": profile.tag_name
                    }
                )