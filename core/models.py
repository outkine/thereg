from django.db import models
from django.contrib.auth.models import AbstractUser
from django.forms import ModelForm


class User(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    social_link = models.CharField(max_length=100, blank=True)
    pronouns = models.CharField(max_length=20)
    photo = models.FileField(upload_to='static/', blank=True)


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name', 'bio', 'social_link', 'photo', 'pronouns']


class Match(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    target = models.ForeignKey(User, on_delete=models.CASCADE, related_name="target_set")

