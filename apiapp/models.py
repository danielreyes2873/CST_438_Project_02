from django.db import models


# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=60)
    url = models.CharField(max_length=250)
    imageUrl = models.CharField(max_length=250)
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=250, default="description")

    def __str__(self):
        return self.name
