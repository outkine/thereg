from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import User, Match, UserForm


def index(request):
    users = User.objects.all()
    return render(request, 'index.html', {'users': users})

def user(request, username):
    user = get_object_or_404(User, username=username)

    match = None
    reverse_match = None
    if request.user.is_authenticated:
        match = Match.objects.filter(author=request.user, target=user).first()
        reverse_match = Match.objects.filter(author=user, target=request.user).first()

    return render(request, 'user.html', {'user': user, 'match': match, 'reverse_match': reverse_match})

def match(request, username):
    if request.user.is_authenticated:
        target = get_object_or_404(User, username=username)
        Match.objects.create(author=request.user, target=target)
    return HttpResponseRedirect(reverse('user', args=[username]))

def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponseRedirect('/')

    else:
        form = UserForm()

    return render(request, 'signup.html', {'form': form})
