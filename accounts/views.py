from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from .forms import CustomUserCreationForm
from django.shortcuts import redirect

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("login")
    

class ProfileView(TemplateView):
    template_name = "profile.html"

class CustomLoginView(LoginView):
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
    