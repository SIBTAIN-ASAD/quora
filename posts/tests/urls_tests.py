'''
This module tests the URLs of the posts app.
'''
from django.test import TestCase
from django.urls import reverse
from posts.tests.factories import TopicFactory
from accounts.factories import CustomUserFactory

class TopicURLsTestCase(TestCase):
    def setUp(self):
        self.user = CustomUserFactory()
        self.client.force_login(self.user)

    def test_add_topic_view(self):
        response = self.client.get(reverse('add_topic'))
        self.assertEqual(response.status_code, 200)

    def test_topic_page_view(self):
        topic = TopicFactory()
        response = self.client.get(reverse('topic_page', kwargs={'topic_id': topic.id}))
        self.assertEqual(response.status_code, 200)

    def test_topic_follow_view(self):
        topic = TopicFactory()
        response = self.client.get(reverse('topic_follow', kwargs={'topic_id': topic.id}))
        self.assertEqual(response.status_code, 200)

    def test_topic_unfollow_view(self):
        topic = TopicFactory()
        response = self.client.get(reverse('topic_unfollow', kwargs={'topic_id': topic.id}))
        self.assertEqual(response.status_code, 200)
