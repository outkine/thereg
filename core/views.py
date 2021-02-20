from django.shortcuts import render, get_object_or_404

from .models import User

def index(request):
    users = User.objects.all()
    return render(request, 'index.html', {'users': users})

def user(request, username):
    user = get_object_or_404(User, username=username)
    return render(request, 'user.html', {'user': user})


