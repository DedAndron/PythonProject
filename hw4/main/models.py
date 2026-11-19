from django.db import models

# Create your models here.

class Contact(models.Model):

    first_name = models.CharField(
        max_length=100,
        verbose_name='First name'
    )

    last_name = models.CharField(
        max_length=100,
        verbose_name='Last name'
    )

    email = models.EmailField(
        verbose_name='Email'
    )

    phone = models.CharField(
        max_length=20,
        verbose_name='Phone number'
    )

    notes = models.TextField(
        blank=True,
        verbose_name='Notes'
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'