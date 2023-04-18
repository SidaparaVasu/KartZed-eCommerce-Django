from django.urls import path, include
from Administrator import views

#
urlpatterns = [
   path('',views.auth_admin, name='auth_admin'),
   path('dashboard',views.index_admin,name='index_admin'),
   path('admin_logout_handle',views.admin_logout_handle,name='admin_logout_handle'),
   
   # Platform ::
   path('platform',views.view_platform,name='view_platform'),
   path('insert_platform',views.insert_platform,name='insert_platform'),
   path('update_platform<id>',views.update_platform,name='update_platform'),
   path('edit_platform/<id>',views.edit_platform,name='edit_platform'),
   path('delete_platform<id>', views.delete_platform, name="delete_platform"),

   # Sub-Category ::
   path('users',views.view_users,name='view_users'),
   path('insert_subcategory',views.insert_subcategory,name='insert_sub_category'),
   path('update_subcategory<id>',views.update_subcategory,name='update_subcategory'),
   path('edit_subcategory/<id>',views.edit_subcategory,name='edit_subcategory'),
   path('delete_subcategory<id>', views.delete_subcategory, name="delete_subcategory"),


]