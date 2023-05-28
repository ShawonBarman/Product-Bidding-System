from django.db import models
from django.contrib.auth.models import User

class Buyer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    buyer_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=200)
    profile_pic = models.ImageField(default='default.png', upload_to='buyer_picture')

class AuthenticateForBuyer(models.Model):
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE, null=True, blank=True)
    password = models.CharField(max_length=50)
