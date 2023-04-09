"""KartZed URL Configuration

Main - application URLs
"""

from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.indexPage, name="indexPage"),
    path('login', views.render_login_page, name="render_login_page"),
    
    # Authentication
    path('userLogin', views.userLogin, name="userLogin"),
    path('verify_otp', views.verify_otp, name="verify_otp"),
    
    path('logoutHandle', views.logoutHandle, name="logoutHandle"),
]
