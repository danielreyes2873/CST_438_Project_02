from django.shortcuts import render
from django.contrib.auth.models import User


# Create your views here.
def index(request):
    return render(request,"admins/admin.html")

def index2(request):
    user = User.objects.all()
    return render(request,"admins/viewUsers.html",{"users":user})

def index3(request):
    return render(request,"admins/createUserInfo.html")

def index4(request):
    return render(request,"admins/updaterUserInfo.html")

