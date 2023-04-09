from django.urls import path, include
from Administrator import views

#
urlpatterns = [
   path('',views.indexAdmin),
   path('indexAdmin',views.indexAdmin,name='indexAdmin'),
   
   path('category',views.viewCategory,name='viewCategory'),
   path('insertCategory',views.insertCategory,name='insertCategory'),

]