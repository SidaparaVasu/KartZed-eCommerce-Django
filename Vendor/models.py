import datetime
import os
from django.db import models

def filepath(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('product_img/', filename)

# Create your models here.
class Vendor(models.Model):
    product_key = models.AutoField(primary_key=True, max_length=16)
    prodname = models.CharField(max_length=50)
    proddescription = models.CharField(max_length=500)
    prodimage = models.ImageField(upload_to=filepath, null=True, blank=True)
    prodprice = models.CharField(max_length=20)
    discount = models.CharField(max_length=50)
