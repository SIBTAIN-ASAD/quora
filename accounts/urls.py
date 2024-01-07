# accounts/urls.py

from django.urls import path
from .views import SignUpView, ProfileView, CustomLoginView, UserProfileUpdateView
from django.contrib.auth.views import LogoutView



urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("profile/", ProfileView.as_view(), name="profile"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(next_page="login"), name="logout"),
    path("update_profile/", UserProfileUpdateView.as_view(), name="update_profile"),
]
