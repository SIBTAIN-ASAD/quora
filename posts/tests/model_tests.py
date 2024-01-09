'''
This file handles the model tests.
'''

from django.test import TestCase
from posts.models import Topic
from .factories import TopicFactory
from accounts.factories import CustomUserFactory


class TopicModelTestCase(TestCase):
    '''
    This class handles the topic model test case.
    '''
    def test_topic_creation(self):
        '''
        This method handles the topic creation.
        '''
        topic = TopicFactory()
        self.assertIsInstance(topic, Topic)
        self.assertIsNotNone(topic.id)
        self.assertIsNotNone(topic.name)
        self.assertIsNotNone(topic.description)
        self.assertIsNotNone(topic.author)
        topic = TopicFactory()
        self.assertIsInstance(topic, Topic)
        self.assertTrue(Topic.objects.filter(id=topic.id).exists())

    def test_topic_followed_by(self):
        '''
        This method handles the topic followed by.
        '''
        user = CustomUserFactory()
        topic = TopicFactory()
        topic.followed_by.add(user)
        self.assertTrue(topic.followed_by.filter(id=user.id).exists())

