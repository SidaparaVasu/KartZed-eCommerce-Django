import datetime, os, random
from django.utils import timezone
from django.db import models
from Administrator.models import *
from Authapp.models import Vendors

def game_logo_filepath(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('product_img/game_logos/', filename)

def game_image_filepath(request, filename):
    while True:
        folder_name = str(random.randint(100000, 999999))
        folder_path = os.path.join('product_img/game_images/', folder_name)
        # Check if the directory already exists
        if not os.path.exists(folder_path):
            break
    
    # Return the path to the file within the new directory
    timestamp = timezone.now().strftime('%Y%m%d-%H%M%S')
    filename = f"{timestamp}_{filename}"
    
    return os.path.join(folder_path, filename)

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
    game_languages     = models.JSONField(default=list)
    game_release_date  = models.CharField(max_length=6) 
    game_price         = models.IntegerField() 
    avail_stock        = models.IntegerField() 
    discount           = models.CharField(max_length=3) 
    
    # features
    game_features      = models.JSONField(default=list)
    game_modes         = models.JSONField(default=list)
    game_categories    = models.JSONField(default=list)
    
    # Minimum Requirements (mr - minimum requirements)
    platform_names     = models.JSONField(default=list)
    os_names           = models.CharField(max_length=100)
    os_versions        = models.CharField(max_length=100)
    processors_names   = models.CharField(max_length=100)
    vc_names           = models.CharField(max_length=100)
    vc_versions        = models.CharField(max_length=100)
    
class GameImages(models.Model):
    game = models.ForeignKey(Games, on_delete=models.CASCADE, related_name='images')
    images = models.ImageField(upload_to=game_image_filepath, null=True, blank=True)

class Vendor_Contact(models.Model):
    contact_id = models.AutoField(primary_key=True)
    contact_name = models.CharField(max_length=100)
    contact_email = models.EmailField()
    contact_message = models.TextField()