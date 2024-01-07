'''
Views for the Topic model.
'''

from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from posts.models import Topic, Question
from posts.common.queries import TopicPageQueries

class AddTopicView(CreateView):
    '''
    View for adding a new topic
    '''
    model = Topic
    template_name = 'topic.html'
    fields = ['title', 'description']
    success_url = reverse_lazy('home')

class TopicPageView(ListView):
    '''
    View for displaying the topic page
    '''
    model = Question
    template_name = 'posts/templates/topic.html'
    context_object_name = 'questions'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        topic = get_object_or_404(Topic, pk=self.kwargs['topic_id'])
        context['topic'] = topic
        context['topics'] = TopicPageQueries.get_topics()
        return context

    def get_queryset(self):
        topic = get_object_or_404(Topic, pk=self.kwargs['topic_id'])
        if self.request.GET.get('sort') == 'user':
            questions = TopicPageQueries.get_topic_questions_paginated_by_user(topic, self.request.user, self.kwargs['page'])
        elif self.request.GET.get('sort') == 'date':
            questions = TopicPageQueries.get_topic_questions_paginated_by_user_and_date(topic, self.request.user, self.kwargs['page'])
        elif self.request.GET.get('sort') == 'likes':
            questions = TopicPageQueries.get_topic_questions_paginated_by_user_and_likes(topic, self.request.user, self.kwargs['page'])
        else:
            questions = TopicPageQueries.get_topic_questions_paginated(topic, self.kwargs['page'])
        return questions

    def get_paginate_by(self, queryset):
        return self.request.GET.get('paginate_by', self.paginate_by)
