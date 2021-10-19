from django.shortcuts import render
from database.models import Items #user wishlist items
from apiapp.models import Item #all items
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    items = Item.objects.all()
    return render(request,"list/list.html", {"items":items})

def viewItem(request, id):
    item = Item.objects.get(id)
    return render(request, "list/viewItem.html", {"item": item})