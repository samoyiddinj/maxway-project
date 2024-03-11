from django.urls import path
from . import views

urlpatterns = [
    path('', views.bucket, name='bucket')
]