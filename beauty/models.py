

from distutils.command.upload import upload
from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    pass





class Category(models.Model):
    categoryName = models.CharField(max_length=40)
    # image = models.ImageField(null=True, blank=True, upload_to="categories/")
    def __str__(self):
        return f"{self.categoryName}"


class Product(models.Model):
    image = models.URLField(null=True, blank=True)
    productName = models.CharField(max_length=40)
    price = models.FloatField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True, related_name="categoryProduct")
    information = models.CharField(max_length=500)
    quntity = models.FloatField(default=0)
    isActive = models.BooleanField(default=True)
    

class wishList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="userWish")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True, related_name="productWish") 


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="userCart")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True, related_name="productCart") 