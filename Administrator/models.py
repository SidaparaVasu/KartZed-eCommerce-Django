# from django.db import models
from djongo import models
# from djongo.models.fields import EmbeddedField
import datetime
import os

# Create your models here.
def filepath(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('category_img/', filename)

class Platform(models.Model):
    platform_id = models.AutoField(primary_key=True)
    platform = models.CharField(max_length=50, unique=True)
     

class SubCategory(models.Model):
    subCategory_id = models.AutoField(primary_key=True)
    subCategory = models.CharField(max_length=50, unique=True)
    imagepath = models.ImageField(upload_to=filepath, null=True, blank=True) 
    category = models.CharField(max_length=50)