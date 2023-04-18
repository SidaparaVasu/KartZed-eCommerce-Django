from django.urls import path, include
from Administrator import views

#
urlpatterns = [
   path('',views.auth_admin, name='auth_admin'),
   path('dashboard',views.index_admin,name='index_admin'),
   path('admin_logout_handle',views.admin_logout_handle,name='admin_logout_handle'),
   
   # Users ::
   path('users',views.view_users,name='view_users'),
   
   # Platform ::
   path('platform',views.view_platform,name='view_platform'),
   path('insert-platform',views.insert_platform,name='insert_platform'),
   path('delete-platform<id>', views.delete_platform, name="delete_platform"),
   
   # Game Features ::
   path('features',views.view_game_features,name='view_game_features'),
   path('insert-feature',views.insert_game_feature,name='insert_game_feature'),
   path('delete_game_feature<id>', views.delete_game_feature, name="delete_game_feature"),
   
   # Game Modes ::
   path('modes',views.view_game_modes,name='view_game_modes'),
   path('insert-mode',views.insert_game_mode,name='insert_game_mode'),
   path('delete_game_mode<id>', views.delete_game_mode, name="delete_game_mode"),
   
   # Game Category ::
   path('category',views.view_game_category,name='view_game_category'),
   path('insert-category',views.insert_game_category,name='insert_game_category'),
   path('delete_game_category<id>', views.delete_game_category, name="delete_game_category"),

   # Game OS & Versions ::
   path('os',views.view_os,name='view_os'),
   path('insert-os',views.insert_os,name='insert_os'),
   path('insert-os-version',views.insert_os_version,name='insert_os_version'),


]