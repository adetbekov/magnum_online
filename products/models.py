from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from magnum_online.functions import randhash6


class Product(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    available = models.BooleanField(default=True)


class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart = models.ManyToManyField(Product)
    created = models.DateTimeField(default=datetime.now)
    qr_hash = models.CharField(max_length=6, default=randhash6, unique=True)