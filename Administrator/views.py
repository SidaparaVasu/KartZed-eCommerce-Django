from django.shortcuts import render,redirect,HttpResponse, get_object_or_404
from django.urls import reverse
from django.db.models import Count
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from .models import Platform, GameFeatures, GameModes, GameCategory, OperatingSystems, OSVersions
from Main.models import Users

# Create your views here.
def index_admin(request):
    return render(request,'index-admin.html')

def auth_admin(request):
    return render(request,'authentication-login.html')

def admin_login(request):
    if request.method == "POST":    
        form = Users(request.POST)
        email = request.POST.get("email_id")
        password = request.POST.get("password")

        encrypted_pass = make_password(password)
        row_counter = Users.objects.filter(user_type="is_admin").count()
        
        if row_counter == 0:
            form = Users(
                        first_name = "",
                        last_name = "",
                        gender = "",
                        email_id = "admin@gmail.com",
                        password = make_password('12345'),
                        phone_number = '',
                        is_phone_verified = "False",
                        otp = "null",
                        user_type = "is_admin"
            )
            form.save()
            messages.success(request, "please login again!")
            return redirect(reverse('auth_admin'))
        else:
            flag = 0
            try:
                admin_data = Users.objects.filter(user_type = "is_admin")
                
                for i in range(len(admin_data)):
                    if admin_data[i].email_id == email:
                        is_password_match = check_password(password, admin_data[i].password)
                        # return HttpResponse(is_password_match)
                        if is_password_match == True:
                            return redirect(reverse('index_admin'))
                        else:
                            messages.error(request, "Password is incorrect!")
                            return redirect(reverse('auth_admin'))
                    else:
                        flag = 1
                if flag == 1:
                    messages.error(request, "Invalid Credentials, try again!")
                    return redirect(reverse('auth_admin'))
            except Exception as e:
                messages.error(request, "An error occured, try again later!")
                return redirect(reverse('auth_admin'))
    return redirect(reverse('auth_admin'))


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

""" Operating System CRUD Starts """

def view_os(request):
    os_data = OperatingSystems.objects.all()
    versions_data = OSVersions.objects.all().select_related('os_name')
    # print(versions_data)
    
    categorized_version_data = {}
    for os in os_data:
        os_name = os.os_name
        versions_for_os = versions_data.filter(os_name_id = os.os_id)
        categorized_version_data[os_name] = [v['version'] for v in list(list(versions_for_os.values()))]
        

    for key, value in categorized_version_data.items():
        print(key, " => ", value)
    print(categorized_version_data)

    return render(request,'OperatingSystems/os.html', context={'operating_system': os_data, 'categorized_version_data': categorized_version_data})

def insert_os(request):
    if request.method == 'GET':
        os_name  = request.GET.get('os_name')
        
        try:
            OperatingSystems.objects.create( os_name = os_name )
            messages.success(request, "Operating System Added successfully!")
            return redirect(reverse(view_os))
        except Exception as e:
            messages.error(request, "Operating System is alreay exists /  insertion failed!")
            return redirect(reverse(view_os))
    messages.error(request, "Operating System Insertion failed!")
    return redirect(reverse(view_os))

def insert_os_version(request):
    if request.method == 'GET':
        os_id  = request.GET.get('os_name')
        os_version  = request.GET.get('version')
        
        os_data = OperatingSystems.objects.get(os_id = os_id)
        
        try:
            OSVersions.objects.create(
                os_name = os_data,
                version = os_version
            )
            messages.success(request, "Version Added!")
            return redirect(reverse(view_os))
        except Exception as e:
            messages.error(request, "An error occured! try again!")
            return redirect(reverse(view_os))
    return redirect(reverse(view_os))
""" Operating System CRUD End """
