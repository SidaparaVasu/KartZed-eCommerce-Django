from django.shortcuts import render,redirect,HttpResponse, get_object_or_404
from django.urls import reverse
from django.core.paginator import Paginator
from django.contrib import messages
import json
from .models import Platform, GameFeatures, GameModes, GameCategory
from Main.models import Users

# Create your views here.
def index_admin(request):
    return render(request,'index-admin.html')

def auth_admin(request):
    return render(request,'authentication-login.html')


def admin_logout_handle(request):
    try:
        del request.session['first_name']
        del request.session['last_name']
        del request.session['gender']
        del request.session['email_id']
        del request.session['phone_number']
        del request.session['is_phone_verified']
        del request.session['user_type']
        del request.session['is_session']
    except KeyError:
        pass
    messages.success(request, "You are Logged out!")
    return redirect(reverse('auth_admin'))


""" USER """
def view_users(request):
    email_id = Users.objects.all()

    p = Paginator(email_id, 3)
    page_number = request.GET.get('page')
    
    try:
        page_obj = p.get_page(page_number)
    except Paginator.PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = p.page(1)
    except Paginator.EmptyPage:
        # if page is empty then return last page
        page_obj = p.page(p.num_pages)
    return render(request,'users/users.html',context={'users':page_obj})


""" Platform CRUD Start """
def view_platform(request):  
    platform = Platform.objects.all()
    return render(request,'platform/platform.html', context={'platforms':platform})

# insertion of platform
def insert_platform(request):
    if request.method == 'GET':
        platform  = request.GET.get('platform_name')
        try:
            Platform.objects.create(
                platform_name = platform,
            )
            messages.success(request, "platform Added successfully!")
            return redirect(reverse(view_platform))
        except Exception as e:
            messages.error(request, "platform Insertion failed!")
            return redirect(reverse(view_platform)) 

# delete platform
def delete_platform(request, id):
    
    obj = get_object_or_404(Platform,platform_id=id)
    # return HttpResponse(obj)
    if request.method == "GET":
        if obj.delete():
            messages.success(request,"platform deleted successfully!")
            return redirect(reverse(view_platform))
        else:
            messages.error(request,"platform couldn't delete!")
    return redirect(reverse(view_platform))

"""  platform CRUD End """


""" Game Features CRUD Start """
def view_game_features(request):
    features = GameFeatures.objects.all()
    return render(request,'gameFeatures/game_features.html',context={'features':features})

def insert_game_feature(request):
    if request.method == 'GET':
        feature  = request.GET.get('game_feature_name')
        
        try:
            GameFeatures.objects.create( game_feature_name = feature )
            messages.success(request, "Game Feature Added successfully!")
            return redirect(reverse(view_game_features))
        except Exception as e:
            messages.error(request, "Game Feature is alreay exists / insertion failed!")
            return redirect(reverse(view_game_features))
    messages.error(request, "Game Feature Insertion failed!")
    return redirect(reverse(view_game_features))


def delete_game_feature(request, id):
    obj = get_object_or_404(GameFeatures,game_feature_id=id)
    
    if request.method == "GET":
        if obj.delete():
            messages.success(request,"Game Feature deleted successfully!")
            return redirect(reverse(view_game_features))
        else:
            messages.error(request,"Game Feature couldn't delete!")
    return redirect(reverse(view_game_features))

""" Game Features CRUD End """

""" Game Modes CRUD Start """
def view_game_modes(request):
    modes = GameModes.objects.all()
    return render(request,'gameModes/game_modes.html',context={'game_modes': modes})

def insert_game_mode(request):
    if request.method == 'GET':
        game_mode  = request.GET.get('game_mode_name')
        
        try:
            GameModes.objects.create( game_mode_name = game_mode )
            messages.success(request, "Game Mode Added successfully!")
            return redirect(reverse(view_game_modes))
        except Exception as e:
            messages.error(request, "Game Mode is alreay exists /  insertion failed!")
            return redirect(reverse(view_game_modes))
    messages.error(request, "Game Mode Insertion failed!")
    return redirect(reverse(view_game_modes))


def delete_game_mode(request, id):
    obj = get_object_or_404(GameModes,game_mode_id=id)
    
    if request.method == "GET":
        if obj.delete():
            messages.success(request,"Game Mode deleted successfully!")
            return redirect(reverse(view_game_modes))
        else:
            messages.error(request,"Game Mode couldn't delete!")
    return redirect(reverse(view_game_modes))

""" Game Modes CRUD End """

""" Game Category CRUD Start """
def view_game_category(request):
    game_category = GameCategory.objects.all()
    return render(request,'gameCategory/game_category.html',context={'game_category': game_category})

def insert_game_category(request):
    if request.method == 'GET':
        game_category  = request.GET.get('game_category_name')
        
        try:
            GameCategory.objects.create( game_category_name = game_category )
            messages.success(request, "Game Category Added successfully!")
            return redirect(reverse(view_game_category))
        except Exception as e:
            messages.error(request, "Game Category is alreay exists /  insertion failed!")
            return redirect(reverse(view_game_category))
    messages.error(request, "Game Category Insertion failed!")
    return redirect(reverse(view_game_category))

def delete_game_category(request, id):
    obj = get_object_or_404(GameCategory,game_category_id=id)
    
    if request.method == "GET":
        if obj.delete():
            messages.success(request,"Game Category deleted successfully!")
            return redirect(reverse(view_game_category))
        else:
            messages.error(request,"Game Category couldn't delete!")
    return redirect(reverse(view_game_category))
""" Game Category CRUD End """