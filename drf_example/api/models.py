from django.db import models

import uuid

class Product(models.Model):
    id = models.UUIDField(primary_key=True,
                          default=uuid.uuid4)
    name = models.CharField(max_length=255)
    price = models.FloatField()
    description = models.TextField(null=True)
    
    class Meta:
        db_table="drf_products"

class Category(models.Model):
    id = models.UUIDField(primary_key=True,
                          default=uuid.uuid4)
    name = models.CharField(max_length=255)