from django.urls import path
from . import views

urlpatterns = [
    path('', views.order_product, name='order')
]