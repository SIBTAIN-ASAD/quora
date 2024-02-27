from django.db import models
# Create your models here.

from cloudinary.models import CloudinaryField
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    email = models.EmailField(unique=True)
    profilePicture = CloudinaryField('image')
    gender = models.CharField(max_length=10, null=True, blank=True)
