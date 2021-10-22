from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def index(request):
    return render(request, "admins/admin.html")


def index2(request):
    user = User.objects.all()
    context = {}
    if request.method == "POST":
        if request.POST.get('userID'):
            u = User.objects.get(id=request.POST.get('userID'))
            u.delete()
            context['msg'] = 'The user is deleted.'
            return render(request, "admins/viewUsers.html", {"users": user})

    return render(request, "admins/viewUsers.html", {"users": user})


def index3(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/admins/viewUsers")
    else:
        form = UserCreationForm()
    return render(request, "admins/createUserInfo.html", {"form": form})


def index4(request):
    return render(request, "admins/updaterUserInfo.html")
