from django.urls import path
from .views import get_products, add_product, delete_product

urlpatterns = [
    path('products/', get_products),
    path('products/add/', add_product),
     path('products/delete/<int:id>/', delete_product), 
]