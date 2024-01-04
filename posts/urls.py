# posts/urls.py
from django.urls import path
from .views import HomePageView, LikeQuestionView, DislikeQuestionView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('like/<int:question_id>/', LikeQuestionView.as_view(), name='like_question'),
    path('dislike/<int:question_id>/', DislikeQuestionView.as_view(), name='dislike_question'),
]
