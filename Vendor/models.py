import datetime
import os
from django.db import models
from Administrator.models import *
from Authapp.models import Vendors

def game_logo_filepath(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('product_img/game_logos', filename)

def game_image_filepath(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('product_img/game_images', filename)

# Create your models here.
class Games(models.Model):
    gid                = models.AutoField(primary_key=True)
    product_key        = models.CharField(unique=True, max_length=16)
    
    vendor_reference = models.ForeignKey(Vendors, on_delete=models.CASCADE)
    
    game_logo          = models.ImageField(upload_to=game_logo_filepath, null=True, blank=True) 
    game_name          = models.CharField(max_length=25)
    game_description   = models.CharField(max_length=300)
    game_developer     = models.CharField(max_length=25)
    game_publisher     = models.CharField(max_length=25)
    
    game_storage       = models.CharField(max_length=6) 
    game_ram           = models.CharField(max_length=3)
    game_languages     = models.CharField(max_length=25)
    game_release_date  = models.CharField(max_length=6) 
    game_price         = models.IntegerField() 
    avail_stock        = models.IntegerField() 
    discount           = models.CharField(max_length=3) 
    
    game_images        = models.ImageField(upload_to=game_image_filepath, null=True, blank=True)
    
    # features
    game_features      = models.CharField(max_length=100)
    game_modes         = models.CharField(max_length=100)
    game_categories    = models.CharField(max_length=100)
    
    # Minimum Requirements (mr - minimum requirements)
    platform_names     = models.CharField(max_length=100)
    os_names           = models.CharField(max_length=100)
    os_versions        = models.CharField(max_length=100)
    processors_names   = models.CharField(max_length=100)
    vc_names           = models.CharField(max_length=100)
    vc_versions        = models.CharField(max_length=100)