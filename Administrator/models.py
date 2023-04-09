from django.db import models

import datetime
import os

# Create your models here.
def filepath(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('uploads/', filename)

class category(models.Model):
    category = models.CharField(max_length=50)
    path = models.ImageField(upload_to=filepath, null=True, blank=True) 