from django.shortcuts import render

# Create your views here.
# views.py
from rest_framework import viewsets

from .serializers import ItemSerializer
from .models import Item


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all().order_by('name')
    serializer_class = ItemSerializer
