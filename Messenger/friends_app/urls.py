from django.urls import path
from .views import FriendsView, InvitesView, RecommendationsView, AllFriendsView

urlpatterns = [
    path('', FriendsView.as_view(), name = "friends"),
    path('invites/', InvitesView.as_view(), name = "invites"),
    path('recommendations/', RecommendationsView.as_view(), name = "recommendations"),
    path('all_friends/', AllFriendsView.as_view(), name = "all_friends"),
]
