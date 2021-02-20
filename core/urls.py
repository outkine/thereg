from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('users/<str:username>', views.user, name='user'),
]
