from django.shortcuts import render, redirect, HttpResponse
from django.shortcuts import render
from .forms import registervendor
from Vendor.models import Vendor


# Create your views here.
def indexVendor(req):
    return render(req,'indexVendor.html')

def addproduct(request):
        return render(request, 'addproduct.html')

def addproduct(request):
    # return HttpResponse("Success")
    if request.method == "POST":
        form = registervendor(request.POST)
        if form.is_valid():
            if form.save():
                return HttpResponse("done")
            
            # return render('register')
    else:
        form = registervendor()
        return render(request, 'indexVendor.html', {'form': form})

def login(request):
    if request.method == "POST":    
        form = registervendor(request.POST)
        un = request.POST.get("username")
        ps = request.POST.get("password")
        
        flag = 0
        data = Vendor.objects.all()
        for i in range(len(data)):
            if data[i].username == un and data[i].password == ps:
                
                return render(request,'home.html')
                #return HttpResponse("Success")
            else :
                flag = 0
        if flag == 0:
            return render(request,'login.html')
            #return HttpResponse("Failed")