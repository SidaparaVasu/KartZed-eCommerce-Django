from django.urls import path, include
from Vendor import views
from Authapp.views import register_vendor, admin_login, vendor_login, vendor_logout_handle

urlpatterns = [
   path('', views.render_vendor_login_page, name='render_vendor_login_page'), 
   path('vendor_logout_handle', vendor_logout_handle, name="vendor_logout_handle"),
   path('dashboard', views.index_vendor, name='index_vendor'), 
   
   # Vendor Register Form
   path('become-a-seller', views.render_vendor_register_page, name='render_vendor_register_page'),
   path('register-vendor', register_vendor, name="register-vendor") ,
   path('login-vendor', views.render_vendor_login_page, name="render_vendor_login_page"),
   path('vendor-login', vendor_login, name="vendor_login"),
   
   # Games
   path('add-game',views.add_game_page,name="add_game_page"),
   path('insert_game',views.insert_game,name='insert_game'),
   path('games_csv_upload',views.games_csv_upload,name='games_csv_upload'),
   path('show-games', views.show_games_page, name="show_games_page"),
   path('show-game-details/<prod_key>', views.show_game_details, name="show_game_details"),
    
    # bulk upload game data
   path('show-game-details/<prod_key>/bulk_image_upload', views.bulk_image_upload, name="bulk_image_upload"),
    
   # export game data
   path("export_game_data/", views.export_game_data, name="export_game_data"),
   
   # edits
   path('show-game-details/<prod_key>/upload_game_logo', views.upload_game_logo, name="upload_game_logo"),
   
   # Delete Game
   path('delete_game/<product_key>', views.delete_game, name="delete_game"),

   # Contact
   path('contact_game_view/', views.contact_game_view, name="contact_game_view"),
   path('contact_game_view/insert_game_contact', views.insert_game_vcontact, name="insert_game_contact"),
   
   #histogram
   # path('dashboard/histogram-price', views.price_histogram, name='price_histogram'),
   path('dashboard/histogram-price/', views.price_histogram, name='price_histogram'),

   
]