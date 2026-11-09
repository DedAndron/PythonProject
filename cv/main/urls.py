from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home, name='home'),
    path('cv/', views.cv, name='cv'),
    path('cv', views.cv, name='cv'),
]