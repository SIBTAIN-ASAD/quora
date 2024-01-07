'''
This class handles the like question view.
'''

from django.shortcuts import get_object_or_404, redirect
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from posts.models import Question, Topic
from posts.common.queries import QuestionPageQueries

class QuestoinView(LoginRequiredMixin, TemplateView):
    '''
    This class handles the specific question view.
    '''
    template_name = "posts/templates/question.html"

    def get_context_data(self, **kwargs):
        '''
        This method handles the get request.
        '''
        context = super().get_context_data(**kwargs)
        question = get_object_or_404(Question, pk=self.kwargs['question_id'])
        context["question"] = QuestionPageQueries.get_complete_question(question)
        context["topics"] = Topic.objects.all()
        return context

class AddQuestionView(LoginRequiredMixin, TemplateView):
    '''
    This class handles the add question view.
    '''
    template_name = "posts/templates/add_question.html"

    def get_context_data(self, **kwargs):
        '''
        This method handles the get request.
        '''
        context = super().get_context_data(**kwargs)
        context['topics'] = Topic.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        '''
        This method handles the post request.
        '''
        title = request.POST.get("title")
        description = request.POST.get("description")
        author = request.user

        # Create a new question
        question = Question.objects.create(
            title=title,
            description=description,
            author=author
        )

        # Handle topics
        topics = request.POST.getlist("topics")
        for topic_id in topics:
            print(topic_id)
            topic = Topic.objects.get(pk=topic_id)
            question.topics.add(topic)
            
        return redirect("question_page", question_id=question.id)

class AddQuestionFormView(LoginRequiredMixin, TemplateView):
    '''
    This class handles the add question form view.
    '''
    template_name = "posts/templates/add_question.html"

    def get_context_data(self, **kwargs):
        '''
        This method handles the get request.
        '''
        context = super().get_context_data(**kwargs)
        context["topics"] = Topic.objects.all()
        return context
