from django.urls import path, include
from Authapp import views

#
urlpatterns = [
    path('',views.render_admin_login_page, name='render_admin_login_page'),
    path('admin_login',views.admin_login, name='admin_login'),

]