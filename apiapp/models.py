from django.db import models


# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=60, default="Item")
    url = models.CharField(max_length=250, default="url")
    imageUrl = models.CharField(max_length=250, default="image")
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=250, default="description")

    def __str__(self):
        return self.name
