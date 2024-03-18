from django.shortcuts import render, HttpResponse
from . import models
from . import forms


def order_product(request):
    form = forms.OrderForm(request.POST or None)
    if request.method == "POST":
        # form.save()
        print(form, form.is_valid())
    ctx = {
        "form": form
    }
    return render(request, "order.html", ctx)
