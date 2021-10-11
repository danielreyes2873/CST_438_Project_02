from django.shortcuts import render
from database.models import Users, Items

# Create your views here.
def index(request):
    return render(request,"list/list.html")