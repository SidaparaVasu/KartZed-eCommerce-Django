import os, io, random, string, imghdr, csv
from django.conf import settings
from PIL import Image
from django.shortcuts import get_object_or_404, render, redirect, HttpResponse
from django.urls import reverse
from django.shortcuts import render
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.db import IntegrityError
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
        vendor = Vendors.objects.get(vendor_unique_keyid = request.session['vendor_unique_keyid'])
        games = Games.objects.filter(vendor_reference = vendor.vendor_id).order_by('game_name')
        return render(request, 'Games/show-games.html', context = {'Games':games})
    else:
        return render(request, 'vendor-login.html') 

""" Check Image is in Image format or not? """
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
        return render(request,'Games/add-game.html', context)
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
        vendor_ins = Vendors.objects.get(vendor_unique_keyid = vendor_unique_id)
    
        try:
            game = Games()
            game.product_key           = generate_product_key(request)
            game.game_logo             = request.FILES['game_logo']
            game.vendor_reference      = vendor_ins  
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
            game.game_features         = list(request.POST.getlist('game_features'))
            game.game_modes            = list(request.POST.getlist('game_modes'))
            game.game_categories       = list(request.POST.getlist('game_categories'))
            game.platform_names        = list(request.POST.getlist('platform_names'))
            game.game_languages        = list(request.POST.getlist('game_languages'))
            game.save()
            messages.success(request, "Game Added successfully!")
            return redirect(reverse(add_game_page))
        except Exception as e:
            messages.success(request, "Game Insertion failed!")
            return redirect(reverse(add_game_page))
    messages.error(request, "Bad request of form! Try again later!")
    return redirect(reverse(add_game_page))


""" Insert Games using CSV upload """
def upload_csv(request):
    if request.method == 'POST' and request.FILES['file']:
        csv_file = request.FILES['file']
        if not csv_file.name.endswith('.csv'):
            messages.error(request, 'File is not a CSV')
            return redirect('upload_csv')

        data_set = csv_file.read().decode('UTF-8')
        io_string = io.StringIO(data_set)
        next(io_string)
        vendor_unique_id = request.POST.get('vendor_unique_keyid')
        vendor_ins = Vendors.objects.get(vendor_unique_keyid = vendor_unique_id)
        for row in csv.reader(io_string, delimiter=',', quotechar='"'):
            # Check for any primary key or unique constraints
            try:
                obj = Games.objects.create(
                    product_key           = generate_product_key(request),
                    game_logo             = row[0],
                    vendor_reference      = vendor_ins,
                    game_name             = row[1],
                    game_description      = row[2],
                    game_developer        = row[3],
                    game_publisher        = row[4],
                    game_release_date     = row[5],
                    avail_stock           = row[6],
                    game_price            = row[7],
                    discount              = row[8],
                    game_storage          = row[9],
                    game_ram              = row[10],
                    game_features         = row[11],
                    game_modes            = row[12],
                    game_categories       = row[13],
                    platform_names        = row[14],
                    game_languages        = row[15]
                )
            except ValidationError as e:
                # Handle any validation errors
                messages.error(request, f"Error creating object: {str(e)}")
                return redirect(reverse(add_game_page))
            except IntegrityError as e:
                # Handle any duplicate primary key or unique constraint errors
                messages.error(request, f"Error creating object: {str(e)}")
                return redirect(reverse(add_game_page))
        messages.success(request, 'CSV file uploaded successfully')
        return redirect(reverse(show_games_page))

    return redirect(reverse(show_games_page))
