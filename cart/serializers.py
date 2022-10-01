from rest_framework import serializers
from cart.models import Cart,Product

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['product_name','cost_price','sale_price']