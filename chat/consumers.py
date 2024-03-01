'''
This module contains the chat consumer class.
'''

import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

from chat.models import Room, Message


class ChatConsumer(WebsocketConsumer):
    '''
    Class to handle the chat consumer.
    '''

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.room_name = None
        self.room_group_name = None
        self.room = None
        self.user = None
        self.user_inbox = None

    def connect(self):
        '''
        This method is called when the websocket connection is established.
        '''
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'
        self.room = Room.objects.get(name=self.room_name)
        self.user = self.scope['user']
        self.user_inbox = f'inbox_{self.user.username}'

        # connection has to be accepted
        self.accept()

        # join the room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name,
        )

        # send the user list to the newly joined user
        self.send(json.dumps({
            'type': 'user_list',
            'users': [user.username for user in self.room.online.all()],
        }))

        if self.user.is_authenticated:
            # ----------------------------------------
            # create a user inbox for private messages
            async_to_sync(self.channel_layer.group_add)(
                self.user_inbox,
                self.channel_name,
            )
            # --------------------------------
            # send the join event to the room
            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    'type': 'user_join',
                    'user': self.user.username,
                }
            )
            self.room.online.add(self.user)

    def disconnect(self, close_code):
        '''
        This method is called when the websocket connection is closed.
        '''
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name,
        )

        if self.user.is_authenticated:
            # ---------------------------------------
            # delete the user inbox for private messages
            async_to_sync(self.channel_layer.group_discard)(
                self.user_inbox,
                self.channel_name,
            )
            # --------------------------------
            # send the leave event to the room
            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    'type': 'user_leave',
                    'user': self.user.username,
                }
            )
            self.room.online.remove(self.user)

    def receive(self, text_data=None, bytes_data=None):
        '''
        This method is called when a message is received from the websocket.
        '''
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        if not self.user.is_authenticated:
            return

        # ---------------------------------------
        if message.startswith('/pm '):
            split = message.split(' ', 2)
            target = split[1]
            target_msg = split[2]

            # send private message to the target
            async_to_sync(self.channel_layer.group_send)(
                f'inbox_{target}',
                {
                    'type': 'private_message',
                    'user': self.user.username,
                    'message': target_msg,
                }
            )
            # send private message delivered to the user
            self.send(json.dumps({
                'type': 'private_message_delivered',
                'target': target,
                'message': target_msg,
            }))
            return
        # --------------------------------

        # send chat message event to the room
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'user': self.user.username,
                'message': message,
            }
        )
        Message.objects.create(user=self.user, room=self.room, content=message)

    def chat_message(self, event):
        '''
        This method is called when a chat message event is received from the room group.
        '''
        self.send(text_data=json.dumps(event))

    def user_join(self, event):
        '''
        This method is called when a user join event is received from the room group.
        '''
        self.send(text_data=json.dumps(event))

    def user_leave(self, event):
        '''
        This method is called when a user leave event is received from the room group.
        '''
        self.send(text_data=json.dumps(event))

    def private_message(self, event):
        '''
        This method is called when a private message event is received from the user inbox group.
        '''
        self.send(text_data=json.dumps(event))

    def private_message_delivered(self, event):
        '''
        This method is called when a private message delivered event is received from the user inbox group.
        '''
        self.send(text_data=json.dumps(event))