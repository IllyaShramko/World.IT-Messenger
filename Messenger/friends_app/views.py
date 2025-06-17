from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.contrib.auth import get_user_model
from user_app.models import Profile, Friendship, Avatar
from django.http import HttpRequest
# Create your views here.

class FriendsView(View):

    def get(self, request: HttpRequest):
        friends_requests1 = Friendship.objects.filter(profile2 =  Profile.objects.get(user = request.user)).filter(accepted = False)
        friends_requests2 = Friendship.objects.filter(profile1 = Profile.objects.get(user = request.user)).filter(accepted = False)
        friends_requests = friends_requests1 | friends_requests2
        friends = Friendship.objects.filter(profile1 =  Profile.objects.get(user = request.user)).filter(accepted = True) | Friendship.objects.filter(profile2 =  Profile.objects.get(user = request.user)).filter(accepted = True)
        requested_profiles_ids = friends_requests.values_list('profile1', flat=True).union(
            friends_requests.values_list('profile2', flat=True)
        )
        friends_ids = friends.values_list('profile1', flat=True).union(
            friends.values_list('profile2', flat=True)
        )
        users = Profile.objects.exclude(pk = Profile.objects.get(user = request.user).pk).exclude(pk__in = requested_profiles_ids).exclude(pk__in = friends_ids)
        print(friends_requests)
        
        profiles_with_avatars = list(users)

        for request1 in friends_requests:
            profiles_with_avatars.append(request1.profile1)
            profiles_with_avatars.append(request1.profile2)

        for request1 in friends:
            profiles_with_avatars.append(request1.profile1)
            profiles_with_avatars.append(request1.profile2)    

            
        avatars = Avatar.objects.filter(profile__in = users).filter(active = True) | Avatar.objects.filter(profile__in=set(profiles_with_avatars), active=True)

        return render(request, "friends_app/friends.html", {
            'page' : "friends",
            'recommendations' : users,
            'friends': friends,
            'friends_requests': friends_requests,
            'avatars': avatars,
            "user": Profile.objects.get(user = request.user)
        })
    def post(self, request: HttpRequest):
        button = request.POST.get("button").split("-")
        if button[0] == "add":
            user = Profile.objects.get(pk = button[1])
            if not Friendship.objects.filter(profile1 = Profile.objects.get(user = request.user)).filter(profile2 = user).exists():
                if not Friendship.objects.filter(profile1 = user).filter(profile2 = Profile.objects.get(user = request.user)).exists():
                    Friendship.objects.create(
                        profile1 = Profile.objects.get(user = request.user),
                        profile2 = user
                    )
        elif button[0] == "deletefriend":
            if Friendship.objects.filter(pk = button[1]).exists():
                request_friend = Friendship.objects.get(pk = button[1])
                request_friend.delete()
        elif button[0] == "deleterequest":
            if Friendship.objects.filter(pk = button[1]).exists():
                request_friend = Friendship.objects.get(pk = button[1])
                request_friend.delete()
                
        elif button[0] == "accept":
            if Friendship.objects.filter(pk = button[1]).exists():
                request_friend = Friendship.objects.get(pk = button[1])
                request_friend.accepted = True
                request_friend.save()
                


        friends_requests1 = Friendship.objects.filter(profile2 =  Profile.objects.get(user = request.user)).filter(accepted = False)
        friends_requests2 = Friendship.objects.filter(profile1 = Profile.objects.get(user = request.user)).filter(accepted = False)
        friends_requests = friends_requests1 | friends_requests2
        friends = Friendship.objects.filter(profile1 =  Profile.objects.get(user = request.user)).filter(accepted = True) | Friendship.objects.filter(profile2 =  Profile.objects.get(user = request.user)).filter(accepted = True)
        requested_profiles_ids = friends_requests.values_list('profile1', flat=True).union(
            friends_requests.values_list('profile2', flat=True)
        )
        friends_ids = friends.values_list('profile1', flat=True).union(
            friends.values_list('profile2', flat=True)
        )
        users = Profile.objects.exclude(pk = Profile.objects.get(user = request.user).pk).exclude(pk__in = requested_profiles_ids).exclude(pk__in = friends_ids)
        print(friends_requests)
        
        profiles_with_avatars = list(users)

        for request1 in friends_requests:
            profiles_with_avatars.append(request1.profile1)
            profiles_with_avatars.append(request1.profile2)

        for request1 in friends:
            profiles_with_avatars.append(request1.profile1)
            profiles_with_avatars.append(request1.profile2)    

            
        avatars = Avatar.objects.filter(profile__in = users).filter(active = True) | Avatar.objects.filter(profile__in=set(profiles_with_avatars), active=True)

        return render(request, "friends_app/friends.html", {
            'page' : "friends",
            'recommendations' : users,
            'friends': friends,
            'friends_requests': friends_requests,
            'avatars': avatars,
            "user": Profile.objects.get(user = request.user)
        })
class InvitesView(TemplateView):
    template_name = "friends_app/invites.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = 'friends'
        return context

class RecommendationsView(TemplateView):

    def get(self, request: HttpRequest):
        users = get_user_model().objects.exclude(pk = self.request.user.pk).exclude(pk__in = self.request.user.friends.all())
        return render(request, "friends_app/recommendations.html", {
            'page' : "friends",
            'recommendations' : users
        })
    def post(self, request: HttpRequest):
        button = request.POST.get("button").split("-")
        if button[0] == "add":
            user = get_user_model().objects.get(pk = request.POST.get("button").split('-')[1])
            request.user.friends.add(user)
        

        
        users = get_user_model().objects.exclude(pk = self.request.user.pk).exclude(pk__in = self.request.user.friends.all())
        return render(request, "friends_app/recommendations.html", {
            'page' : "friends",
            'recommendations' : users
        })
class AllFriendsView(TemplateView):

    def get(self, request: HttpRequest):
        friends = request.user.friends.all()
        return render(request, "friends_app/all_friends.html", {
            'page' : "friends",
            'friends': friends,
        })
    def post(self, request: HttpRequest):
        button = request.POST.get("button").split("-")
        
        if button[0] == "delete":
            user = get_user_model().objects.get(pk = request.POST.get("button").split('-')[1])
            request.user.friends.remove(user)
        

        
        friends = request.user.friends.all()
        return render(request, "friends_app/all_friends.html", {
            'page' : "friends",
            'friends': friends,
        })