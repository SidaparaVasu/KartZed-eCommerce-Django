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
        path('view_browse/', views.view_browse, name="view_browse"),
    
    # Authentication
    path('customer_login', customer_login, name="customer_login"),
    path('customer_login_handle', customer_login_handle, name="customer_login_handle"),
    path('customer_logout_handle', customer_logout_handle, name="customer_logout_handle"),
    
    # Update User profile
    path('update_customer_profile', update_customer_profile, name="update_customer_profile"),

    # Cart
    path('view_cart',views.view_cart,name="view_cart"),
    path('add_to_cart/<id>',views.add_to_cart,name="add_to_cart"),

    #view game page
    path('view_game_page/<str:product_key>', views.view_game_detail, name="game_details"), 

    #contact
    path('contact_view/', views.contact_view, name="contact_view"),
    path('contact_view/insert_contact', views.insert_contact, name="insert_contact"),

]
