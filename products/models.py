from django.db import models
from datetime import datetime
from magnum_online.functions import hashing


class Product(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    available = models.BooleanField(default=True)


class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart = models.ManyToManyFiled(Product)
    created = models.DateTimeField(default=datetime.now())
    qr_hash = models.CharField(max_field=10, default=functions., unique=True)