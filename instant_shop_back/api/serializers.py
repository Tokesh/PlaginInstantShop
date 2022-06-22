from rest_framework import serializers
from .models import City,Shop,Category,Product

class ProductSerializer(serializers.ModelSerializer):
    #category = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'category', 'shop', 'price')


class CitySerializer(serializers.ModelSerializer):
    #category = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = City
        fields = ('id', 'name')


class ShopSerializer(serializers.ModelSerializer):

    class Meta:
        model = Shop
        fields = ('id', 'name', 'city')


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Shop
        fields = ('id', 'name')