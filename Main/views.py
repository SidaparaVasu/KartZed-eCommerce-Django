from django.shortcuts import render, redirect, HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from os import *

from Email.views import Email
from .models import Users # Users model

# Create your views here.
def indexPage(request):
    return render(request, 'index.html')

def render_login_page(request):
    return render(request, 'login.html')


""" Authentication """
# User Login
def userLogin(request):        
    
    if request.method == 'POST':
        
        email_obj = Email()
        email = request.POST.get('email')
    
        fetch_email = Users.objects.filter(email_id=str(email))
        
        if len(fetch_email) > 0:
            if email_obj.send_login_otp([email]):
                return render(request, 'login.html', {'result': True, 'email': email})
                return redirect(reverse('indexPage'), {'result': True, 'email': email})
        else:
            try: 
                Users.objects.create(
                    first_name = '',
                    last_name = '',
                    gender = '',
                    email_id = email,
                    phone_number = '',
                    is_phone_verified = False,
                    otp = None,
                    user_type = 'is_user'
                )
                email_obj.send_login_otp([email])
                return render(request, 'login.html', {'result': True, 'email': email})
                return redirect(reverse('indexPage'), {'result': True, 'email': email})
            except Exception as e:
                return HttpResponse(f"An Error Occured: Cannot create user {e}")
        
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
            
            request.session['first_name'] = user_data.first_name
            request.session['last_name'] = user_data.last_name
            request.session['gender'] = user_data.gender
            request.session['email_id'] = user_data.email_id
            request.session['phone_number'] = user_data.phone_number
            request.session['is_phone_verified'] = user_data.is_phone_verified
            request.session['user_type'] = user_data.user_type
            request.session['is_session'] = True
            
            return HttpResponseRedirect('/')
        else:
            er_context = {'result' : True, 'email': email, 'errormsg': "OTP doesn't match! New OTP sent"}
            return render(request, 'login.html', er_context)
        
def logoutHandle(request):
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
    # messages.success(request, "You are Logged out!")
    return redirect(reverse('indexPage'))