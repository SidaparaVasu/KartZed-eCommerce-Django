"""KartZed URL Configuration

Main - application URLs
"""

from . import views
from django.urls import path, include
from Authapp.views import render_customer_login_page, customer_login
from Authapp.views import customer_login_handle, customer_logout_handle, update_customer_profile

urlpatterns = [
    path('', views.indexPage, name="indexPage"),
    path('login', render_customer_login_page, name="render_customer_login_page"),
    path('account', views.render_account_page, name="render_account_page"),
    
    # Authentication
    path('customer_login', customer_login, name="customer_login"),
    path('customer_login_handle', customer_login_handle, name="customer_login_handle"),
    path('customer_logout_handle', customer_logout_handle, name="customer_logout_handle"),
    
    # Update User profile
    path('update_customer_profile', update_customer_profile, name="update_customer_profile"),
    
]
