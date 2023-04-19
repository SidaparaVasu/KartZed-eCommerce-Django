from django.shortcuts import render, HttpResponse
from django.conf import settings
from django.core.mail import send_mail
import random
from Authapp.models import Customers # Users model

# Create your views here.
class Email():
    
    # Generate Login OTP
    def generate_otp(self):
        """Generate a 6-digit OTP"""
        return random.randint(100000, 999999)
       
    def send_login_otp(self, recipient_list):
          
        email = recipient_list[0]
        otp = self.generate_otp()
        
        # return HttpResponse(email)      
        try:
            """ Updating OTP value with new generated OTP """            
            Customers.objects.filter(cust_email=email).update(otp=str(otp))
            
            subject = "Login in KartZed"
            message = f"Your OTP for authentication is: {otp}"
            email_from = settings.EMAIL_HOST_USER
            
            if send_mail(subject, message, email_from, recipient_list):
                return f"OTP has been successfully sent on {email}."
            else:
                return f"An error occurred while sending the OTP on {email}. Please check your email address and try again later!"
        except Customers.DoesNotExist:
            return f"No user found with email {email}."