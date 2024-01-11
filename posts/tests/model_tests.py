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
        self.assertTrue(Topic.objects.filter(id=topic.id).exists())
        

    def test_topic_followed_by(self):
        '''
        This method handles the topic followed by.
        '''
        user = CustomUserFactory()
        topic = TopicFactory()
        topic.followed_by.add(user)
        self.assertTrue(topic.followed_by.filter(id=user.id).exists())


    def test_topic_unfollowed_by(self):
        '''
        This method handles the topic unfollowed by.
        '''
        user = CustomUserFactory()
        topic = TopicFactory()
        topic.followed_by.add(user)
        topic.followed_by.remove(user)
        self.assertFalse(topic.followed_by.filter(id=user.id).exists())

    def test_topic_followed_by_count(self):
        '''
        This method handles the topic followed by count.
        '''
        user = CustomUserFactory()
        topic = TopicFactory()
        topic.followed_by.add(user)
        self.assertEqual(topic.followed_by.count(), 1)


    def test_topic_unfollowed_by_count(self):
        '''
        This method handles the topic unfollowed by count.
        '''
        user = CustomUserFactory()
        topic = TopicFactory()
        topic.followed_by.add(user)
        topic.followed_by.remove(user)
        self.assertEqual(topic.followed_by.count(), 0)
        
    def test_topic_str_representation(self):
        '''
        This method tests the __str__ method of the Topic model.
        '''
        topic = TopicFactory(name='Test Topic')
        self.assertEqual(topic.name, 'Test Topic')


    def test_topic_author_is_custom_user(self):
        '''
        This method tests if the author of the Topic is an instance of CustomUser.
        '''
        topic = TopicFactory()
        self.assertIsInstance(topic.author, CustomUserFactory._meta.model)

    def test_topic_author_username(self):
        '''
        This method tests if the author's username is set correctly.
        '''
        user = CustomUserFactory(username='test_user')
        topic = TopicFactory(author=user)
        self.assertEqual(topic.author.username, 'test_user')
