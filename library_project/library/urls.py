from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('books/', views.book_list, name='book_list'),
    path('books/<int:pk>/', views.book_detail, name='book_detail'),
    path('readers/', views.reader_list, name='reader_list'),
    path('readers/<int:pk>/', views.reader_detail, name='reader_detail'),

]