from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('users/<str:username>', views.user, name='user'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('match/<str:username>', views.match, name='match'),
    path('signup/', views.signup, name='signup')
]
