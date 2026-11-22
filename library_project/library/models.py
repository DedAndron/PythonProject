from django.db import models
from django.db.models import Q


class Book(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='Book Title'
    )

    author = models.CharField(
        max_length=150,
        verbose_name='Author'
    )

    publication_year = models.PositiveIntegerField(
        verbose_name='Publication Year'
    )

    genre = models.CharField(
        max_length=100,
        verbose_name='Genre'
    )

    publisher = models.CharField(
        max_length=150,
        verbose_name='Publisher'
    )

    readers = models.ManyToManyField(
        'Reader',
        through='Borrowing',
        related_name='books',
        blank=True
    )

    @property
    def is_available(self):
        return not self.borrowings.filter(
            returned_at__isnull=True
        ).exists()

    def __str__(self):
        return self.title


class Reader(models.Model):
    first_name = models.CharField(
        max_length=100,
        verbose_name='First Name'
    )

    last_name = models.CharField(
        max_length=100,
        verbose_name='Last Name'
    )

    phone = models.CharField(
        max_length=20,
        verbose_name='Contact Phone'
    )

    email = models.EmailField(
        unique=True,
        verbose_name='Email'
    )

    registration_date = models.DateField(
        auto_now_add=True,
        verbose_name='Registration Date'
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Borrowing(models.Model):
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name='borrowings',
        verbose_name='Book'
    )

    reader = models.ForeignKey(
        Reader,
        on_delete=models.CASCADE,
        related_name='borrowings',
        verbose_name='Reader'
    )

    borrowed_at = models.DateField(
        auto_now_add=True,
        verbose_name='Borrowing Date'
    )

    returned_at = models.DateField(
        null=True,
        blank=True,
        verbose_name='Return Date'
    )

    def __str__(self):
        return f'{self.book.title} - {self.reader}'