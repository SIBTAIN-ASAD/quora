# posts/urls.py
from django.urls import path
from .views import (HomePageView, 
                    LikeQuestionView,
                    DislikeQuestionView,
                    AnswerQuestionView,
                    SearchView,
                    LikeAnswerView,
                    DislikeAnswerView,
                    AddTopicView,
                    TopicPageView,
                    QuestoinView,
                    AboutView,
                    )

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('like/<int:question_id>/', LikeQuestionView.as_view(), name='like_question'),
    path('dislike/<int:question_id>/', DislikeQuestionView.as_view(), name='dislike_question'),
    path('answer/<int:question_id>/', AnswerQuestionView.as_view(), name='answer_question'),
    path('like_answer/<int:answer_id>/', LikeAnswerView.as_view(), name='like_answer'),
    path('dislike_answer/<int:answer_id>/', DislikeAnswerView.as_view(), name='dislike_answer'),
    path('search/', SearchView.as_view(), name='search'),
    path('add_topic/', AddTopicView.as_view(), name='add_topic'),
    path('topic/<int:topic_id>/', TopicPageView.as_view(), name='topic_page'),
    path('topic/<int:topic_id>/<int:page>/', TopicPageView.as_view(), name='topic_page_paginated'),
    path('question/<int:question_id>/', QuestoinView.as_view(), name='question_page'),
    path('about/<str:target_username>', AboutView.as_view(), name='about'),
]
