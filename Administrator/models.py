# from django.db import models
from djongo import models
# from djongo.models.fields import EmbeddedField
import datetime
import os

# Create your models here.
    
class GameFeatures(models.Model):
    game_feature_id = models.AutoField(primary_key=True)
    game_feature_name = models.CharField(max_length=25, unique=True)
    
class GameModes(models.Model):
    game_mode_id = models.AutoField(primary_key=True)
    game_mode_name = models.CharField(max_length=25, unique=True)
    
class GameCategory(models.Model):
    game_category_id = models.AutoField(primary_key=True)
    game_category_name = models.CharField(max_length=25, unique=True)