'''
This class handles the like question view.
'''

from django.shortcuts import get_object_or_404, redirect
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from posts.models import Question, Vote
from posts.common.queries import QuestionPageQueries

class QuestoinView(LoginRequiredMixin, TemplateView):
    '''
    This class handles the like question view.
    '''
    template_name = "posts/templates/question.html"

    def get_context_data(self, **kwargs):
        '''
        This method handles the get request.
        '''
        context = super().get_context_data(**kwargs)
        question = get_object_or_404(Question, pk=self.kwargs['question_id'])
        context["question"] = QuestionPageQueries.get_complete_question(question)
        return context
