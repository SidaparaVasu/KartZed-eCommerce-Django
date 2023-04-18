from django import forms
from Administrator.models import *


class PlatformForm(forms.ModelForm):
    class Meta:
        model  = Platform
        fields = ('platform_id', 'platform_name')
        
class GameFeaturesForm(forms.ModelForm):
    class Meta:
        model  = GameFeatures
        fields = ('game_feature_id','game_feature_name')
        
class GameModesForm(forms.ModelForm):
    class Meta:
        model  = GameModes
        fields = ('game_mode_id','game_mode_name')
        
class GameCategoryForm(forms.ModelForm):
    class Meta:
        model  = GameCategory
        fields = ('game_category_id','game_category_name')