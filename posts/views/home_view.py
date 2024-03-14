'''
This file contains all the views that are used in the home page.
'''

from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from posts.common.queries import HomePageQueries

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

        # if search is empty string, return all followed questions
        if len(request.POST.get('search')) == 0:
            context["followed_questions"] = HomePageQueries.get_user_questions(user)
            return self.render_to_response(context)

        # Get searched questions along with likes and dislikes
        context["searched_questions"], context["searched_topics"] = HomePageQueries.get_searched_questions(request.POST.get('search'))
        context["search_str"] = request.POST.get('search')

        return self.render_to_response(context)
