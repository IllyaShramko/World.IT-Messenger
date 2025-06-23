from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from user_app.models import Friendship, Profile, Avatar
from .models import ChatGroup, ChatMessage
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

        context["groups"] = ChatGroup.objects.filter(members = context["user"]).exclude(is_personal_chat= True)

        print(ChatGroup.objects.filter(members = context["user"]))

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
        elif button == "createGroup":
            contacts_to_add = request.POST.getlist("contactsAdded")
            avatar = request.FILES.get("avatar")
            name = request.POST.get("groupname")

            print(avatar)
            if not avatar:
                avatar= "images/group_avatars/Indicator_wngVNLF.png"

            group = ChatGroup.objects.create(
                name = name,
                admin = Profile.objects.get(user = request.user),
                avatar = avatar
            )
            group.members.add(Profile.objects.get(user = self.request.user))
            for contactid in contacts_to_add:
                contact = Profile.objects.get(pk = contactid)
                group.members.add(contact)
            group.save()
        context = {}
        
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

        context["groups"] = ChatGroup.objects.filter(members = context["user"]).exclude(is_personal_chat= True)

        
        return render(
            request,
            "chat_app/chats.html",
            context=context
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
        chat = ChatGroup.objects.get(pk= kwargs.get("group_pk"))
        context["compainions"] = chat.members.exclude(pk = context["user"].pk)
        if chat.is_personal_chat:
            context["groupname"] = f"{context['compainions'].first().user.first_name} {context['compainions'].first().user.last_name}"
        else:
            context["groupname"] = chat.name
        context["groupavatar"] = chat.avatar.url

        friends = Friendship.objects.filter(profile1 =  Profile.objects.get(user = self.request.user)).filter(accepted = True) | Friendship.objects.filter(profile2 =  Profile.objects.get(user = self.request.user)).filter(accepted = True)

        profiles_with_avatars = []
        for request1 in friends:
            profiles_with_avatars.append(request1.profile1)
            profiles_with_avatars.append(request1.profile2)   
            
        avatars = Avatar.objects.filter(profile__in = profiles_with_avatars).filter(active = True)

        context["avatars"] = avatars

        context["history_messages"] = ChatMessage.objects.filter(chat_group_id = kwargs.get('group_pk'))
        context["group_pk"] = kwargs.get('group_pk')

        context["groups"] = ChatGroup.objects.filter(members = context["user"]).exclude(is_personal_chat= True)

        if context["user"] == chat.admin:
            context["is_me_admin"] = True
        else:
            context["is_me_admin"] = False

        return context  
    
    def dispatch(self, request, *args, **kwargs):
        chat = ChatGroup.objects.filter(pk=  self.kwargs.get("group_pk")).exists()
        print(chat)

        if not chat:
            return redirect("all_chats")

        
        return super().dispatch(request, *args, **kwargs)


def redirect_to_personal_chat(request, user1_pk, user2_pk):
    '''
        перенаправлення до особистого чату між двома користувачами
    '''
    # отримуємо 1-ого користувача з динамічного url
    user1 = Profile.objects.get(pk = user1_pk)
    # отримуємо 2-ого користувача з динамічного url
    user2 = Profile.objects.get(pk = user2_pk)
    # шукаємо групу особистого чату між цими користувачами
    group : ChatGroup = ChatGroup.objects.filter(is_personal_chat = True).filter(members = user1).filter(members = user2).first()
    # перевіряємо, якщо особистого чату між цими користувачами немає
    if not group:
        # створюємо групу (особистий чат)
        group = ChatGroup.objects.create(name = f"Chats {user1}, {user2}", is_personal_chat = True, admin= user1, avatar = "images/group_avatars/Indicator_wngVNLF.png")
        # додаємо користувачів до групи
        group.members.add(user1, user2)
        # зберігаємо зміни у групі
        group.save()
    # перенаправляємо користувача на сторінку цього персонального чату
    return redirect('chat', group.pk)

def delete_group(request, group_pk):

    group = ChatGroup.objects.get(pk = group_pk)
    profile = Profile.objects.get(user = request.user)
    if group.admin == profile:
        group.delete()
    return redirect("all_chats")

def leave_group(request, group_pk):
    group = ChatGroup.objects.get(pk = group_pk)
    profile = Profile.objects.get(user = request.user)
    if profile in group.members.all():
        group.members.remove(profile)
        group.save() 

    return redirect("all_chats")

def get_group(request, group_pk):
    group = ChatGroup.objects.get(pk = group_pk)
    avatars = Avatar.objects.filter(profile__in = group.members.all()).filter(active = True)
    print(avatars)
    return render(request, "chat_app/edit_group.html", context={
        "group": group,
        "groupmembers": group.members.exclude(pk = Profile.objects.get(user = request.user).pk),
        "avatars": avatars
    })

def edit_chat(request, group_pk):
    group = ChatGroup.objects.get(pk=group_pk)

    edited_name = request.POST.get("groupname")
    edited_avatar = request.FILES.get("avatar")
    edited_members = request.POST.getlist("contacts")
    
    edited_members_profiles = Profile.objects.filter(pk__in=edited_members) | Profile.objects.filter(user=request.user)

    if edited_name and edited_name != group.name:
        group.name = edited_name

    if edited_avatar:
        group.avatar = edited_avatar

    group.members.set(edited_members_profiles)
    group.save()

    return redirect("chat", group_pk)
