from django.shortcuts import render, redirect, HttpResponse
from .models import Users
from os import *
from pathlib import Path

# Create your views here.
def indexPage(request):
    return render(request, 'index.html')


# Authentication
def registerUser(request):
    
    if request.method == 'POST':
        mobile_no = request.POST.get('mobileno')
        return HttpResponse(mobile_no)
        
    return render(request, 'index.html')