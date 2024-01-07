'''
Views for the accounts app
'''
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.views import LoginView
from .forms import CustomUserCreationForm
from django.shortcuts import redirect
# authenticated mixins in django
from django.contrib.auth.mixins import LoginRequiredMixin
from .common import ProfileQueries

class SignUpView(CreateView):
    '''
    View for signing up a new user
    '''
    form_class = CustomUserCreationForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("login")

class ProfileView(LoginRequiredMixin, TemplateView):
    '''
    View for displaying the profile of the user
    '''
    template_name = "profile.html"
    redirect_field_name = "login"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context["user"] = user
        context["questions"], context['qlikes'], context['qdislikes'] = ProfileQueries.all_questions(user.id)
        context["answers"] = ProfileQueries.all_answers(user.id)
        context["topics"] = ProfileQueries.all_topics(user.id)
        context["votes"] = ProfileQueries.all_votes(user.id)
        return context


class CustomLoginView(LoginView):
    '''
    View for logging in the user
    '''
    template_name = "registration/login.html"
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("profile")

    # if user is authenticated, then redirect to profile page
    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("profile")
        return super().get(request, *args, **kwargs)

class UserProfileUpdateView(LoginRequiredMixin, TemplateView):
    '''
    View for updating the user profile
    '''
    template_name = "registration/update_profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context["user"] = user
        return context

    def post(self, request, *args, **kwargs):
        user = self.request.user
        user.first_name = request.POST.get('first_name')
        user.email = request.POST.get('email')
        user.age = request.POST.get('age')
        user.profilePicture = request.FILES.get('profilePicture')
        user.gender = request.POST.get("gender")
        user.save()
        return redirect("profile")
