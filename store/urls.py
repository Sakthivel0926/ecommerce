from django.urls import path
from .views import *

urlpatterns = [
    path('products/', get_products),
    path('products/add/', add_product),  
    path('products/<int:pk>/', update_product), 
    path('products/delete/<int:pk>/', delete_product),
]