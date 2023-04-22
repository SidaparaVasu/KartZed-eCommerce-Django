import os, random, string, imghdr
from django.shortcuts import get_object_or_404, render, redirect, HttpResponse
from django.urls import reverse
from django.shortcuts import render
from django.contrib import messages
from .models import Games
from Administrator.models import *
from Administrator.views import get_os_by_category

# Create your views here.

#call main page
def index_vendor(request):
    return render(request,'index-vendor.html')

def render_vendor_register_page(request):
    return render(request, 'vendor-register.html')

def render_vendor_login_page(request):
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
def view_game(request):
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
    return render(request,'Games/game.html',context)

def generate_product_key(request):
    """
    Generates a random product key of the specified length.
    """
    length=16
    letters_and_digits = string.ascii_uppercase + string.ascii_lowercase + string.digits
    key = ''.join(random.choice(letters_and_digits) for i in range(length))
    return key

def insert_game(request):
    if request.method == 'GET':
        prod_key              = generate_product_key(request)
        game_logo             = request.GET.get('game_logo')
        game_name             = request.GET.get('game_name')
        game_desc             = request.GET.get('game_description')
        game_developer        = request.GET.get('game_developer')
        game_publisher        = request.GET.get('game_publisher')
        game_release_date     = request.GET.get('game_release_date')
        avail_stock           = request.GET.get('avail_stock')
        game_price            = request.GET.get('game_price')
        discount              = request.GET.get('discount')
        game_storage          = request.GET.get('game_storage')
        game_ram              = request.GET.get('game_ram')
        game_feature          = ','.join(request.GET.getlist('game_feature'))
        game_modes            = ','.join(request.GET.getlist('game_modes'))
        game_category         = ','.join(request.GET.getlist('game_category'))
        platform_name         = request.GET.get('platform_name')
        # os_name               = request.GET.get('os_name')
        # os_version            = request.GET.get('os_version')
        # processors_name       = request.GET.get('processors_name')
        # vc_name               = request.GET.get('vc_name')
        # vc_version            = request.GET.get('vc_version')
        
        # gamefeatures  = GameFeatures.objects.get(game_feature_name=game_feature)
        # gamemodes     = GameModes.objects.get(game_mode_name=game_modes)
        # gamecategory  = GameCategory.objects.get(game_category_name=game_category)
        platforms     = Platform.objects.get(platform_name = platform_name)
        # osname        = OperatingSystems.objects.get(os_name=os_name)
        # osversion     = OSVersions.objects.get(version=os_version)
        # processorsname= Processors.objects.get(processor_name=processors_name)
        # vcname        = VideoCards.objects.get(vc_name=vc_name)
        # vcversion     = VCVersions.objects.get(vc_version_name=vc_version)

        try:
            Games.objects.create(
                product_key           = prod_key, 
                game_name             = game_name,
                game_description      = game_desc,
                game_developer        = game_developer,
                game_publisher        = game_publisher,
                game_release_date     = game_release_date,
                avail_stock           = avail_stock,
                game_price            = game_price,
                discount              = discount,
                game_storage          = game_storage,
                game_ram              = game_ram,
                game_feature          = game_feature,
                game_modes            = game_modes,
                game_category         = game_category,
                platform_name         = platforms
            )
            messages.success(request, "Game Added successfully!")
            return redirect(reverse(view_game))
        except Exception as e:
            #messages.error(request, "")
            #return redirect(reverse(view_game))
            return HttpResponse(e)
    messages.error(request, "Game Insertion failed!")
    return redirect(reverse(view_game))