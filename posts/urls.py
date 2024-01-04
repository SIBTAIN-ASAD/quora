# posts/urls.py
from django.urls import path
from .views import HomePageView, LikeQuestionView, DislikeQuestionView, AnswerQuestionView, SearchView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('like/<int:question_id>/', LikeQuestionView.as_view(), name='like_question'),
    path('dislike/<int:question_id>/', DislikeQuestionView.as_view(), name='dislike_question'),
    path('answer/<int:question_id>/', AnswerQuestionView.as_view(), name='answer_question'),
    path('search/', SearchView.as_view(), name='search'),
]
