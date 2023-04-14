from django.shortcuts import get_object_or_404, render, redirect, HttpResponse
from django.urls import reverse
from django.shortcuts import render
from django.contrib import messages
import random
import string
from .forms import registervendor
from Vendor.models import Vendor


# Create your views here.

#call main page
def index_vendor(request):
    return render(request,'index-vendor.html')

#view product information
def view_product(request):
    context = {}
    
    context["product"] = Vendor.objects.all()
    return render(request, "product/product.html", context)

def generate_product_key():
    """Generate a random product key of specified length."""
    length = 16
    characters = string.ascii_uppercase + string.digits
    product_key = ''.join(random.choice(characters) for i in range(length))
    return product_key

#add product information
def add_product(request):
    form = registervendor(request.POST,request.FILES)
    if form.is_valid():
        try:
            form.product_key = generate_product_key()
            form.save()
            messages.success(request, "Product Added successfully!")
            return redirect(reverse(view_product))
        except Exception as e:
            messages.success(request, "Product Insertion failed!")
            return redirect(reverse(view_product))
    return render(request, 'product/product.html')

# update function of product
def update_product(request, id):
    product = Vendor.objects.get(product_key=id) 
    # return HttpResponse(product.product_key)      
    return render(request, "product/update-product.html",{'product' : product})

#edit product information
def edit_product(request,product_key):
    data = Vendor.objects.get(product_key=product_key)

    try:
        data.prodname  = request.POST.get('prodname')
        data.proddescription  = request.POST.get('proddescription')
        data.prodprice  = request.POST.get('prodprice')
        data.discount  = request.POST.get('discount')
        data.prodimage  = request.POST.get('prodimage')      
        data.save()
        messages.success(request, "Product Updated successfully!")
        return redirect(reverse(view_product))
    except Exception as e:
        messages.success(request, "Product Updation failed!")
        return redirect(reverse(view_product))

#delete product information
def delete_product(request,product_key):
    obj = get_object_or_404(Vendor, product_key=product_key)
    if request.method == "GET":
        try:
            obj.delete()
            messages.success(request, "Product Deleted Successfully!")
            return redirect(reverse(view_product))
        except Exception as e:
            messages.error(request, "Product Deletion Failed!")
            return redirect(reverse(view_product))
    return redirect(reverse(view_product))
