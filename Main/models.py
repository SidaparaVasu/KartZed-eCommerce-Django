from djongo import models

# Create your models here.
class Users(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    gender = models.CharField(max_length=1)
    email_id = models.CharField(max_length=25)
    mobile_no = models.IntegerField(max_length=10)
    user_type = models.IntegerField(max_length=1)