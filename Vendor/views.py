from django.shortcuts import get_object_or_404, render, redirect, HttpResponse
from django.urls import reverse
from django.shortcuts import render
from django.contrib import messages
import random
import string
from .models import *
from Administrator.models import *

# Create your views here.

#call main page
def index_vendor(request):
    return render(request,'index-vendor.html')

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
    pass