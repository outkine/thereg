from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import User, Match

def index(request):
    users = User.objects.all()
    return render(request, 'index.html', {'users': users})

def user(request, username):
    user = get_object_or_404(User, username=username)
    return render(request, 'user.html', {'user': user})


    return render(request, 'user.html', {'user': user})

def match(request, username):
    if request.user.is_authenticated:
        target = get_object_or_404(User, username=username)
        Match.objects.create(author=request.user, target=target)
    return HttpResponseRedirect(reverse('user', args=[username]))
