from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token
from api.views import creating_objects, show_products, show_cities, show_shops,getShopsByCity,prod_by_shop,prod_detail_by_shop, categories,prod_by_category_shop, all_prod


urlpatterns=[
    path('login/', obtain_jwt_token),
    path('daily_update/', creating_objects),
    path('products/',show_products),
    path('shops/<int:shop_id>/products/', prod_by_shop),
    path('shops/<int:shop_id>/products/<int:prod_id>/',prod_detail_by_shop),
    path('shops/<int:shop_id>/categories/<int:categ_id>/products/',prod_by_category_shop),
    path('shops/<int:shop_id>/categories/', categories),
    path('cities/',show_cities),
    path('shops/',show_shops),
    path('cities/<int:city_id>/', getShopsByCity),
    path('all_products/', all_prod)
]