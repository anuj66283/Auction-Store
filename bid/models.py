from uuid import uuid4

from django.db import models
from django.contrib.auth import get_user_model

from store.models import Product

CustomUser = get_user_model()

# Create your models here.

class Bid(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, blank=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    price = models.FloatField(default=100)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    bid_date = models.DateTimeField(auto_now_add=True)
    winner = models.BooleanField(default=False, blank=True)
