from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework import authentication, permissions, status
from rest_framework.permissions import AllowAny
from django.db.models import Q, Count, Exists
from rest_framework.viewsets import ModelViewSet
from itertools import chain
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from datetime import datetime
from products.models import Product, Category, SubCategory
from .serializers import ShortProductSerializer, ProductSerializer, CategorySerializer, SubCategorySerializer
from rest_framework.decorators import api_view

	
class ProductsView(ListAPIView):
	queryset = Product.objects.filter(available=True).order_by('-created')
	permission_classes = (AllowAny,)
	serializer_class = ShortProductSerializer


class CategoriesView(ListAPIView):
	queryset = Category.objects.all()
	permission_classes = (AllowAny,)
	serializer_class = CategorySerializer


class SubCategoriesView(ListAPIView):
	queryset = SubCategory.objects.all()
	permission_classes = (AllowAny,)
	serializer_class = SubCategorySerializer


@api_view(['GET', 'PUT', 'DELETE'])
def get_post(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    elif request.method == 'PUT':
        # serializer = SnippetSerializer(snippet, data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        pass

    elif request.method == 'DELETE':
        # snippet.delete()
        # return Response(status=status.HTTP_204_NO_CONTENT)
        pass

