
from django.shortcuts import render,redirect
from database.models import Items
from apiapp.models import Item #all items
from django.contrib.auth.models import User

def index(request):
    return render(request, "editItem/item.html")

def index2(request,id):
    item = Item.objects.get(id=id)

    if request.method == "POST":
        if request.POST.get('ID'):
            i = Item.objects.get(id=request.POST.get('ID'))
            if request.POST.get('url'):
                i.url = request.POST.get('url')
            if request.POST.get('imgUrl'):
                i.imageUrl = request.POST.get('imgUrl')
            if request.POST.get('price'):
                i.price = request.POST.get('price')
            if request.POST.get('description'):
                i.description = request.POST.get('description')
            i.save()
            return redirect("/list")
    return render(request, "editItem/item.html",{"item":item})
