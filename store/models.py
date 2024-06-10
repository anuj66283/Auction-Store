from uuid import uuid4
from django.db import models
from django.contrib.auth import get_user_model

CustomUser = get_user_model()

# Create your models here.
UNITS = (('KG', 'KG'), ('meter', 'meter'), ('liter', 'liter'), ('pieces', 'pieces'))

PRODUCT_STATUS = (('available', 'available'), ('bidded', 'bidded'), ('expired', 'expired'))

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50, primary_key=True, default="unnamed", blank=True)

class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=True)
            
class Product(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, blank=True)
    title = models.CharField(max_length=100)
    desc = models.TextField(max_length=500)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    quantity = models.FloatField(default=1)
    price = models.FloatField(default=100)
    unit = models.CharField(max_length=20, choices=UNITS)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=PRODUCT_STATUS, default="available")
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True)

class ProductImage(models.Model): 
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='images/products')

class ProductHistory(models.Model):
    buyer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    bought_date = models.DateTimeField(auto_now_add=True)