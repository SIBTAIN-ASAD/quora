'''
File contains urls for tokens app, handling API requests
'''

from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from .views import JWTLoginView, HomeView, LogoutView


urlpatterns = [
    path('login', JWTLoginView.as_view(), name='api-login'),
    path('token/',
          jwt_views.TokenObtainPairView.as_view(),
          name ='token_obtain_pair'),
    path('token/refresh/',
          jwt_views.TokenRefreshView.as_view(),
          name ='token_refresh'),
    path('home', HomeView.as_view(), name ='api-home'),
    path('logout', LogoutView.as_view(), name='api-logout'),
]
