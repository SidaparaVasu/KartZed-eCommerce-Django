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
   path('delete_platform<id>', views.delete_platform, name="delete_platform"),
   
   # Game Features ::
   path('game_features',views.view_game_features,name='view_game_features'),
   path('insert_game_feature',views.insert_game_feature,name='insert_game_feature'),
   path('delete_game_feature<id>', views.delete_game_feature, name="delete_game_feature"),
   
   # Game Modes ::
   path('game_modes',views.view_game_modes,name='view_game_modes'),
   path('insert_game_mode',views.insert_game_mode,name='insert_game_mode'),
   path('delete_game_mode<id>', views.delete_game_mode, name="delete_game_mode"),
]