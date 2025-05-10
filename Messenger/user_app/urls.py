from .views import RegistrationPageView, AuthPageView, CustomLogoutView
from django.urls import path


urlpatterns = [
    path('signup/', RegistrationPageView.as_view(), name = 'reg'),
    path('login/', AuthPageView.as_view(), name = 'login'),
    path('logout/', CustomLogoutView.as_view(), name = "logout")
]