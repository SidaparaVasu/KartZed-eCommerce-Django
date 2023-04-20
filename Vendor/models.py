import datetime
import os
from django.db import models
from Administrator.models import *

def filepath(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('product_img/', filename)

# Create your models here.
class Games(models.Model):
    product_key     = models.AutoField(primary_key=True, max_length=16)
    game_developer  = models.CharField(max_length=50)
    game_name       = models.CharField(max_length=50)
    game_publisher  = models.CharField(max_length=50)
    game_description= models.CharField(max_length=500)
    platform_name   = models.ForeignKey(Platform, on_delete=models.CASCADE)
    game_feature    = models.ForeignKey(GameFeatures, on_delete=models.CASCADE)
    game_modes      = models.ForeignKey(GameModes, on_delete=models.CASCADE)
    game_category   = models.ForeignKey(GameCategory, on_delete=models.CASCADE)
    os_name         = models.ForeignKey(OperatingSystems, on_delete=models.CASCADE)
    os_version      = models.ForeignKey(OSVersions, on_delete=models.CASCADE)
    processors_name = models.ForeignKey(Processors, on_delete=models.CASCADE)
    vc_name         = models.ForeignKey(VideoCards, on_delete=models.CASCADE)
    vc_version      = models.ForeignKey(VCVersions, on_delete=models.CASCADE)
    game_ram        = models.CharField(max_length=10)
    game_languages  = models.CharField(max_length=25)
    game_regions    = models.CharField(max_length=50)
    game_price      = models.IntegerField(max_length=5)
    avail_stock     = models.IntegerField(max_length=5)
    discount        = models.CharField(max_length=50)
