import os
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from magnum_online.functions import randhash6, strnormalize, hashing


STATUS_CHOICE = {
	('I', 'Incomplete'),
	('S', 'Completed'),
	('R', 'Rejected'),
	('C', 'Canceled'),
}

def upload_full_image(instance, filename):
    return "images/%s%s%s" % (instance.id, hashing(), os.path.splitext(filename)[1])


class Category(models.Model):
    name = models.CharField(max_length=30, blank=False)
    created = models.DateTimeField(default=datetime.now)

    class Meta:
      verbose_name = "Категория"
      verbose_name_plural = "Категории"

    def __str__(self):
      return str(self.name)


class SubCategory(models.Model):
    name = models.CharField(max_length=30, blank=False)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    created = models.DateTimeField(default=datetime.now)

    class Meta:
      verbose_name = "Субкатегория"
      verbose_name_plural = "Субкатегории"

    def __str__(self):
      return str(self.name)


class Manufacturer(models.Model):
    name = models.CharField(max_length=30)
    main_category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    description = models.TextField()
    country = CountryField()
    full_image = models.ImageField(null=True, blank=True, upload_to=upload_full_image)
    created = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = "Производитель"
        verbose_name_plural = "Производители"

    def __str__(self):
        return "<manufacturer-{}>".format(strnormalize(self.name))


class Product(models.Model):
    name = models.CharField(max_length=30)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.SET_NULL, null=True)
    price = models.IntegerField()
    code = models.IntegerField(null=True, blank=True)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.SET_NULL, null=True)
    description = models.TextField(null=True, blank=True)
    full_image = models.ImageField(null=True, blank=True, upload_to=upload_full_image)
    created = models.DateTimeField(default=datetime.now)
    available = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self):
        return "<product-{}>".format(strnormalize(self.name))


class Point(models.Model):
    name = models.CharField(max_length=30)
    real_address = models.CharField(max_length=30)
    latitude = models.FloatField()
    longitude = models.FloatField()
    created = models.DateTimeField(default=datetime.now)
    open_time = models.TimeField()
    close_time = models.TimeField()

    class Meta:
        verbose_name = "Пункт выдачи"
        verbose_name_plural = "Пункты выдачи"

    def __str__(self):
        return "<point-{}>".format(strnormalize(self.name))


class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    point = models.ForeignKey(Point, on_delete=models.SET_NULL, null=True)
    cart = models.ManyToManyField(Product)
    status = models.CharField(max_length=3, choices=STATUS_CHOICE, default="I")
    created = models.DateTimeField(default=datetime.now)
    qr_hash = models.CharField(max_length=6, default=randhash6, unique=True)

    class Meta:
        verbose_name = "Транзакция"
        verbose_name_plural = "Транзакции"

    def __str__(self):
        return "<transaction-{}>".format(self.qr_hash)