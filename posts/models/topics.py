from django.db import models
from .questions import Question

# Create your models here.

class Topic(models.Model):
    '''
    Topic model
    '''
    name = models.CharField(max_length=200)
    description = models.TextField()
    questions = models.ManyToManyField(Question)
    author = models.ForeignKey("accounts.CustomUser", on_delete=models.CASCADE)
    followed_by = models.ManyToManyField("accounts.CustomUser", related_name="followed_topics")
