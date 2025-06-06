from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.contrib.auth import get_user_model
from django.http import HttpRequest
# Create your views here.

class FriendsView(View):

    def get(self, request: HttpRequest):
        users = []
        for user in get_user_model().objects.exclude(pk = self.request.user.pk).exclude(pk__in = self.request.user.friends.all()):
            if len(users) < 3:
                users.append(user)
            else:
                break
        friends = self.request.user.friends.all()[:3]
        return render(request, "friends_app/friends.html", {
            'page' : "friends",
            'recommendations' : users,
            'friends': friends,
        })
    def post(self, request: HttpRequest):
        button = request.POST.get("button").split("-")
        if button[0] == "add":
            user = get_user_model().objects.get(pk = request.POST.get("button").split('-')[1])
            request.user.friends.add(user)
        elif button[0] == "delete":
            user = get_user_model().objects.get(pk = request.POST.get("button").split('-')[1])
            request.user.friends.remove(user)
        

        print(user)
        users = []
        for user in get_user_model().objects.exclude(pk = self.request.user.pk).exclude(pk__in = self.request.user.friends.all()):
            if len(users) < 3:
                users.append(user)
            else:
                break
        friends = self.request.user.friends.all()[:3]
        return render(request, "friends_app/friends.html", {
            'page' : "friends",
            'recommendations' : users,
            'friends': friends,
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