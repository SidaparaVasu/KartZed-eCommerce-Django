from django import forms
from .models import *

class GamesForm(forms.ModelForm):
    class Meta:
        model = Games
        fields = [
            'product_key',
            'vendor_company_name',
            'game_logo',
            'game_name',
            'game_description',
            'game_developer',
            'game_publisher',
            'game_storage',
            'game_ram',
            'game_languages',
            'game_release_date',
            'game_price',
            'avail_stock',
            'discount',
            'game_images',
            'game_features',
            'game_modes',
            'game_categories',
            'platform_names',
            'os_names',
            'os_versions',
            'processors_names',
            'vc_names',
            'vc_versions'
        ]