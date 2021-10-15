from django.db import models


class Form(models.Model):
    email = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    # phone = models.CharField(max_length=100)
    # company = models.CharField(max_length=100)
    # manager = models.CharField(max_length=100)
    # budget = models.IntegerField()
    message = models.TextField(max_length=200)
    # commented fields did not exist on template contactUs already
