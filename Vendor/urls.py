from django.urls import path, include
from Vendor import views
from .forms import registervendor
from Administrator.views import auth_admin



urlpatterns = [
   path('',views.index_vendor, name='index_vendor'),
   # path('', auth_admin, name='auth_admin'),
   
   #path('vendorlogin/', login, name='login'),
   path('add_product', views.add_product, name='add_product'),
   path('view_product', views.view_product, name="view_product"),
   path('update_product<id>',views.update_product,name='update_product'),
   path('edit_product/<product_key>', views.edit_product,name="edit_product"),
   path('delete_product/<product_key>', views.delete_product,name="delete_product"),
]