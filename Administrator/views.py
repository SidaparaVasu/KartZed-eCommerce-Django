from django.shortcuts import render,redirect,HttpResponse, get_object_or_404
from django.urls import reverse
from django.core.paginator import Paginator
from django.contrib import messages
from Administrator.forms import PlatformForm
from Administrator.forms import SubCategoryForm

from Main.models import Users
from .models import Platform
from .models import SubCategory


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


""" 
    Platform CRUD 
"""
def view_platform(request):  
    platform = Platform.objects.all()
    
    p = Paginator(platform, 3)
    page_number = request.GET.get('page')
    
    try:
        page_obj = p.get_page(page_number)
    except Paginator.PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = p.page(1)
    except Paginator.EmptyPage:
        # if page is empty then return last page
        page_obj = p.page(p.num_pages)                   
    return render(request,'platform/platform.html', context={"platform":page_obj}) # calls platform page

# insertion of platform
def insert_platform(request):
    if request.method == 'POST':
        
        platform  = request.POST.get('platform')
        
        # cat_image_path = request.POST.get('cat_image_path')
        form = PlatformForm(request.POST or None, request.FILES)  
        
        try:
            Platform.objects.create(
                platform = platform,
            )
            messages.success(request, "platform Added successfully!")
            return redirect(reverse(view_platform))
        except Exception as e:
            messages.error(request, "platform Insertion failed!")
            return redirect(reverse(view_platform))

# Update Function Of platform
def update_platform(request, id):
    context = Platform.objects.get(platform_id=id)
    return render(request, "platform/update-platform.html",{'context' : context})

def edit_platform(request, id):
    data = Platform.objects.get(platform_id=id)
    edited_platform  = request.POST.get('platform')
    try:
        data.platform = edited_platform
        data.save()
        messages.success(request, "platform Updated successfully!")
        return redirect(reverse(view_platform))
    except Exception as e:
        messages.success(request, "platform Updation failed!")
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
""" 
    platform CRUD End
"""

""" 
    Sub Category CRUD 
"""
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

# insertion of subcategory
def insert_subcategory(request):
    if request.method == 'POST':
        subCategory  = request.POST.get('subCategory')
        imagepath = ""
        category = request.POST.get('category')
        # cat_image_path = request.POST.get('cat_image_path')
        form = SubCategoryForm(request.POST or None, request.FILES)  
        if len(request.FILES) != 0:
            form.image = request.FILES['sub_cat_image_path']
            imagepath = form.image
        # return HttpResponse(category) 

        try:
            SubCategory.objects.create(
                subCategory = subCategory,
                imagepath = imagepath,
                category = Category.objects.get(category_id=category)
            )
            messages.success(request, "Sub-Category Added successfully!")
            return redirect(reverse(view_subcategory))
        except Exception as e:
            messages.error(request, "Sub-Category Insertion failed!")
            return redirect(reverse(view_subcategory))
            return HttpResponse(e)

# update function of subcategory
def update_subcategory(request, id):
    category = Category.objects.all()        
    context = SubCategory.objects.get(subCategory_id=id)
    return render(request, "subcategory/update-subcategory.html",{'context' : context, 'category':category})

def edit_subcategory(request, id):
    data = SubCategory.objects.get(category_id=id)
    edited_subcategory  = request.POST.get('subCategory')
    try:
        data.subCategory = edited_subcategory
        data.save()
        messages.success(request, "Sub-Category Updated successfully!")
        return redirect(reverse(view_subcategory))
    except Exception as e:
        messages.success(request, "Sub-Category Updation failed!")
        return redirect(reverse(view_subcategory))  

# delete subcategory
def delete_subcategory(request, id):
    obj = get_object_or_404(SubCategory,subCategory_id=id)
    # return HttpResponse(obj)
    if request.method == "GET":
        if obj.delete():
            messages.success(request,"Sub-Category deleted successfully!")
            return redirect(reverse(view_subcategory))
        else:
            messages.error(request,"Sub-Category couldn't delete!")
    return redirect(reverse(view_subcategory))

""" 
    Sub Category CRUD End
"""