from django.shortcuts import render, redirect
from database.models import Items #user wishlist items
from apiapp.models import Item #all items

def index(request, id):
    item = Items.objects.get(id=id)
    return render(request, "editItem/item.html", {"item":item})

def removeItem(request, id):
    item = Items.objects.get(id=id)
    item.delete()
    return redirect("/")

