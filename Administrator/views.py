from django.shortcuts import render,redirect,HttpResponse, get_object_or_404
from django.urls import reverse
from django.core.paginator import Paginator
from django.contrib import messages

from Main.models import Contact
from .models import Offer, Platform, GameFeatures, GameModes, GameCategory, OperatingSystems, OSVersions ,Plan
from .models import Processors, VideoCards, VCVersions
from Authapp.models import Customers

# Create your views here.
def index_admin(request):
    return render(request,'index-admin.html')

""" USER """
def view_customers(request):
    customers = Customers.objects.all()

    p = Paginator(customers, 10)
    page_number = request.GET.get('page')
    
    try:
        page_obj = p.get_page(page_number)
    except Paginator.PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = p.page(1)
    except Paginator.EmptyPage:
        # if page is empty then return last page
        page_obj = p.page(p.num_pages)
    return render(request,'customers/customers.html',context={'customers':page_obj})


""" Platform CRUD Start """
def view_platform(request):  
    platform = Platform.objects.all().order_by('platform_name')
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
    features = GameFeatures.objects.all().order_by('game_feature_name')
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
    modes = GameModes.objects.all().order_by('game_mode_name')
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
    game_category = GameCategory.objects.all().order_by('game_category_name')
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

def get_os_by_category(request):
    os_data = OperatingSystems.objects.all()
    versions_data = OSVersions.objects.all().select_related('os_name')
    # print(versions_data)
    
    categorized_version_data = {}
    for os in os_data:
        os_name = os.os_name
        versions_for_os = versions_data.filter(os_name_id = os.os_id)
        categorized_version_data[os_name] = [v['version'] for v in list(list(versions_for_os.values()))]
        
    return categorized_version_data
    # for key, value in categorized_version_data.items():
    #     print(key, " => ", value)
    # print(categorized_version_data)

def view_os(request):
    os_data = OperatingSystems.objects.all()
    categorized_version_data = get_os_by_category(request)

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
        
        # return HttpResponse(os_id)
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
""" Processors CRUD Start """

def view_processor(request):
    os_data = OperatingSystems.objects.all()
    processor = Processors.objects.all()
    return render(request,'Processors/processors.html',context ={
        'operating_system':os_data,
        'processor':processor
    })

def insert_processor(request):
    if request.method == 'GET':
        os_name  = request.GET.get('os_name')
        # return HttpResponse(os_name)
        os_data = OperatingSystems.objects.get(os_id=os_name)
        processor_name  = request.GET.get('processor_name')
        
        try:
            Processors.objects.create( 
                os_name = os_data,
                processor_name = processor_name 
            )
            messages.success(request, "Processor Added successfully!")
            return redirect(reverse(view_processor))
        except Exception as e:
            messages.error(request, "Processor is alreay exists /  insertion failed!")
            return redirect(reverse(view_processor))
    messages.error(request, "Processor Insertion failed!")
    return redirect(reverse(view_processor))

def delete_processor(request,id):
    obj = get_object_or_404(Processors,processor_id=id)
    
    if request.method == "GET":
        if obj.delete():
            messages.success(request,"Processor deleted successfully!")
            return redirect(reverse(view_processor))
        else:
            messages.error(request,"Processor couldn't delete!")
    return redirect(reverse(view_processor))

""" Processors CRUD End """

""" VideoCards CRUD Start """

def view_vc(request):
    vc_data = VideoCards.objects.all()
    versions_data = VCVersions.objects.all().select_related('vc_name')
    # print(versions_data)
    
    categorized_version_data = {}
    for vc in vc_data:
        vc_name = vc.vc_name
        versions_for_vc = versions_data.filter(vc_name_id = vc.vc_id)
        categorized_version_data[vc_name] = [v['vc_version_name'] for v in list(list(versions_for_vc.values()))]
        

    for key, value in categorized_version_data.items():
        print(key, " => ", value)
    print(categorized_version_data)

    return render(request,'VideoCards/videocards.html', context={'vc_data': vc_data, 'categorized_version_data': categorized_version_data})
    #return render(request,'VideoCards/videocards.html',context={'vc_data':vc_data})

