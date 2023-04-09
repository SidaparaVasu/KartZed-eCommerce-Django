from djongo import models

# Create your models here.
class Users(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    gender = models.CharField(max_length=6)
    email_id = models.CharField(max_length=320, unique=True)
    phone_number = models.CharField(max_length=10, unique=True)
    is_phone_verified = models.BooleanField(default=False)
    otp = models.CharField(max_length=6)
    user_type = models.CharField(max_length=9)
    
    class Meta:
        db_table = "Main_Users"
    
    """
    "" USER TYPES ""
    is_user
    is_admin
    is_staff
    is_vendor
    is_active
    """
    
    """
    {
        "_id": "642be6292dcaf86cb3ac2079",
        "first_name": "vasu",
        "last_name": "sidapara",
        "gender": "male",
        "email_id": "vasupatel303@gmail.com",
        "is_phone_verified": "False",
        "otp": "null",
        "user_type": "is_user"
    }
    """