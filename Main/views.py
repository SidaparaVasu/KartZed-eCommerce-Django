from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse
from os import *

from Email.views import Email
from .models import Users # Users model

# Create your views here.
def indexPage(request):
    # result = request.GET.get('result')
    # email = request.GET.get('email')
    
    # context = {'result': result, 'email': email}
    # # return redirect('', context)
    return render(request, 'index.html')

def esehi(request):
    return render(request, 'esehi.html')

""" Authentication """
# User Login
def userLogin(request):        
    
    if request.method == 'POST':
        
        email_obj = Email()
        email = request.POST.get('email')
    
        fetch_email = Users.objects.filter(email_id=str(email))
        
        if len(fetch_email) > 0:
            if email_obj.send_login_otp([email]):
                return render(request, 'index.html', {'result': True, 'email': email})
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
                return render(request, 'index.html', {'result': True, 'email': email})
                return redirect(reverse('indexPage'), {'result': True, 'email': email})
            except Exception as e:
                return HttpResponse(f"An Error Occured: Cannot create user {e}")
        
    return render(request, 'index.html')


def verify_otp(request):
    
    if request.method == 'POST':
        
        input_otp, email = request.POST.get('otp-input'), request.POST.get('email')
        
        user_data = Users.objects.get(email_id=email)
        
        context = {'result' : False, 'email': email}
        
        if int(user_data.otp) == int(input_otp):
            return render(request, 'index.html', {'result': False, 'email': email})
            # url = f"{reverse('indexPage')}?result={context['result']}&email={context['email']}"
            # return redirect(url)
        else:
            return HttpResponse("OTP doesn't match")
        
        