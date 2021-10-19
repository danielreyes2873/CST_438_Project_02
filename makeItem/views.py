from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import CreateItemForm

def index(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CreateItemForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('home/home.html')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = CreateItemForm()

    return render(request, 'makeItem/index.html', {'form': form})