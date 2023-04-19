from django.shortcuts import render, redirect, HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from os import *

from Email.views import Email
#from .models import Users # Users model


# Create your views here.
def indexPage(request):
    return render(request, 'index.html')

def render_login_page(request):
    return render(request, 'login.html')

def render_account_page(request):
    return render(request, 'user_account.html')


""" Authentication """



""" Update Profile of User """
def update_user_profile(request):
    if request.method == 'GET':
        first_name = request.GET.get('first_name')
        last_name = request.GET.get('last_name')
        email_id = request.GET.get('email_id')
        phone_number = request.GET.get('phone_number')
        gender = request.GET.get('gender')
        
        user_data = Users.objects.get(email_id=email_id)
        
        if gender == "" or gender == None:
            gender = user_data.gender
        
        
        try:
            user_data.first_name = first_name
            user_data.last_name = last_name
            user_data.email_id = email_id
            user_data.phone_number = phone_number
            user_data.gender = gender
            user_data.save()
            
            request.session['first_name'] = user_data.first_name
            request.session['last_name'] = user_data.last_name
            request.session['gender'] = user_data.gender
            request.session['email_id'] = user_data.email_id
            request.session['phone_number'] = user_data.phone_number
            request.session['gender'] = user_data.gender
            
            messages.success(request, "Profile Updated!")
            return redirect(reverse('render_account_page'))
        except Exception as e:
            messages.success(request, "Try again! an error occured")
            return redirect(reverse('render_account_page'))
        
        return HttpResponse(email_id)
    pass