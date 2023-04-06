from django.shortcuts import render, redirect, HttpResponse
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
        
        if len(input_otp) < 6:
            er_context = {'result' : True, 'email': email, 'errormsg': "Invalid OTP! must be 6 digits"}
            return render(request, 'login.html', er_context)
        
        if int(user_data.otp) == int(input_otp):
            return redirect(reverse('indexPage'))
        else:
            er_context = {'result' : True, 'email': email, 'errormsg': "OTP doesn't match! New OTP sent"}
            return render(request, 'login.html', er_context)
        
        