from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('card/<int:card_id>/', views.get_card, name='card'),
    path('search/', views.search, name='search'),
]