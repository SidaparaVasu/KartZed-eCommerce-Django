from django.urls import path, include
from Administrator import views

#
urlpatterns = [
   path('',views.indexAdmin),
   path('indexAdmin',views.indexAdmin,name='indexAdmin'),
   
   # Category ::
   path('category',views.viewCategory,name='viewCategory'),
   path('insertCategory',views.insertCategory,name='insertCategory'),
   path('updateCategory<id>',views.updateCategory,name='updateCategory'),
   path('editCategory/<id>',views.editCategory,name='editCategory'),
   path('deleteCategory<id>', views.deleteCategory, name="deleteCategory"),

   # Sub-Category ::
   path('subCategory',views.viewSubCategory,name='subCategory'),
   path('insertSubCategory',views.insertSubCategory,name='insertSubCategory'),
   path('updateCategory<id>',views.updateSubCategory,name='updateCategory'),
   path('deleteCategory<id>', views.deleteSubCategory, name="deleteCategory"),


]