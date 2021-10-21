from django.http import HttpResponseRedirect
from django.shortcuts import render

from apiapp.models import Item
from .forms import CreateItemForm

def index(request):
    if request.method == 'POST':
        form = CreateItemForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            price = form.cleaned_data['price']
            url = form.cleaned_data['url']
            urlImage = form.cleaned_data['urlimage']

            item = Item(name=name, price=price, url=url, imageUrl=urlImage)
            item.save()
            return HttpResponseRedirect('/')
    else:
        form = CreateItemForm()

    return render(request, 'makeItem/index.html', {'form': form})