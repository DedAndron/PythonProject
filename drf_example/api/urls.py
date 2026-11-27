from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register("products", views.ProductViewSet, "products_view_set")

urlpatterns = [
    path('', include(router.urls)),
    path('sample/', views.ExampleView.as_view(), name="sample_view"),
    # path('products/', views.ProductListView.as_view(), name="productlist_view"),
    # path('product/<uuid:id>', views.ProductView.as_view(),name="product_view")
]
