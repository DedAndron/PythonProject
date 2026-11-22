import secrets

from django.contrib import messages
from django.contrib.auth import get_user_model
from django.db import transaction
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .models import Book, Reader


def book_list(request):
    search = request.GET.get('search', '').strip()
    available_only = request.GET.get('available') == 'true'

    books = Book.objects.all().order_by('title')

    if search:
        books = books.filter(
            Q(title__icontains=search) |
            Q(author__icontains=search) |
            Q(genre__icontains=search)
        )

    if available_only:
        books = books.exclude(borrowings__returned_at__isnull=True).distinct()

    context = {
        'books': books,
        'search': search,
        'available_only': available_only,
    }

    return render(request, 'main/book_list.html', context)


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'main/book_detail.html', {'book': book})


def reader_list(request):
    search = request.GET.get('search', '').strip()
    readers = Reader.objects.all().order_by('first_name')

    if search:
        readers = readers.filter(
            Q(first_name__icontains=search) |
            Q(last_name__icontains=search)
        )

    return render(
        request,
        'main/reader_list.html',
        {'readers': readers, 'search': search}
    )


def reader_detail(request, pk):
    reader = get_object_or_404(
        Reader.objects.prefetch_related('borrowings__book'),
        pk=pk
    )
    return render(request, 'main/reader_detail.html', {'reader': reader})