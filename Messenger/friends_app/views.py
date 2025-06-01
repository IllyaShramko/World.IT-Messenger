from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class FriendsView(TemplateView):
    template_name = "friends_app/friends.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = 'friends'
        return context
    
class InvitesView(TemplateView):
    template_name = "friends_app/invites.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = 'friends'
        return context

class RecommendationsView(TemplateView):
    template_name = "friends_app/recommendations.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = 'friends'
        return context
    
class AllFriendsView(TemplateView):
    template_name = "friends_app/all_friends.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = 'friends'
        return context