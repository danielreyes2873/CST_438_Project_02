from django.shortcuts import render
from django.http import HttpResponse
from .models import Users, Items


# Create your views here.
def index(response, userID):
    ls = Users.objects.get(userID=userID)
    return HttpResponse("<h1>%s</h1>" % ls.username)
