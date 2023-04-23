import os, random, string, imghdr
from PIL import Image
from django.shortcuts import get_object_or_404, render, redirect, HttpResponse
from django.urls import reverse
from django.shortcuts import render
from django.contrib import messages
from django.core.exceptions import ValidationError
from .models import Games
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
        games = Games.objects.filter(vendor_reference = request.session['vendor_unique_keyid'])
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
    if request.method == 'GET': 
        vendor_unique_id = request.GET.get('vendor_unique_keyid')
        vendors = Vendors.objects.get(vendor_unique_keyid = vendor_unique_id)
        
        game_logo_path = request.GET.get('game_logo')
        game_logo_path = "product_img/game_logos/"+str(game_logo_path)
        # return HttpResponse(game_logo_path)
        try:
            Games.objects.create(
                product_key           = generate_product_key(request),
                game_logo             = game_logo_path,
                vendor_company_name   = vendors, 
                game_name             = request.GET.get('game_name'),
                game_description      = request.GET.get('game_description'),
                game_images           = request.FILES.getlist('game_images'),
                game_developer        = request.GET.get('game_developer'),
                game_publisher        = request.GET.get('game_publisher'),
                game_release_date     = request.GET.get('game_release_date'),
                avail_stock           = request.GET.get('avail_stock'),
                game_price            = request.GET.get('game_price'),
                discount              = request.GET.get('discount'),
                game_storage          = request.GET.get('game_storage'),
                game_ram              = request.GET.get('game_ram'),
                game_features         = ','.join(request.GET.getlist('game_features')),
                game_modes            = ','.join(request.GET.getlist('game_modes')),
                game_categories       = ','.join(request.GET.getlist('game_categories')),
                platform_names        = ','.join(request.GET.getlist('platform_names')),
                game_languages        = ','.join(request.GET.getlist('game_languages')),
            )
            messages.success(request, "Game Added successfully!")
            return redirect(reverse(add_game_page))
        except Exception as e:
            messages.success(request, "Game Insertion failed!")
            return redirect(reverse(add_game_page))
    messages.error(request, "Bad request of form! Try again later!")
    return redirect(reverse(add_game_page))