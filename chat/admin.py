'''
This file is used to register the models in the admin panel.
'''
from django.contrib import admin

from chat.models import Room, Message

admin.site.register(Room)
admin.site.register(Message)
