from rest_framework import serializers
from products.models import Product, SubCategory, Category
from django.db.models import Q
from rest_framework.response import Response
from django.conf import settings
from django.contrib.auth.models import User


class CategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = Category
		fields = ['name',]


class SubCategorySerializer(serializers.ModelSerializer):
	count = serializers.SerializerMethodField()

	class Meta:
		model = SubCategory
		fields = ['name', 'category', 'count']

	def get_count(self, obj):
		return Product.objects.filter(subcategory__name=obj.name).count()


class ShortProductSerializer(serializers.ModelSerializer):
	subcategory = SubCategorySerializer(read_only=True)
	category = CategorySerializer(read_only=True)
	image_url = serializers.SerializerMethodField()
	
	class Meta:
		model = Product
		fields = ['id', 'name', 'created', 'price', 'image_url', 'subcategory', 'category']

	def get_image_url(self, obj):
		if obj.full_image:
			return "{0}{1}".format(settings.BASE_URL, obj.full_image.url)
		else:
			return None


class ProductSerializer(serializers.ModelSerializer):
	subcategory = SubCategorySerializer(read_only=True)
	image_url = serializers.SerializerMethodField()

	class Meta:
		model = Product
		fields = ['id', 'name', 'description', 'manufacturer', 'subcategory', 'available', 'created', 'image_url', 'code']

	def get_image_url(self, obj):
		if obj.full_image:
			return "{0}{1}".format(settings.BASE_URL, obj.full_image.url)
		else:
			return None



