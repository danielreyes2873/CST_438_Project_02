from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from database.models import Items


# Create your views here.
def index(request):
    return render(request, "admins/admin.html")


def index2(request):
    user = User.objects.all()
    if request.method == "POST":
        if request.POST.get('userID'):
            u = User.objects.get(id=request.POST.get('userID'))
            u.delete()
            item = Items.objects.all()
            for i in item:
                if i.userId == u.id:
                    i.delete()
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


# def index4(request):
#     return render(request, "admins/updaterUserInfo.html")

def index5(request):
    user = User.objects.all()

    if request.method == "POST":
        if request.POST.get('userID'):
            u = User.objects.get(id=request.POST.get('userID'))
            return render(request, "admins/updatingUsers.html", {"u":u})
        if request.POST.get('ID'):
            u = User.objects.get(id=request.POST.get('ID'))
            if request.POST.get('username'):
                u.username = request.POST.get('username')
            if request.POST.get('password'):
                u.set_password(request.POST.get('password'))
            u.save()
            return render(request, "admins/updaterUserInfo.html", {"users": user})

    return render(request, "admins/updaterUserInfo.html", {"users": user})

def index6(request):
    return render(request, "updatingUsers.html")
