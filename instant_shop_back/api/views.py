from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
import os
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from api.serializers import ProductSerializer, CitySerializer, ShopSerializer, CategorySerializer
from api.models import Product,Category,Shop, City

@csrf_exempt
def creating_objects(request):
    with open(os.path.join(os.path.dirname(__file__), 'new_file.json'), 'r') as f:
        data = json.load(f)
        for i in range(len(data)):
            name = data[i]['name']
            shop = data[i]['shop']
            category = data[i]['category']
            price = data[i]['price']
            cat = Category.objects.get(name = category)
            sh = Shop.objects.get(name=shop)
            Product.objects.create(name=name, category=cat, shop=sh, price=price)

@api_view(['GET'])
def show_products(request):
    if request.method == 'GET':
        prod = Product.objects.all()
        serializer = ProductSerializer(prod, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def show_cities(request):
    if request.method == 'GET':
        cit = City.objects.all()
        serializer = CitySerializer(cit, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def show_shops(request):
    if request.method == 'GET':
        shop = Shop.objects.all()
        serializer = ShopSerializer(shop, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def getShopsByCity(request, city_id):
    if request.method == 'GET':
        shop = Shop.objects.filter(city_id=city_id)
        serializer = ShopSerializer(shop, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def prod_by_shop(request, shop_id):
    if request.method == 'GET':
        products = Product.objects.filter(shop_id=shop_id)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def prod_detail_by_shop(request, shop_id, prod_id):
    if request.method == 'GET':
        products = Product.objects.filter(id=prod_id).filter(shop_id=shop_id)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def categories(request, shop_id):
    if request.method == 'GET':
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def prod_by_category_shop(request, shop_id, categ_id):
    if request.method == 'GET':
        products = Product.objects.filter(shop_id=shop_id).filter(category_id=categ_id)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def all_prod(request):
    if request.method == 'GET':
        prod = Product.objects.all()
        serializer = ProductSerializer(prod, many=True)
        return Response(serializer.data)