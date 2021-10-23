from django.db import models


# Create your models here.

class Items(models.Model):
    # users = models.ForeignKey(Users, on_delete=models.CASCADE)
    itemID = models.AutoField(primary_key=True)
    userId = models.IntegerField()
    name = models.CharField(max_length=60, default="item")
    url = models.CharField(max_length=250)
    imageUrl = models.CharField(max_length=250, default="image")
    price = models.DecimalField(decimal_places=2, max_digits=12, default=0.00)
    description = models.CharField(max_length=250, default="description")
    quantity = models.IntegerField(default=0)
    priority = models.CharField(max_length=25, default="0")

    def __str__(self):
        return self.url
