from djongo import models

# Create your models here.
class Users(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    gender = models.CharField(max_length=6)
    email_id = models.CharField(max_length=320, unique=True)
    phone_number = models.IntegerField(max_length=10, unique=True)
    is_phone_verified = models.BooleanField(default=False)
    otp = models.CharField(max_length=6)
    user_type = models.IntegerField(max_length=1)