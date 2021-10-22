from django.shortcuts import render
from django.contrib.auth.models import User
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
    return render(request, "admins/createUserInfo.html")


def index4(request):
    return render(request, "admins/updaterUserInfo.html")
