from django.urls import path, include
from Vendor import views
from Authapp.views import register_vendor, admin_login, vendor_login

urlpatterns = [
   path('', views.index_vendor, name='index_vendor'),
   
   # Vendor Register Form
   path('become-a-seller', views.render_vendor_register_page, name='render_vendor_register_page'),
   path('register-vendor', register_vendor, name="register-vendor") ,
   path('login-vendor', views.render_vendor_login_page, name="render_vendor_login_page"),
   path('vendor-login', vendor_login, name="vendor_login"),
   
   # Games
   path('game',views.view_game,name="view_game"),
   path('insert_game',views.insert_game,name='insert_game')
]