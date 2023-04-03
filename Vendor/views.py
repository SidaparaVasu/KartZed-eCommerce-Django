from django.shortcuts import render, redirect, HttpResponse
from django.shortcuts import render
from .forms import registervendor


# Create your views here.
def indexVendor(req):
    return render(req,'indexVendor.html')

def addproduct(request):
        return render(request, 'addproduct.html')

def registervendor(request):
    if request.method == 'POST':
        form = registervendor(request.POST)
        if form.is_valid():
            if form.save():
                return HttpResponse("done")
            
            # return render('register')
    else:
        form = registervendor()
    return render(request, 'register.html', {'form': form})

