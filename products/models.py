from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from magnum_online.functions import randhash6, strnormalize


STATUS_CHOICE = {
	('I', 'Incomplete'),
	('S', 'Completed'),
	('R', 'Rejected'),
	('C', 'Canceled'),
}


class Product(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    created = models.DateTimeField(default=datetime.now)
    available = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self):
        return "<product-{}>".format(strnormalize(self.name))


class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart = models.ManyToManyField(Product)
    status = models.CharField(max_length=3, choices=STATUS_CHOICE, default="I")
    created = models.DateTimeField(default=datetime.now)
    qr_hash = models.CharField(max_length=6, default=randhash6, unique=True)

    class Meta:
        verbose_name = "Транзакция"
        verbose_name_plural = "Транзакции"

    def __str__(self):
        return "<transaction-{}>".format(self.qr_hash)