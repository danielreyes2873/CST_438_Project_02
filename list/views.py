from django.shortcuts import render
from database.models import Users, Items

# Create your views here.
def index(request):
    users = Users.objects.all()

    items = Items.objects.all()
    return render(request,"list/list.html", {"items":items})

def viewItem(request, id):
    item = Items.objects.get(itemID=id)

    return render(request,"viewItem/item.html", {"item":item})