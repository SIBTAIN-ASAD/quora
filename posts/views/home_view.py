'''
This file contains all the views that are used in the home page.
'''

from django.views.generic import TemplateView
from django.views import View
from posts.models import Question, Vote, Topic, Answer
from posts.common.queries import HomePageQueries
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect


class HomePageView(LoginRequiredMixin, TemplateView):
    '''
    This class handles the home page view.
    '''
    template_name = "posts/templates/home.html"

    def get_context_data(self, **kwargs):
        '''
        This method handles the get request.
        '''
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context["user"] = user
        context["topics"] = user.followed_topics.all()

        # Get followed questions along with likes and dislikes
        context["followed_questions"] = HomePageQueries.get_user_questions(user)

        return context
    
class SearchView(LoginRequiredMixin, TemplateView):
    '''
    This class handles the search view.
    '''
    template_name = "posts/templates/home.html"

    def post(self, request, *args, **kwargs):
        '''
        This method handles the post request.
        '''
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context["user"] = user
        context["topics"] = user.followed_topics.all()

        # Get searched questions along with likes and dislikes
        context["searched_questions"], context["searched_topics"] = HomePageQueries.get_searched_questions(request.POST.get('search'))
        context["search_str"] = request.POST.get('search')

        return self.render_to_response(context)
    
class LikeQuestionView(LoginRequiredMixin, View):
    '''
    This class handles the like question view.
    '''
    def post(self, request, question_id, *args, **kwargs):
        '''
        This method handles the post request.
        '''
        question = get_object_or_404(Question, pk=question_id)
        user = self.request.user

        # Check if the user has already liked the question
        existing_vote = Vote.objects.filter(question=question, author=user, vote_type='L').first()

        if not existing_vote:
            # If the user hasn't liked the question, create a new like
            Vote.objects.create(question=question, author=user, vote_type='L')

        # Redirect back to the question or wherever you want
        return redirect('/', question_id=question_id)

class DislikeQuestionView(LoginRequiredMixin, View):
    '''
    This class handles the dislike question view.
    '''
    def post(self, request, question_id, *args, **kwargs):
        '''
        This method handles the post request.
        '''
        question = get_object_or_404(Question, pk=question_id)
        user = self.request.user

        # Check if the user has already disliked the question
        existing_vote = Vote.objects.filter(question=question, author=user, vote_type='D').first()

        if not existing_vote:
            # If the user hasn't disliked the question, create a new dislike
            Vote.objects.create(question=question, author=user, vote_type='D')

        # Redirect back to the question or wherever you want
        return redirect('/', question_id=question_id)
    
class AnswerQuestionView(LoginRequiredMixin, View):
    '''
    This class handles the answer question view.
    '''
    def post(self, request, question_id, *args, **kwargs):
        '''
        This method handles the post request.
        '''
        question = get_object_or_404(Question, pk=question_id)
        user = self.request.user

        # Create a new answer
        Answer.objects.create(question=question, author=user, description=request.POST.get('answer'))

        # Redirect back to the question or wherever you want
        return redirect('/', question_id=question_id)
