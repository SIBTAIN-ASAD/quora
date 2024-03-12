'''
This file is used to handle api views request in tokens app
'''

from rest_framework import serializers

from tokens.models import UserRatingComment

class UserRatingCommentSerializer(serializers.ModelSerializer):
    '''
    Serializer for UserRatingComment model
    '''
    class Meta:
        '''
        Meta class for UserRatingComment
        '''
        model = UserRatingComment
        fields = '__all__'
