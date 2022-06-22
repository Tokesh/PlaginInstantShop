from django.contrib import admin
from api.models import Category, Product,Shop,City
from django.views.decorators.csrf import csrf_exempt
# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Shop)
admin.site.register(City)