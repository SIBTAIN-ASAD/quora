'''
This file contains the model for user rating and comments
'''
from django.db import models

from accounts.models import CustomUser

# user rating comment model
class UserRatingComment(models.Model):
    '''
    Model to store user rating and comments
    I made it for testing encryption and decryption
    '''
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    rating = models.CharField(max_length=500) # By Manual encryption and decryption
    comment = models.CharField(max_length=500) 
    review  = models.CharField(max_length=500)
    catalog = models.CharField(max_length=500)
    comment_type = models.CharField(max_length=500)
    class Meta:
        '''
        Meta class for UserRatingComment
        '''
        db_table = 'user_rating_comment'
        verbose_name = 'User Rating Comment'
        verbose_name_plural = 'User Rating Comments'

    # manager
    objects = models.Manager()
