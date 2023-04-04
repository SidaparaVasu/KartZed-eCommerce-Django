"""KartZed URL Configuration

Main - application URLs
"""

from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.indexPage, name="indexPage"),
    path('esehi', views.esehi, name="esehi"),
    
    # Authentication
    path('userLogin', views.userLogin, name="userLogin"),
    path('verify_otp', views.verify_otp, name="verify_otp"),
]
