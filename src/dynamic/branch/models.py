from django.db import models


class Branch(models.Model):

    name = models.CharField(max_length=100)
    address_name = models.CharField(max_length=100)
    work_time = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=13, null=False, blank=False)
    status = models.SmallIntegerField(choices=[(1, "Ochiq"), (2, "Yopiq")])

