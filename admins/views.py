from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"admins/admin.html")

def index2(request):
    return render(request,"admins/viewUsers.html")

def index3(request):
    return render(request,"admins/createUserInfo.html")

def index4(request):
    return render(request,"admins/updaterUserInfo.html")

