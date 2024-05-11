from django.shortcuts import render, redirect
from item.models import Category, Item
from .forms import SignupForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from userprofile.forms import UserProfileForm

def index(request):
    items = Item.objects.filter(is_sold=False)[:6]
    categories = Category.objects.all()

    return render(request, "core/index.html", {
        "categories": categories,
        "items": items
    })

def contact(request):
    return render(request, "core/contact.html")

def signup(request):
    if request.method == "POST":
        core_form = SignupForm(request.POST)
        profile_form = UserProfileForm(request.POST, request.FILES)
        if core_form.is_valid() and profile_form.is_valid():
            user = core_form.save()
            profile_form.instance.user = user
            profile_form.save()
        return redirect("/login/")
    else:
        core_form = SignupForm()
        profile_form = UserProfileForm()
    return render(request, "core/signup.html", {"core_form":core_form,"profile_form":profile_form})

@login_required
def sign_out(request):
    logout(request)
    return redirect('/')