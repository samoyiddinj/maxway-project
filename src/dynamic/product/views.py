from django.shortcuts import render

from dynamic.product.models import Product, Category


def index(request):
    categories = Category.objects.prefetch_related('product_set').all()
    ctx = {
        'categories': categories
    }
    return render(request, 'index.html', ctx)
