from django.shortcuts import get_object_or_404, render, redirect, HttpResponse
from django.shortcuts import render
from .forms import registervendor
from Vendor.models import Vendor


# Create your views here.

#call main page
def indexVendor(req):
    return render(req,'indexVendor.html')

#add product information
def addproduct(request):
    form = registervendor(request.POST,request.FILES)
    if form.is_valid():

        form.save()
        return redirect("/vendor")
    
    return render(request, 'addproduct.html')

#view product information
def viewproduct(request):
    context = {}
    
    context["prod"] = Vendor.objects.all()
    return render(request, "viewproduct.html", context)

#edit product information
def editproduct(request,id):
    context = {}
    obj = get_object_or_404(Vendor, id=id)
    form = registervendor(request.POST or None, instance=obj)

    if form.is_valid():
        # return HttpResponse(form)
        form.save()

        return redirect("/vendor")

    context['form'] = form
    return render(request, "editproduct.html",context)

#delete product information
def deleteproduct(request,id):
	context={}
	obj = get_object_or_404(Vendor, id=id)
	if request.method == "GET":
		obj.delete()
		return redirect("/vendor")
	return render(request, "viewproduct.html", context)
