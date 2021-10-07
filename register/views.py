from django.shortcuts import render, redirect
from database.models import Users
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm


def register(response):
    if response.method == "POST":
        form = UserCreationForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect("/")
    else:
        form = UserCreationForm()

    return render(response, "register/register.html", {"form": form})


def index(request):
    if request.method == "POST":
        if request.POST.get('username') and request.POST.get('password') and request.POST.get('repeatPassword'):
            if request.POST.get('password') == request.POST.get('repeatPassword'):
                user = Users()
                user.username = request.POST.get('username')
                user.password = request.POST.get('password')
                user.save()
                return render(request, 'home/home.html')
            else:
                return render(request, 'register/index.html', {"error": "passwords must match"})

    else:
        return render(request, "register/index.html")
