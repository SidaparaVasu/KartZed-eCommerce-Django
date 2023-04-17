from django.shortcuts import render, redirect, HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from os import *

from Email.views import Email
from .models import Users # Users model

# Create your views here.
def indexPage(request):
    return render(request, 'index.html')

def render_login_page(request):
    return render(request, 'login.html')

def render_account_page(request):
    return render(request, 'user_account.html')


""" Authentication """
# User Login
def user_login(request):        
    
    if request.method == 'POST':
        
        email_obj = Email()
        email = request.POST.get('email')
    
        fetch_email = Users.objects.filter(email_id=str(email))
        # return HttpResponse(len(fetch_email))
        if len(fetch_email) > 0:
            if email_obj.send_login_otp([email]):
                return render(request, 'login.html', {'result': True, 'email': email})
        else:
            # return HttpResponse(email)
            try: 
                Users.objects.create(
                    first_name = '',
                    last_name = '',
                    gender = '',
                    email_id = email,
                    password = '',
                    phone_number = '',
                    is_phone_verified = False,
                    otp = None,
                    user_type = 'is_user'
                )
                
                email_obj.send_login_otp([email])
                return render(request, 'login.html', {'result': True, 'email': email})
            except Exception as e:
                messages.success(request, "An Error Occured: try login again")
                # return render(request, 'login.html')
                # return HttpResponse(f"An Error Occured: Cannot create user {e}")
        
    return render(request, 'login.html')


def verify_otp(request):
    
    if request.method == 'POST':
        
        input_otp, email = request.POST.get('otp-input'), request.POST.get('email')
        
        user_data = Users.objects.get(email_id=email)
        # return HttpResponse(user_data.email_id)
        
        if len(input_otp) < 6:
            er_context = {'result' : True, 'email': email, 'errormsg': "Invalid OTP! must be 6 digits"}
            return render(request, 'login.html', er_context)
        
        if int(user_data.otp) == int(input_otp):
            return True, user_data
        
def login_handle(request):
    verified, user_data = verify_otp(request)
    if verified:
        request.session['first_name'] = user_data.first_name
        request.session['last_name'] = user_data.last_name
        request.session['gender'] = user_data.gender
        request.session['email_id'] = user_data.email_id
        request.session['phone_number'] = user_data.phone_number
        request.session['is_phone_verified'] = user_data.is_phone_verified
        request.session['user_type'] = user_data.user_type
        request.session['is_session'] = True
        
        messages.success(request, "You are Logged in successfully!")
        return HttpResponseRedirect('/')
    else:
        er_context = {'result' : True, 'email': user_data.email_id, 'errormsg': "OTP doesn't match! New OTP sent"}
        return render(request, 'login.html', er_context)
        
def logout_handle(request):
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
    return redirect(reverse('indexPage'))



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