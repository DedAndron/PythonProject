from django.db.models.query_utils import Q
from django.shortcuts import render, get_object_or_404

from .models import *


# Create your views here.

def home(request):
    products = Product.objects.all()

    return render(request, 'main/product_list.html', {
        'products': products
    })

def buyer_list(request):
    buyers = Buyer.objects.all().order_by('first_name')
    context = {
        'buyers': buyers,
    }

    return render(request, 'main/buyer_list.html', context)


def buyer_detail(request, pk):
    buyer = get_object_or_404(Buyer, pk=pk)
    return render(request, 'main/buyer_detail.html', {'buyer': buyer})

def seller_list(request):
    selected_job = request.GET.get('job_title', '')

    sellers = Seller.objects.all()

    if selected_job:
        sellers = sellers.filter(job_title=selected_job)

    return render(request, 'main/seller_list.html', {
        'sellers': sellers,
        'selected_job': selected_job
    })

def seller_detail(request, pk):
    seller = get_object_or_404(Seller, pk=pk)
    return render(request, 'main/seller_detail.html', {'seller': seller})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'main/product_detail.html', {'product': product})

def sale_list(request):
    sales = Sale.objects.select_related(
        'buyer', 'seller'
    ).prefetch_related('product')

    return render(request, 'main/sale_list.html', {
        'sales': sales
    })

def sale_detail(request, pk):
    sale = get_object_or_404(
        Sale.objects.select_related(
            'buyer', 'seller'
        ).prefetch_related('product'),
        pk=pk
    )

    sale.calculate_sum()

    return render(request, 'main/sale_detail.html', {
        'sale': sale
    })