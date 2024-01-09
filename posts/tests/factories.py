'''
tests/test_factories.py
'''

import factory
from accounts.factories import CustomUserFactory
from posts.models import Topic

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
