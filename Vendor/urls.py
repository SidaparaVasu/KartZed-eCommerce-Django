from django.urls import path, include
from Vendor import views
from .forms import registervendor



urlpatterns = [
   path('/',views.indexVendor),
   #path('vendorlogin/', login, name='login'),
   path('/addproduct', views.addproduct, name='addproduct'),
   path('/viewproduct', views.viewproduct, name="viewproduct"),
   path('/editproduct<id>', views.editproduct,name="prod-edit"),
   path('/deleteproduct<id>', views.deleteproduct,name="prod-delete"),
]