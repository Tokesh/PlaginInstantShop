from django.db import models
import json, jsonfield

class City(models.Model):
    name = models.CharField(max_length=250)
    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'
        # ordering = ('name',)

    def to_json(self):
        return {
            'name': self.name,
        }

    def __str__(self):
        return f'{self.id}: {self.name}'


class Shop(models.Model):
    name = models.CharField(max_length=250)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='shop')
    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазины'
        # ordering = ('name',)

    def to_json(self):
        return {
            'name': self.name,
        }

    def __str__(self):
        return f'{self.id}: {self.name}'


class Category(models.Model):
    name = models.CharField(max_length=250)
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        # ordering = ('name',)

    def to_json(self):
        return {
            'name': self.name,
        }

    def __str__(self):
        return f'{self.id}: {self.name}'
#add shop to front
class Product(models.Model):
    name = models.CharField(max_length=250)
    category = models.ForeignKey(Category,on_delete=models.CASCADE, related_name='products')
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='products')
    price = models.IntegerField()
    filename = models.TextField(default = "0.jpg")
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        # ordering = ('name',)

    def to_json(self):
        return {
            'name': self.name,
            'category':self.category,
            'shop':self.shop,
            'price':self.price
        }

    def __str__(self):
        return f'{self.id}: {self.name}'
