"""KartZed URL Configuration

Main - application URLs
"""

from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.indexPage, name="indexPage"),
    
    # Authentication
    path('registerUser', views.registerUser, name="registerUser"),
]
