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
    
class Contact(models.Model):
    contact_id = models.AutoField(primary_key=True)
    contact_name = models.CharField(max_length=100)
    contact_email = models.CharField(unique=True, max_length=50)
    contact_message = models.CharField(max_length=50)

class Orders(models.Model):
    oid = models.AutoField(primary_key=True)
    order_id = models.CharField(unique=True, max_length=12)
    user = models.ForeignKey(Customers, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

class OrderItems(models.Model):
    order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    game = models.ForeignKey(Games, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    points = models.IntegerField()