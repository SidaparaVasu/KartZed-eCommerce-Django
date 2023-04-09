from django.shortcuts import render,redirect,HttpResponse, get_object_or_404
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
    
    p = Paginator(category, 3)
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
            messages.success(request, "Category Added successfully!")
            return redirect(reverse(viewCategory))
        except Exception as e:
            messages.error(request, "Category Insertion failed!")
            return redirect(reverse(viewCategory))

def updateCategory(request, id):
    context = Category.objects.get(category_id=id)
    return render(request, "category/update_category.html",{'context' : context})

# Update Function Of Category
def editCategory(request, id):
    data = Category.objects.get(category_id=id)
    edited_category  = request.POST.get('category')
    try:
        data.category = edited_category
        if data.save():
            messages.success(request, "Category Updated successfully!")
            return redirect(reverse(viewCategory))
        else:
            messages.success(request, "Category Updation failed!")
            return redirect(reverse(viewCategory))
    except Exception as e:
        messages.success(request, "Category Updation failed!")
        return redirect(reverse(viewCategory))  
    
def deleteCategory(request, id):
    
    obj = get_object_or_404(Category,category_id=id)
    # return HttpResponse(obj)
    if request.method == "GET":
        if obj.delete():
            messages.success(request,"Category deleted successfully!")
            return redirect(reverse(viewCategory))
        else:
            messages.error(request,"Category couldn't delete!")
    return redirect(reverse(viewCategory))