'''
This file contains all the queries that are used in the accounts app.
'''

from accounts.models import CustomUser
from posts.models import Question, Answer, Topic, Vote

class ProfileQueries:
    '''
    This class contains all the queries related to the Profile model.
    '''
    @staticmethod
    def get_user_by_id(user_id):
        '''
        This method returns the user with the given id.
        '''
        return CustomUser.objects.get(id=user_id)

    @staticmethod
    def all_questions(user_id):
        '''
        This method returns all the questions asked by the user with the given id.
        '''

        data_set = Question.objects.filter(author=user_id)
        return data_set

    @staticmethod
    def all_answers(user_id):
        '''
        This method returns all the answers given by the user with the given id.
        '''
        return Answer.objects.filter(author=user_id)

    @staticmethod
    def all_topics(user_id):
        '''
        This method returns all the topics followed by the user with the given id.
        '''
        return Topic.objects.filter(followed_by=user_id)

    @staticmethod
    def all_votes(user_id):
        '''
        This method returns all the votes given by the user with the given id.
        '''
        return Vote.objects.filter(author=user_id)
