from django.urls import path, include
from Administrator import views

#
urlpatterns = [
   path('',views.auth_admin, name='auth_admin'),
   path('dashboard',views.index_admin,name='index_admin'),
   path('admin_logout_handle',views.admin_logout_handle,name='admin_logout_handle'),
   
   # Category ::
   path('category',views.view_category,name='view_category'),
   path('insert_category',views.insert_category,name='insert_category'),
   path('update_category<id>',views.update_category,name='update_category'),
   path('edit_category/<id>',views.edit_category,name='edit_category'),
   path('delete_category<id>', views.delete_category, name="delete_category"),

   # Sub-Category ::
   path('subcategory',views.view_subcategory,name='view_subcategory'),
   path('insert_subcategory',views.insert_subcategory,name='insert_sub_category'),
   path('update_subcategory<id>',views.update_subcategory,name='update_subcategory'),
   path('edit_subcategory/<id>',views.edit_subcategory,name='edit_subcategory'),
   path('delete_subcategory<id>', views.delete_subcategory, name="delete_subcategory"),


]