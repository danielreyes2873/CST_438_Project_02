from django.shortcuts import render
from database.models import Users, Items

# Create your views here.
def index(request):
    firstUser = Users.objects.get(userID=1)
    username = firstUser.username
    return render(request,"list/list.html", {"username":username})