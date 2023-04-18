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