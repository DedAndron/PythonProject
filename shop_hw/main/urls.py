from django.urls import path

from . import views

urlpatterns = [
    # Products
    path('', views.home, name='home'),
    path('products/<int:pk>/', views.product_detail, name='product_detail'),

    # Buyers
    path('buyers/', views.buyer_list, name='buyer_list'),
    path('buyers/<int:pk>/', views.buyer_detail, name='buyer_detail'),

    # Sellers
    path('sellers/', views.seller_list, name='seller_list'),
    path('sellers/<int:pk>/', views.seller_detail, name='seller_detail'),

    # Sales
    path('sales/', views.sale_list, name='sale_list'),
    path('sales/<int:pk>/', views.sale_detail, name='sale_detail'),
]
