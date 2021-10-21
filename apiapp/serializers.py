# serializers.py
from rest_framework import serializers

from .models import Item


class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = ('name', 'url', 'imageUrl', 'price')
