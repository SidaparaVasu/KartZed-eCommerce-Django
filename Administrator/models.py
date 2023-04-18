# from django.db import models
from djongo import models
# from djongo.models.fields import EmbeddedField

# Create your models here.

class Platform(models.Model):
    platform_id = models.AutoField(primary_key=True)
    platform = models.CharField(max_length=50, unique=True)
    