from djongo import models
from Authapp.models import *
from Vendor.models import *

# Create your models here.

class Cart(models.Model):
    cart_id = models.AutoField(primary_key=True)
    cust_id = models.ForeignKey(Customers, on_delete=models.CASCADE)
    is_paid = models.BooleanField(default=False)

class CartItems(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    game = models.ForeignKey(Games, on_delete=models.SET_NULL, null=True,blank=True)
    
