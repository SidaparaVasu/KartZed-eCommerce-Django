import datetime
import os
from django.db import models
from Administrator.models import *

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
    
    game_logo          = models.ImageField(upload_to=game_logo_filepath, null=True, blank=True) #•
    game_name          = models.CharField(max_length=25)#•
    game_description   = models.CharField(max_length=300)#•
    game_developer     = models.CharField(max_length=25)#•
    game_publisher     = models.CharField(max_length=25)#•
    
    game_storage       = models.CharField(max_length=6)   # mr #•
    game_ram           = models.CharField(max_length=3)   # mr
    game_languages     = models.CharField(max_length=25)
    game_release_date  = models.CharField(max_length=6) #•
    game_price         = models.IntegerField() #•
    avail_stock        = models.IntegerField() #•
    discount           = models.CharField(max_length=3) #•
    
    game_image         = models.ImageField(upload_to=game_image_filepath, null=True, blank=True)
    
    # features
    game_feature       = models.ForeignKey(GameFeatures, on_delete=models.CASCADE)  # Single, Multi Player
    game_modes         = models.ForeignKey(GameModes, on_delete=models.CASCADE)     # Battle Royale, Open World
    game_category      = models.ForeignKey(GameCategory, on_delete=models.CASCADE)  # Action, Casual
    
    # requirements
    
    # Minimum Requirements (mr - minimum requirements)
    platform_name      = models.ForeignKey(Platform, on_delete=models.CASCADE)
    os_name            = models.ForeignKey(OperatingSystems, on_delete=models.CASCADE)
    os_version         = models.ForeignKey(OSVersions, on_delete=models.CASCADE)
    processors_name    = models.ForeignKey(Processors, on_delete=models.CASCADE)
    vc_name            = models.ForeignKey(VideoCards, on_delete=models.CASCADE)
    vc_version         = models.ForeignKey(VCVersions, on_delete=models.CASCADE)