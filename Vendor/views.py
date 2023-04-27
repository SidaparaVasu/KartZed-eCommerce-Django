import os, random, string, imghdr
from django.conf import settings
from PIL import Image
from django.shortcuts import get_object_or_404, render, redirect, HttpResponse
from django.urls import reverse
from django.shortcuts import render
from django.contrib import messages
from django.core.exceptions import ValidationError


from .models import Games, Vendor_Contact
from .forms import GamesForm
from Authapp.models import Vendors
from Administrator.models import *
from Administrator.views import get_os_by_category

# Create your views here.

#call main page
def index_vendor(request):
    if request.session.get('is_vendor_authenticated', False):
        return render(request,'index-vendor.html')
    else:
        return render(request, 'vendor-login.html')    

def render_vendor_register_page(request):
    return render(request, 'vendor-register.html')

def render_vendor_login_page(request):
    return render(request, 'vendor-login.html')

def show_games_page(request):
    if request.session.get('is_vendor_authenticated', False):
        vendor = Vendors.objects.get(vendor_unique_keyid = request.session['vendor_unique_keyid'])
        games = Games.objects.filter(vendor_reference = vendor.vendor_id).order_by('game_name')
        return render(request, 'Games/show-games.html', context = {'Games':games})
    else:
        return render(request, 'vendor-login.html') 

""" Check Image is in Image formt or not? """
def is_image(file):
    """
    Returns True if the selected file is an image, False otherwise.
    """
    image_formats = ('.jpg', '.jpeg', '.png', '.gif')
    file_extension = os.path.splitext(file.name)[1]
    if file_extension.lower() in image_formats:
        return True
    elif imghdr.what(file) in image_formats:
        return True
    else:
        return False

# Games CRUD
def add_game_page(request):
    if request.session.get('is_vendor_authenticated', False):
        categorized_os_version_data = get_os_by_category(request)
        context = {
            'platforms'                   : Platform.objects.order_by('platform_name'),
            'game_features'               : GameFeatures.objects.order_by('game_feature_name'),
            'game_modes'                  : GameModes.objects.order_by('game_mode_name'),
            'game_categories'             : GameCategory.objects.order_by('game_category_name'),
            'operatingsys'                : OperatingSystems.objects.all(),
            # 'operatingsysversion'       : OSVersions.objects.all(),
            'categorized_version_data'    : categorized_os_version_data,
            'processors'                  : Processors.objects.all(),
            'vc'                          : VideoCards.objects.all(),
            'vcv'                         : VCVersions.objects.all(),
        }
        # return HttpResponse(context['categorized_version_data'])
        return render(request,'Games/game.html', context)
    else:
        return render(request, 'vendor-login.html') 

def generate_product_key(request):
    """
    Generates a random product key of the specified length.
    """
    length=16
    letters_and_digits = string.ascii_uppercase + string.ascii_lowercase + string.digits
    key = ''.join(random.choice(letters_and_digits) for i in range(length))
    return key

def check_image_format(file):
    try:
        # open the file and check if it's an image
        image = Image.open(file)
        if image.format.lower() not in ['jpeg', 'jpg', 'png', 'gif']:
            raise ValidationError('File must be in image format.')
        else:
            return image
    except IOError:
        raise ValidationError('File is not an image.')

def insert_game(request):
    if request.method == 'POST': 
        vendor_unique_id = request.POST.get('vendor_unique_keyid')
        vendors = Vendors.objects.get(vendor_unique_keyid = vendor_unique_id)
    
        try:
            features = list(request.POST.getlist('game_features'))
            modes = list(request.POST.getlist('game_modes'))
            categoires = list(request.POST.getlist('game_categories'))
            platforms = list(request.POST.getlist('platform_names'))
            languages = list(request.POST.getlist('game_languages'))
            
            game = Games()
            game.product_key           = generate_product_key(request)
            game.game_logo             = request.FILES['game_logo']
            game.vendor_reference      = vendors 
            game.game_name             = request.POST.get('game_name')
            game.game_description      = request.POST.get('game_description')
            game.game_developer        = request.POST.get('game_developer')
            game.game_publisher        = request.POST.get('game_publisher')
            game.game_release_date     = request.POST.get('game_release_date')
            game.avail_stock           = request.POST.get('avail_stock')
            game.game_price            = request.POST.get('game_price')
            game.discount              = request.POST.get('discount')
            game.game_storage          = request.POST.get('game_storage')
            game.game_ram              = request.POST.get('game_ram')
            game.game_features         = features
            game.game_modes            = modes
            game.game_categories       = categoires
            game.platform_names        = platforms
            game.game_languages        = languages
            game.save()
            messages.success(request, "Game Added successfully!")
            return redirect(reverse(add_game_page))
        except Exception as e:
            return HttpResponse(e)
            messages.success(request, "Game Insertion failed!")
            return redirect(reverse(add_game_page))
    messages.error(request, "Bad request of form! Try again later!")
    return redirect(reverse(add_game_page))


def contact_game_view(request):
    return render(request, 'contact.html')

def insert_game_vcontact(request):
    #return HttpResponse("yo")
    if request.method == 'POST':
        contact_name    = request.POST.get('contact_name')
        contact_email   = request.POST.get('contact_email')
        contact_message = request.POST.get('contact_message')
        try:
            Vendor_Contact.objects.create( 
                contact_name    = contact_name,   
                contact_email   = contact_email,  
                contact_message = contact_message,
            )
        except Exception as e:
            return HttpResponse(e)
                
    return render(request, 'contact.html')