'''
This file contains the views for the chat app.
'''
from django.shortcuts import render

from chat.models import Room


def chat_view(request):
    '''
    This view returns the index page.
    '''
    return render(request, 'chat.html', {
        'rooms': Room.objects.all(),
    })


def room_view(request, room_name):
    '''
    This view returns the room page.
    '''
    chat_room, created = Room.objects.get_or_create(name=room_name)
    return render(request, 'room.html', {
        'room': chat_room,
    })
