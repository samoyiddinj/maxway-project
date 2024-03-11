from django.db import models
from dynamic.product.models import Product
from dynamic.user.models import User


class Bucket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class BucketItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL
                                , null=True)
    count = models.SmallIntegerField(default=1, null=True)
