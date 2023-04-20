from django import forms
from .models import *

class GamesForm(forms.ModelForm):
    class Meta:
        model = Games
        fields = ['product_key','game_developer','game_name','game_publisher','game_desc','platform_name','game_feature','game_modes','game_category','os_name','os_version','processors_name','vc_name','vc_version','game_ram','game_languages','game_regions','game_price','avail_stock','discount',]