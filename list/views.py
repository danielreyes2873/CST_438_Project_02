from django.shortcuts import render, redirect
from database.models import Items  # user wishlist items
from apiapp.models import Item  # all items
from django.contrib.auth.models import User


# Create your views here.
def index(request):
    items = Item.objects.all()
    if request.method == "POST":
        u = User.objects.get(id=request.POST.get('userID'))
        return redirect("wishList/", u)

    return render(request, "list/list.html", {"items": items})


def viewItem(request, id):
    item = Item.objects.get(id=id)
    if request.method == "POST":
        if request.POST.get('quantity') and request.POST.get('priority'):
            u = User.objects.get(id=request.POST.get('userID'))
            item = Item.objects.get(id=request.POST.get('itemId'))
            itemname = item.name
            itemUrl = item.url
            itemImage = item.imageUrl
            itemdesc = item.description
            itemPrice = item.price
            itemQuantity = request.POST.get('quantity')
            itemPriority = request.POST.get('priority')

            newItem = Items(userId=u.id, name=itemname, url=itemUrl, imageUrl=itemImage, description=itemdesc,
                            price=itemPrice, quantity=itemQuantity, priority=itemPriority)
            newItem.save()
            return redirect("/list")

    return render(request, "list/viewItem.html", {"item": item})


def wishList(request, id):
    items = Items.objects.select_related().filter(userId=id)
    if request.method == "POST":
        if request.POST.get('itemID'):
            item = Items.objects.get(itemID=request.POST.get('itemID'))
            item.delete()
        return render(request, "list/wishList.html", {"items": items})
    # items = Items.objects.select_related().filter(userId=id)
    return render(request, "list/wishList.html", {"items": items})

def wishListNone(request):
    return render(request, "list/wishListNone.html")
