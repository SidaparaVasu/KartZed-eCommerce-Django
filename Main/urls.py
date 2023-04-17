"""KartZed URL Configuration

Main - application URLs
"""

from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.indexPage, name="indexPage"),
    path('login', views.render_login_page, name="render_login_page"),
    
    # Authentication
    path('user_login', views.user_login, name="user_login"),
    path('login_handle', views.login_handle, name="login_handle"),
    path('logout_handle', views.logout_handle, name="logout_handle"),
]
