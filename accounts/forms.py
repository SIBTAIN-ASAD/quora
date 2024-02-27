# accounts/forms.py
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import CustomUser
class CustomUserCreationForm(UserCreationForm):
    '''
    This class handles the custom user creation form.
    '''
    class Meta(UserCreationForm):
        '''
        This class handles the meta data of the custom user creation form.
        '''
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ( "age", "email", "profilePicture", "first_name", "gender")

        def clean_age(self):
            '''
            This method handles the clean age.
            '''
            age = self.cleaned_data.get("age")
            if age < 0:
                raise forms.ValidationError("Age should be a positive number")
            return age

class CustomUserChangeForm(UserChangeForm):
    '''
    This class handles the custom user change form.
    '''
    class Meta:
        '''
        This class handles the meta data of the custom user change form.
        '''
        model = CustomUser
        fields = UserChangeForm.Meta.fields

    def clean_age(self):
        '''
        This method handles the clean age.
        '''
        age = self.cleaned_data.get("age")
        if age < 0:
            raise forms.ValidationError("Age should be a positive number")
        return age        
