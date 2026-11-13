from django.db import models

# Create your models here.

class Card(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    created_at = models.DateTimeField()
class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    hashed_password = models.CharField(max_length=200)
    email = models.EmailField()
    is_active = models.BooleanField(default=True)
    refresh_token = models.CharField(max_length=200)