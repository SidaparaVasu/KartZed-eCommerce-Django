from django.urls import path, include
from Vendor import views

urlpatterns = [
   path('',views.index_vendor, name='index_vendor'),
   
   # Games
   path('game',views.view_game,name="view_game"),
   path('insert-game',views.insert_game,name='insert_game')
]