from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    pub = models.IntegerField()
    genre = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    is_in_stock = models.BooleanField(default=False)

class Reader(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
