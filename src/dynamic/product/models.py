from django.db import models
from dynamic.user.models import User


class Category(models.Model):
    name = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField()
    image = models.ImageField(upload_to='images', null=True, blank=True)
    price = models.IntegerField(null=False, blank=False)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=False)
    is_available = models.BooleanField(default=False)

    def __str__(self):
        return self.title
