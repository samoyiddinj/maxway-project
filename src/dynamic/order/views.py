from django.shortcuts import render, HttpResponse
from . import models


def order_product(request):
    return render(request, 'order.html', {})
