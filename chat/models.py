''' 
File contains the Room and Message models. 
Room model is used to store the name of the room and the users online in the room.
Message model is used to store the messages sent in the room.
'''


from django.db import models
from accounts.models import CustomUser
    

class Room(models.Model):
    '''
    Room model is used to store the name of the room and the users online in the room.
    '''
    name = models.CharField(max_length=128)
    online = models.ManyToManyField(to=CustomUser, related_name='online', blank=True)

    def get_online_count(self):
        '''
        This method returns the number of users online in the room.
        '''
        return self.online.count()

    def join(self, user):
        '''
        This method adds the user to the online users in the room.
        '''
        self.online.add(user)
        self.save()

    def leave(self, user):
        '''
        This method removes the user from the online users in the room.
        '''
        self.online.remove(user)
        self.save()

    def __str__(self):
        return f'{self.name} ({self.get_online_count()})'


class Message(models.Model):
    '''
    Message model is used to store the messages sent in the room.
    '''
    user = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE)
    room = models.ForeignKey(to=Room, on_delete=models.CASCADE)
    content = models.CharField(max_length=512)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username}: {self.content} [{self.timestamp}]'
