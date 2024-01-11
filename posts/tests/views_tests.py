'''
This module handles the views tests.
'''
from django.test import TestCase
from django.urls import reverse
from posts.tests.factories import *
from accounts.factories import CustomUserFactory
from posts.models import Topic


class TopicViewsTestCase(TestCase):
    '''
    This class handles the topic views test case.
    '''
    def setUp(self):
        self.user = CustomUserFactory()

    def test_add_topic_view_authenticated_user(self):
        '''
        This method handles the add topic view with an authenticated user.
        '''
        self.client.force_login(self.user)
        response = self.client.post(reverse('add_topic'), {'name': 'Test Topic', 'description': 'Test Description'})
        self.assertEqual(response.status_code, 302)  # Check for a successful redirect
        self.assertTrue(Topic.objects.filter(name='Test Topic').exists())

    def test_topic_page_view_authenticated_user(self):
        '''
        This method handles the topic page view with an authenticated user.
        '''
        self.client.force_login(self.user)
        topic = TopicFactory(author=self.user)
        response = self.client.get(reverse('topic_page', args=[topic.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, topic.name)

    def test_topic_follow_view_authenticated_user(self):
        '''
        This method handles the topic follow view with an authenticated user.
        '''
        self.client.force_login(self.user)
        topic = TopicFactory()
        response = self.client.get(reverse('topic_follow', args=[topic.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(topic.followed_by.filter(id=self.user.id).exists())

    def test_topic_unfollow_view_authenticated_user(self):
        '''
        This method handles the topic unfollow view with an authenticated user.
        '''
        self.client.force_login(self.user)
        topic = TopicFactory()
        topic.followed_by.add(self.user)
        response = self.client.get(reverse('topic_unfollow', args=[topic.id]))
        self.assertEqual(response.status_code, 200)
        self.assertFalse(topic.followed_by.filter(id=self.user.id).exists())
