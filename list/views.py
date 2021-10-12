from django.shortcuts import render
from database.models import Items
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    users = User.objects.all()

    items = Items.objects.all()
    return render(request,"list/list.html", {"items":items})

def viewItem(request, id):
    item = Items.objects.get(itemID=id)

    return render(request,"viewItem/item.html", {"item":item})
