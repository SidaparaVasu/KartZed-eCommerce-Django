import random, string
from django.shortcuts import render,redirect,HttpResponse, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.hashers import make_password, check_password
from django.urls import reverse
from django.contrib import messages
from .models import Admins, Customers, Vendors

from Email.views import Email
from Administrator.views import index_admin
from Main.views import indexPage, render_account_page

# Create your views here.
def render_admin_login_page(request):
    return render(request, 'admin-login.html')

def render_customer_login_page(request):
    return render(request, 'customer-login.html')


"""  ADMIN LOGIN  """
def set_default_admin(request):
    form = Admins(
        admin_name = 'administrator',
        admin_role = 'super_admin',
        admin_email = 'admin@gmail.com',
        admin_password = make_password('admin@123'),
        admin_image = ''
    )
    
def admin_login(request):
    if request.method == "POST":    
        email = request.POST.get("admin_email")
        password = request.POST.get("admin_password")

        row_counter = Admins.objects.all().count()
        # return HttpResponse(row_counter)
        if row_counter == 0:
            form = Admins(
                admin_name = 'administrator',
                admin_role = 'super_admin',
                admin_email = 'admin@gmail.com',
                admin_password = make_password('admin@123'),
                admin_image = ''
            )
            form.save()
        else:
            flag = 0
            try:
                admin_data = Admins.objects.all()
                # return HttpResponse(admin_data)
                for i in range(len(admin_data)):
                    if admin_data[i].admin_email == email:
                        
                        is_password_match = check_password(password, admin_data[i].admin_password)
                        
                        if is_password_match == True:
                            return redirect(reverse('index_admin'))
                        else:
                            messages.error(request, "Password is incorrect!")
                            return redirect(reverse('render_admin_login_page'))
                    else:
                        flag = 1
                if flag == 1:
                    messages.error(request, "Invalid Credentials, try again!")
                    return redirect(reverse('render_admin_login_page'))
            except Exception as e:
                messages.error(request, "An error occured, try again later!")
                return redirect(reverse('render_admin_login_page'))
    return redirect(reverse('render_admin_login_page'))


def admin_logout_handle(request):
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
    return redirect(reverse('auth_admin'))                        

""" ADMIN LOGIN ENDS """

""" CUSTOMER LOGIN """
def customer_login(request):        
    
    if request.method == 'POST':
        
        email_obj = Email()
        email = request.POST.get('email')
    
        fetch_email = Customers.objects.filter(cust_email=str(email))
        # return HttpResponse(len(fetch_email))
        if len(fetch_email) > 0:
            if email_obj.send_login_otp([email]):
                return render(request, 'customer-login.html', {'result': True, 'email': email})
        else:
            # return HttpResponse(email)
            try: 
                Customers.objects.create(
                    cust_first_name = '',
                    cust_last_name = '',
                    cust_gender = '',
                    cust_email = email,
                    cust_phone_number = '',
                    is_phone_verified = False,
                    otp = 'null',
                    cust_country = '',
                    cust_state = '',
                    cust_city = '',
                    cust_address = ''
                )
                
                email_obj.send_login_otp([email])
                return render(request, 'customer-login.html', {'result': True, 'email': email})
            except Exception as e:
                messages.success(request, "An Error Occured: try login again")
                # return render(request, 'customer-login.html')
                # return HttpResponse(f"An Error Occured: Cannot create user {e}")
        
    return render(request, 'customer-login.html')

def verify_otp(request):
    
    if request.method == 'POST':
        
        input_otp, email = request.POST.get('otp-input'), request.POST.get('email')
        
        user_data = Customers.objects.get(cust_email=email)
        # return HttpResponse(user_data.email_id)
        
        if len(input_otp) < 6:
            er_context = {'result' : True, 'email': email, 'errormsg': "Invalid OTP! must be 6 digits"}
            return render(request, 'customer-login.html', er_context)
        
        if int(user_data.otp) == int(input_otp):
            return True, user_data, email
        
def customer_login_handle(request):
    verified, user_data, email = verify_otp(request)
    if verified:
        Customers.objects.filter(cust_email=email).update(otp='null')
        # Storing Customers data into session
        request.session['cust_first_name'] = user_data.cust_first_name
        request.session['cust_last_name'] = user_data.cust_last_name
        request.session['cust_gender'] = user_data.cust_gender
        request.session['cust_email'] = user_data.cust_email
        request.session['cust_phone_number'] = user_data.cust_phone_number
        request.session['is_phone_verified'] = user_data.is_phone_verified
        request.session['cust_country'] = user_data.cust_country
        request.session['cust_state'] = user_data.cust_state
        request.session['cust_city'] = user_data.cust_city
        request.session['cust_address'] = user_data.cust_address
        request.session['is_session'] = True
        
        messages.success(request, "You are Logged in successfully!")
        return HttpResponseRedirect('/')
    else:
        er_context = {'result' : True, 'email': user_data.email_id, 'errormsg': "OTP doesn't match! New OTP sent"}
        return render(request, 'customer-login.html', er_context)
    
def customer_logout_handle(request):
    try:
        del request.session['cust_first_name']
        del request.session['cust_last_name']
        del request.session['cust_gender']
        del request.session['cust_email']
        del request.session['cust_phone_number']
        del request.session['is_phone_verified']
        del request.session['cust_country']
        del request.session['cust_state']
        del request.session['cust_city']
        del request.session['cust_address']
        del request.session['is_session']
    except KeyError:
        pass
    messages.success(request, "You are Logged out!")
    return redirect(reverse('indexPage'))
""" CUSTOMER LOGIN ENDS """

""" UPDATE CUSTOMER PROFILE """
def update_customer_profile(request):
    if request.method == 'GET':
        first_name = request.GET.get('cust_first_name')
        last_name = request.GET.get('cust_last_name')
        email_id = request.GET.get('cust_email')
        phone_number = request.GET.get('cust_phone_number')
        gender = request.GET.get('cust_gender')
        
        user_data = Customers.objects.get(cust_email=email_id)
        
        if gender == "" or gender == None:
            gender = user_data.cust_gender
        
        try:
            user_data.cust_first_name = first_name
            user_data.cust_last_name = last_name
            user_data.cust_email = email_id
            user_data.cust_phone_number = phone_number
            user_data.cust_gender = gender
            user_data.save()
            
            request.session['cust_first_name'] = user_data.cust_first_name
            request.session['cust_last_name'] = user_data.cust_last_name
            request.session['cust_gender'] = user_data.cust_gender
            request.session['cust_email'] = user_data.cust_email
            request.session['cust_phone_number'] = user_data.cust_phone_number
            request.session['is_phone_verified'] = user_data.is_phone_verified
            request.session['cust_country'] = user_data.cust_country
            request.session['cust_state'] = user_data.cust_state
            request.session['cust_city'] = user_data.cust_city
            request.session['cust_address'] = user_data.cust_address
            request.session['is_session'] = True
            
            messages.success(request, "Profile Updated!")
            return redirect(reverse('render_account_page'))
        except Exception as e:
            messages.success(request, "Try again! an error occured")
            return redirect(reverse('render_account_page'))
        
        return HttpResponse(email_id)
    pass
""" UPDATE CUSTOMER PROFILE """