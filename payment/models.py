from django.db import models
from product.models import *
from buyer.models import *

# Create your models here.
class Payment(models.Model):
    bid = models.ForeignKey(Bid, on_delete=models.SET_NULL, null=True, blank=True)
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE, null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_time = models.DateTimeField()
