from django.db.models import Q
from django.shortcuts import get_object_or_404, render

from .models import *

# Create your views here.

def book_list(request):
    search = request.GET.get('search', '')

    books = Book.objects.all().order_by('title')

    if search:
        books = books.filter(
            Q(title__icontains=search)
        )

    context = {
        'books': books,
        'search': search
    }

    return render(request, 'main/book_list.html', context)


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    context = {
        'book': book
    }
    return render(request, 'main/book_detail.html', context)

def reader_list(request):
    search = request.GET.get('search', '')

    readers = Reader.objects.all().order_by('first_name')

    if search:
        readers = readers.filter(
            Q(first_name__icontains=search) |
            Q(last_name__icontains=search)
        )

    context = {
        'readers': readers,
        'search': search
    }

    return render(request, 'main/reader_list.html', context)


def reader_detail():
    return None