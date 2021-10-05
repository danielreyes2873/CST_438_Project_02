from django.shortcuts import render
from database.models import Users


def index(request):
    if request.method == "POST":
        if request.POST.get('username') and request.POST.get('password'):
            user = Users()
            user.username = request.POST.get('username')
            user.password = request.POST.get('password')
            user.save()
            return render(request, 'register/index.html')
    else:
        return render(request, "register/index.html")