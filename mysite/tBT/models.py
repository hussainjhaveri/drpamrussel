from django import forms
from django.db import models





class Form(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField(max_length= 200)
