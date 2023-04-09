from django.shortcuts import render,redirect,HttpResponse
from django.urls import reverse
from django.core.paginator import Paginator
from django.contrib import messages
from Administrator.forms import CategoryForm

from .models import Category

# Create your views here.
def indexAdmin(req):
    return render(req,'indexAdmin.html')


# CCATEGORY :: CRUD
def viewCategory(request):  
    category = Category.objects.all()
    
    p = Paginator(category, 1)
    page_number = request.GET.get('page')
    
    try:
        page_obj = p.get_page(page_number)
    except Paginator.PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = p.page(1)
    except Paginator.EmptyPage:
        # if page is empty then return last page
        page_obj = p.page(p.num_pages)
        
                                
    return render(request,'Category.html', context={"category":page_obj})           # calls category page

# insertion of category
def insertCategory(request):
    if request.method == 'POST':
        
        category  = request.POST.get('category')
        imagepath = ""
        # cat_image_path = request.POST.get('cat_image_path')
        form = CategoryForm(request.POST or None, request.FILES)  
        if len(request.FILES) != 0:
            form.image = request.FILES['cat_image_path']
            imagepath = form.image
            
        try:
            Category.objects.create(
                category = category,
                imagepath = imagepath
            )
            
            return redirect(reverse(viewCategory))
        except Exception as e:
            return HttpResponse(e)
        if form.save():
            return HttpResponse("Saved!")    
        else:
            return HttpResponse("Error!")    

#SUB-CATEGORY :: CRUD
