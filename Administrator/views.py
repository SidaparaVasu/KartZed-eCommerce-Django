from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from Administrator.forms import CategoryForm

# Create your views here.
def indexAdmin(req):
    return render(req,'indexAdmin.html')


# CCATEGORY :: CRUD
def Category(req):                              
    return render(req,'Category.html')           # calls category page

def addCategory(req):
    return render(req,'addCategory.html')        # calls addcategory page

# insertion of category
def insertCategory(request):
    if request.method == 'POST':
        
        category  = request.POST.get('category')
        # cat_image_path = request.POST.get('cat_image_path')
        form = CategoryForm(request.POST or None, request.FILES)  
        if len(request.FILES) != 0:
            form.image = request.FILES['cat_image_path']
        return HttpResponse(form.image)    

#SUB-CATEGORY :: CRUD
