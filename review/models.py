from uuid import uuid4
from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator 

from store.models import Product

CustomUser = get_user_model()

# Create your models here.

class Review(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True)
    buyer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="buyer")
    seller = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="seller")
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], default=1)
    review = models.CharField(max_length=250, blank=True, null=True)
    review_date = models.DateTimeField(auto_now_add=True)