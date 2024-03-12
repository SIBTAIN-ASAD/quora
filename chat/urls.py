'''
This file is used to define the URL patterns for the chat application.
'''
from django.urls import path

from . import views

urlpatterns = [
    path('', views.chat_view, name='chat-index'),
    path('<str:room_name>/', views.room_view, name='chat-room'),
]
