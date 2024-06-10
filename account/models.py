from uuid import uuid4
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    id = models.UUIDField(default=uuid4, blank=True, primary_key=True)
    is_buyer = models.BooleanField(default=True, blank=True)
    is_verified = models.BooleanField(default=False, blank=True)
    phone = models.CharField(max_length=10)
    date_created = models.DateTimeField(auto_now_add=True, blank=True)
    login_date = models.DateTimeField(auto_now=True, blank=True)
    code = models.IntegerField(default=0, blank=True)

class BuyerUser(models.Model):
    buyer = models.OneToOneField(User, on_delete=models.CASCADE)
    profile = models.ImageField(upload_to="images/profile", blank=True, null=True)

class SellerUser(models.Model):
    seller = models.OneToOneField(User, on_delete=models.CASCADE)
    profile = models.ImageField(upload_to="images/profile")
    district = models.CharField(max_length=50)
    full_address = models.CharField(max_length=100)
    