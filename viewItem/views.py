from django.shortcuts import render
from database.models import Users, Items

# Create your views here.
def index(request, id):
    item = Items.objects.get(ItemId=id)

    return render(request, "viewItem/item.html", {"item":item})