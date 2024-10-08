'''
This file contains the forms for the topics.
'''

from django import forms
from posts.models import Topic

class AddTopicForm(forms.ModelForm):
    '''
    Form for adding a new topic
    '''
    class Meta:
        model = Topic
        fields = ['name', 'description', 'topic_picture']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }
