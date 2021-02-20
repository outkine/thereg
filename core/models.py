from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    social_link = models.CharField(max_length=100, blank=True)
    pronouns = models.CharField(max_length=20)
