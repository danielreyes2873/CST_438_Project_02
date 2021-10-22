from django.shortcuts import render,redirect
from database.models import Items
from apiapp.models import Item #all items
from django.contrib.auth.models import User

def index(request):
    return render(request, "editItem/item.html")

def index2(request,name):
    item = Item.objects.get(name=name)

    if request.method == "POST":
        if request.POST.get('ID'):
            id = Item.objects.get(id=request.POST.get('ID'))
            if request.POST.get('url'):
                id.url = request.POST.get('url')
            if request.POST.get('imgUrl'):
                id.imageUrl = request.POST.get('imgUrl')
            if request.POST.get('price'):
                id.price = request.POST.get('price')
            if request.POST.get('description'):
                id.description = request.POST.get('description')
            id.save()
            return redirect("/list")
    return render(request, "editItem/item.html",{"item":item})









