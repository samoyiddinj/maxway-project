from django.db import models
from django.db.models.fields import SmallIntegerField
from dynamic.bucket.models import Bucket
from dynamic.user.models import User
from dynamic.product.models import Product


class Order(models.Model):
    bucket = models.ForeignKey(Bucket, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    address = models.TextField(max_length=70, null=True, blank=False)
    order_date = models.DateTimeField(auto_now_add=True)


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    count = SmallIntegerField(default=1, null=False, blank=False)
