'''
tests/test_factories.py
'''

import factory
from accounts.factories import CustomUserFactory
from posts.models import Topic, Question, Answer, Vote

class TopicFactory(factory.django.DjangoModelFactory):
    '''
    This class handles the topic factory.
    '''
    class Meta:
        '''
        This class handles the meta data of the topic factory.
        '''
        model = Topic

    name = factory.Faker('word')
    description = factory.Faker('paragraph')
    author = factory.SubFactory(CustomUserFactory)

class QuestionFactory(factory.django.DjangoModelFactory):
    '''
    This class handles the question factory.
    '''
    class Meta:
        '''
        This class handles the meta data of the question factory.
        '''
        model = Question

    title = factory.Faker('sentence')
    description = factory.Faker('paragraph')
    author = factory.SubFactory(CustomUserFactory)
    topic = factory.SubFactory(TopicFactory)

class AnswerFactory(factory.django.DjangoModelFactory):
    '''
    This class handles the answer factory.
    '''
    class Meta:
        '''
        This class handles the meta data of the answer factory.
        '''
        model = Answer

    description = factory.Faker('paragraph')
    author = factory.SubFactory(CustomUserFactory)
    question = factory.SubFactory(QuestionFactory)

class VoteFactory(factory.django.DjangoModelFactory):
    '''
    This class handles the vote factory.
    '''
    class Meta:
        '''
        This class handles the meta data of the vote factory.
        '''
        model = Vote

    vote_type = factory.Faker('word')
    author = factory.SubFactory(CustomUserFactory)
    answer = factory.SubFactory(AnswerFactory)
    question = factory.SubFactory(QuestionFactory)

    