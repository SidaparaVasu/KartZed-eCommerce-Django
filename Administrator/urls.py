from django.urls import path, include
from Administrator import views
urlpatterns = [
   path('',views.indexAdmin),
]