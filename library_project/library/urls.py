from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    # Books
    path('', views.book_list, name='book_list'),
    path('books/', views.book_list, name='book_list'),
    path('books/<int:pk>/', views.book_detail, name='book_detail'),

    # Readers
    path('readers/', views.reader_list, name='reader_list'),
    path('readers/<int:pk>/', views.reader_detail, name='reader_detail'),

    # Authentication
    path(
        'login/',
        auth_views.LoginView.as_view(
            template_name='library/login.html'
        ),
        name='login'
    ),

    path(
        'logout/',
        auth_views.LogoutView.as_view(),
        name='logout'
    ),
]