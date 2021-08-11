from django.db import models

# Create your models here.


class Information(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    address = models.CharField(max_length=50)
    contact = models.IntegerField()
