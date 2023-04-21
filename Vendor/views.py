from django.shortcuts import get_object_or_404, render, redirect, HttpResponse
from django.urls import reverse
from django.shortcuts import render
from django.contrib import messages
import random
import string
from .models import Games
from Administrator.models import *

# Create your views here.

#call main page
def index_vendor(request):
    return render(request,'index-vendor.html')

def render_vendor_register_page(request):
    return render(request, 'vendor-register.html')

def render_vendor_login_page(request):
    return render(request, 'vendor-login.html')

# Games CRUD
def view_game(request):
    context = {
        'platform'         : Platform.objects.all(),
        'game_feature'    : GameFeatures.objects.all(),
        'game_modes'       : GameModes.objects.all(),
        'game_category'    : GameCategory.objects.all(),
        'os'               : OperatingSystems.objects.all(),
        'osv'              : OSVersions.objects.all(),
        'processors'       : Processors.objects.all(),
        'vc'               : VideoCards.objects.all(),
        'vcv'              : VCVersions.objects.all(),

    }
    return render(request,'Games/game.html',context)

def insert_game(request):
    if request.method == 'GET':
        game_name      = request.GET.get('game_name')
        game_developer = request.GET.get('game_developer')
        game_publisher = request.GET.get('game_publisher')
        game_desc      = request.GET.get('game_description')
        platform_name  = request.GET.get('platform_name')
        game_feature   = request.GET.get('game_feature')
        game_modes     = request.GET.get('game_mode')
        game_category  = request.GET.get('game_category')
        os_name        = request.GET.get('os_name')
        os_version     = request.GET.get('os_version')
        processors_name= request.GET.get('processors_name')
        vc_name        = request.GET.get('vc_name')
        vc_version     = request.GET.get('vc_version')
        game_price     = request.GET.get('game_price')
        avail_stock    = request.GET.get('avail_stock')
        discount       = request.GET.get('discount')
        #print(type(game_price))
        #return HttpResponse(game_price)
        
        platforms     = Platform.objects.get(platform_name = platform_name)
        gamefeatures  = GameFeatures.objects.get(game_feature_name=game_feature)
        gamemodes     = GameModes.objects.get(game_mode_name=game_modes)
        gamecategory  = GameCategory.objects.get(game_category_name=game_category)
        osname        = OperatingSystems.objects.get(os_name=os_name)
        osversion     = OSVersions.objects.get(version=os_version)
        processorsname= Processors.objects.get(processor_name=processors_name)
        vcname        = VideoCards.objects.get(vc_name=vc_name)
        vcversion     = VCVersions.objects.get(vc_version_name=vc_version)

        try:
            Games.objects.create( 
                game_developer  =  game_developer,
                game_name       =  game_name,
                game_publisher  =  game_publisher,
                game_description=  game_desc,
                platform_name   =  platforms,
                game_feature    =  gamefeatures,
                game_modes      =  gamemodes,
                game_category   =  gamecategory,
                os_name         =  osname,
                os_version      =  osversion,
                processors_name =  processorsname,
                vc_name         =  vcname,
                vc_version      =  vcversion,
                game_ram        =  "",
                game_languages  =  "",
                game_regions    =  "",
                game_price      =  game_price,
                avail_stock     =  avail_stock,
                discount        =  discount,
             )
            messages.success(request, "Game Added successfully!")
            return redirect(reverse(view_game))
        except Exception as e:
            #messages.error(request, "")
            #return redirect(reverse(view_game))
            return HttpResponse(e)
    messages.error(request, "Game Insertion failed!")
    return redirect(reverse(view_game))