def insert_vc(request):
    if request.method == 'GET':
        vc_name  = request.GET.get('vc_name')
        
        try:
            VideoCards.objects.create( vc_name = vc_name )
            messages.success(request, "Video Card Added successfully!")
            return redirect(reverse(view_vc))
        except Exception as e:
            messages.error(request, "Video Card is alreay exists /  insertion failed!")
            return redirect(reverse(view_vc))
    messages.error(request, "Video Card Insertion failed!")
    return redirect(reverse(view_vc))

def insert_vc_version(request):
    if request.method == 'GET':
        vc_id  = request.GET.get('vc_name')
        version_name  = request.GET.get('vc_version')
        
        vc_data = VideoCards.objects.get(vc_id = vc_id)
        # return HttpResponse(vc_data.vc_name)
        
        try:
            VCVersions.objects.create(
                vc_name = vc_data,
                vc_version_name = version_name
            )
            messages.success(request, "VC Version Added!")
            return redirect(reverse(view_vc))
        except Exception as e:
            messages.error(request, "An error occured! try again!")
            return redirect(reverse(view_vc))
            #return HttpResponse(e)
    return redirect(reverse(view_vc))

""" VideoCards CRUD End """

""" Offer CRUD Start """

def view_offer(request):

    offer = Offer.objects.all()
    return render(request,'offer/offer.html',context ={'offer':offer})

def insert_offer(request):
    if request.method == 'POST':
        offer_name  = request.POST.get('offer_name')
        offer_description  = request.POST.get('offer_description')
        offer_tc  = request.POST.get('offer_tc')
        
        try:
            Offer.objects.create( 
                offer_name = offer_name,
                offer_description = offer_description,
                offer_tc  = offer_tc 
                )
            messages.success(request, "Offer Added successfully!")
            return redirect(reverse(view_offer))
        except Exception as e:
            messages.error(request, "Offer is alreay exists /  insertion failed!")
            return redirect(reverse(view_offer))
    messages.error(request, "Processor Insertion failed!")
    return redirect(reverse(view_offer))

def delete_offer(request,id):
    obj = get_object_or_404(Offer,offer_id=id)
    
    if request.method == "GET":
        if obj.delete():
            messages.success(request,"Offer deleted successfully!")
            return redirect(reverse(view_offer))
        else:
            messages.error(request,"Offer couldn't delete!")
    return redirect(reverse(view_offer))

""" Offer CRUD End """


""" Contact Us Start """

def view_contact(request):

    contact = Contact.objects.all()
    return render(request,'contact/viewcontact.html',context ={'contact':contact})

def delete_contact(request,id):
    obj = get_object_or_404(Contact,contact_id=id)
    #return HttpResponse(obj)
    if request.method == "GET":
        if obj.delete():
            messages.success(request,"Offer deleted successfully!")
            return redirect(reverse(view_contact))
        else:
            messages.error(request,"Offer couldn't delete!")
            return redirect(reverse(view_contact))
    #return HttpResponse(obj)


""" Contact Us End """

""" Plan Start """

def view_plan(request):
    return render(request,'Plan/view_plan.html')

def insert_plan(request):
    if request.method == 'POST':
        points = request.POST.get('points')
        amount = request.POST.get('amount')
        
        try:
            Plan.objects.create( 
                points = points,
                amount = amount,
                )
            messages.success(request, "Plan Added successfully!")
            return redirect(reverse(view_plan))
        except Exception as e:
            messages.error(request, e)
            return redirect(reverse(view_plan))
    messages.error(request, "Plan Insertion failed!")
    return redirect(reverse(view_plan))

""" Plan End """
