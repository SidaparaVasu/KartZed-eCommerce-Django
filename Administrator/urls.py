from django.urls import path, include
from Administrator import views

#
urlpatterns = [
   path('',views.indexAdmin),
   path('indexAdmin',views.indexAdmin,name='indexAdmin'),
   
   path('category',views.viewCategory,name='viewCategory'),
   path('insertCategory',views.insertCategory,name='insertCategory'),
   path('updateCategory<id>',views.updateCategory,name='updateCategory'),
   path('editCategory/<id>',views.editCategory,name='editCategory'),
   path('deleteCategory<id>', views.deleteCategory, name="deleteCategory"),
]