"""KartZed URL Configuration

Main - application URLs
"""

from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.indexPage, name="indexPage"),
    path('login', views.render_login_page, name="render_login_page"),
    path('account', views.render_account_page, name="render_account_page"),
    
    
    # Authentication
    path('user_login', views.user_login, name="user_login"),
    path('login_handle', views.login_handle, name="login_handle"),
    path('logout_handle', views.logout_handle, name="logout_handle"),
    
    # Update User profile
    path('update_user_profile', views.update_user_profile, name="update_user_profile"),
    
]
