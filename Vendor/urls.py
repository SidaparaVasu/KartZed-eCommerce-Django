from django.urls import path, include
from Vendor import views
from .forms import registervendor



urlpatterns = [
   path('/',views.indexVendor),
   #path('vendorlogin/', login, name='login'),
   path('/addproduct/', views.addproduct, name='addproduct'),
   #path('addproduct/', views.addproduct, name="addproduct"),
]