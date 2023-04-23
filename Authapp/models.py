from django.db import models
import datetime, os


# Function for taking file path and set path for save into collection
def filepath(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('admin-images/', filename)

# Create your models here.
class Admins(models.Model):
    admin_id = models.AutoField(primary_key=True)
    admin_unique_keyid = models.CharField(max_length=16, unique=True)
    admin_name = models.CharField(max_length=20)
    admin_role = models.CharField(max_length=40)
    admin_email = models.CharField(max_length=20)
    admin_password = models.CharField(max_length=12)
    admin_image = models.ImageField(upload_to=filepath, null=True, blank=True)
    
class Customers(models.Model):
    cust_id            = models.AutoField(primary_key=True)
    cust_unique_keyid  = models.CharField(max_length=16, unique=True)
    cust_first_name    = models.CharField(max_length=20)
    cust_last_name     = models.CharField(max_length=20)
    cust_gender        = models.CharField(max_length=6)
    cust_email         = models.CharField(max_length=20)
    cust_phone_number  = models.CharField(max_length=13)
    is_phone_verified  = models.BooleanField(default=False)
    otp                = models.CharField(max_length=6)
    cust_country       = models.CharField(max_length=25)
    cust_state         = models.CharField(max_length=25)
    cust_city          = models.CharField(max_length=25)
    cust_address       = models.CharField(max_length=50)
    
    
class Vendors(models.Model):
    vendor_id = models.AutoField(primary_key=True)
    vendor_unique_keyid = models.CharField(max_length=16, unique=True)
    vendor_fullname = models.CharField(max_length=20)
    vendor_password = models.CharField(max_length=12)
    vendor_email = models.CharField(max_length=20, unique=True)
    vendor_phone_number = models.CharField(max_length=10, unique=True)
    company_name = models.CharField(max_length=30, unique=True)
    company_address = models.CharField(max_length=50)
    company_phone_number = models.CharField(max_length=10, unique=True)
    GSTIN = models.CharField(max_length=15, unique=True)
    pickup_pincode = models.CharField(max_length=10)
    pickup_address = models.CharField(max_length=50)