from django.urls import path, include
from Authapp import views

#
urlpatterns = [
    path('',views.render_admin_login_page, name='render_admin_login_page'),
    path('admin_login',views.admin_login, name='admin_login'),
    
    path('change_password_page',views.change_password_page, name='change_password_page'),
    path('forgot_password_page',views.forgot_password_page, name='forgot_password_page'),
    path('verify_otp_page',views.verify_otp_page, name='verify_otp_page'),
    path('upd_password_page',views.upd_password_page, name='upd_password_page'),
    
    path('admin_change_password',views.admin_change_password, name='admin_change_password'),
    path('forgot_password',views.forgot_password, name='forgot_password'),
    path('verify_forgot_password_otp',views.verify_forgot_password_otp, name='verify_forgot_password_otp'),
    path('new_password',views.new_password, name='new_password'),
]