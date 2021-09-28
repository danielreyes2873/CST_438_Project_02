from django.db import models


# Create your models here.
class Users(models.Model):
    userID = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username


class Items(models.Model):
    # users = models.ForeignKey(Users, on_delete=models.CASCADE)
    itemID = models.AutoField(primary_key=True)
    userId = models.IntegerField()
    url = models.CharField(max_length=250)

    def __str__(self):
        return self.url
