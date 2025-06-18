from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from user_app.models import Friendship, Profile, Avatar
# Create your views here.

class ChatsView(TemplateView):
    template_name = "chat_app/chats.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page"] = "chats"
        context['contacts'] = Friendship.objects.filter(profile2 = Profile.objects.get(user = self.request.user)).filter(accepted = True) | Friendship.objects.filter(profile1 = Profile.objects.get(user = self.request.user)).filter(accepted = True)
        print(Friendship.objects.filter(profile2 = Profile.objects.get(user = self.request.user)).filter(accepted = True) | Friendship.objects.filter(profile1 = Profile.objects.get(user = self.request.user)).filter(accepted = True))
        context['chat'] = False
        context["user"] = Profile.objects.get(user = self.request.user)

        friends = Friendship.objects.filter(profile1 =  Profile.objects.get(user = self.request.user)).filter(accepted = True) | Friendship.objects.filter(profile2 =  Profile.objects.get(user = self.request.user)).filter(accepted = True)

        profiles_with_avatars = []
        for request1 in friends:
            profiles_with_avatars.append(request1.profile1)
            profiles_with_avatars.append(request1.profile2)   
            
        avatars = Avatar.objects.filter(profile__in = profiles_with_avatars).filter(active = True)

        context["avatars"] = avatars
        return context  
    
    def post(self, request: HttpRequest):
        button = request.POST.get('button')
        print(button)
        if button == "contactOpen":
            return render(
                request,
                "chat_app/chats.html",
                context = {
                    "messages": ...,
                    "groups": ...,
                }
            )
        
class ChatView(TemplateView):
    template_name = "chat_app/chat.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page"] = "chats"
        context['contacts'] = Friendship.objects.filter(profile2 = Profile.objects.get(user = self.request.user)).filter(accepted = True) | Friendship.objects.filter(profile1 = Profile.objects.get(user = self.request.user)).filter(accepted = True)
        print(Friendship.objects.filter(profile2 = Profile.objects.get(user = self.request.user)).filter(accepted = True) | Friendship.objects.filter(profile1 = Profile.objects.get(user = self.request.user)).filter(accepted = True))
        context['chat'] = True
        context["user"] = Profile.objects.get(user = self.request.user)
        chat = Friendship.objects.get(pk = self.kwargs.get("chat_pk"))
        if chat.profile1 != context["user"]:
            companion = chat.profile1
        else:
            companion = chat.profile2
        context['companion'] = companion

        friends = Friendship.objects.filter(profile1 =  Profile.objects.get(user = self.request.user)).filter(accepted = True) | Friendship.objects.filter(profile2 =  Profile.objects.get(user = self.request.user)).filter(accepted = True)

        profiles_with_avatars = []
        for request1 in friends:
            profiles_with_avatars.append(request1.profile1)
            profiles_with_avatars.append(request1.profile2)   
            
        avatars = Avatar.objects.filter(profile__in = profiles_with_avatars).filter(active = True)

        context["avatars"] = avatars
        return context  
    