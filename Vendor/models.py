from django.db import models


# Create your models here.
class Vendor(models.Model):
    prodname = models.CharField(max_length=50)
    proddescription = models.CharField(max_length=500)
    prodimage = models.ImageField(upload_to='vendor/product_img', null=True, blank=True)
    prodprice = models.IntegerField(max_length=20)
    discount = models.CharField(max_length=50)
