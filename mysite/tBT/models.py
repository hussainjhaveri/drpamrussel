from django import forms
from django.db import models


class Form(models.Model):
    name = models.CharField(max_length=100)
<<<<<<< HEAD:mysite/tBT/models.py
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField(max_length= 200)
=======
    # phone = models.CharField(max_length=100)
    # company = models.CharField(max_length=100)
    # manager = models.CharField(max_length=100)
    # budget = models.IntegerField()
    message = models.TextField(max_length=200)
    # commented fields did not exist on template contactUs already
>>>>>>> f37b6bfac827787387a3fe309ec937234b79a627:mysite/hBE/models.py
