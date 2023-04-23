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

class OperatingSystemsForm(forms.ModelForm):
    class Meta:
        model  = OperatingSystems
        fields = ('os_id','os_name')

class OSVersionForm(forms.ModelForm):
    class Meta:
        model  = OSVersions
        fields = ('version_id','os_name','version')

class ProcessorForm(forms.ModelForm):
    class Meta:
        model  = Processors
        fields = ('processor_id','processor_name')

class VideoCardsForm(forms.ModelForm):
    class Meta:
        model  = VideoCards
        fields = ('vc_id','vc_name')

class VCVersionsForm(forms.ModelForm):
    class Meta:
        model  = VCVersions
        fields = ('vc_version_id','vc_name','vc_version_name')

class OfferForm(forms.ModelForm):
    class Meta:
        model  = Offer 
        fields = ('offer_id', 'offer_name', 'offer_description', 'offer_tc')