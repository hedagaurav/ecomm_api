from pprint import pprint
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics
# from cart.models import Product
# from cart.serializers import ProductSerializer
# Create your views here.
class ProductView(generics.ListCreateAPIView):
    pass
    # queryset = Product.objects.all()
    # print(queryset)
    # serializer_class = ProductSerializer