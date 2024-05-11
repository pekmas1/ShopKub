from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from userprofile.models import UserProfile
from django.contrib.auth.models import User

@login_required
def detail(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    user = get_object_or_404(User, username=request.user.username)
    return render(request, 'userprofile/detail.html', {"profile":profile, "user":user})