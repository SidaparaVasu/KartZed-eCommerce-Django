# from django.db import models
from djongo import models
# from djongo.models.fields import EmbeddedField

# Create your models here.    
class Platform(models.Model):
    platform_id = models.AutoField(primary_key=True)
    platform_name = models.CharField(max_length=25, unique=True)
    
class GameFeatures(models.Model):
    game_feature_id = models.AutoField(primary_key=True)
    game_feature_name = models.CharField(max_length=25, unique=True)
    
class GameModes(models.Model):
    game_mode_id = models.AutoField(primary_key=True)
    game_mode_name = models.CharField(max_length=25, unique=True)
    
class GameCategory(models.Model):
    game_category_id = models.AutoField(primary_key=True)
    game_category_name = models.CharField(max_length=25, unique=True)


class OperatingSystems(models.Model):
    os_id = models.AutoField(primary_key=True)
    os_name = models.CharField(max_length=25, unique=True)

class OSVersions(models.Model):
    version_id = models.AutoField(primary_key=True)
    os_name = models.ForeignKey(OperatingSystems, on_delete=models.CASCADE)
    version = models.CharField(max_length=50,unique=True) 

class Processors(models.Model):
    processor_id = models.AutoField(primary_key=True)
    os_name = models.ForeignKey(OperatingSystems, on_delete=models.CASCADE)
    processor_name = models.CharField(max_length=50,unique=True)

class VideoCards(models.Model):
    vc_id = models.AutoField(primary_key=True)
    vc_name = models.CharField(max_length=50,unique=True)

class VCVersions(models.Model):
    vc_version_id = models.AutoField(primary_key=True)
    vc_name = models.ForeignKey(VideoCards, on_delete=models.CASCADE) 
    vc_version_name = models.CharField(max_length=50,unique=True)
    
class Offer(models.Model):
    offer_id = models.AutoField(primary_key=True)
    offer_name = models.CharField(max_length=225) 
    offer_description = models.CharField(max_length=220)
    offer_tc = models.CharField(max_length=220)