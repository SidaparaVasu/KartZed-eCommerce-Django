from django.shortcuts import render, redirect, HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from os import *
from Vendor.models import *
from .models import *
from Email.views import Email

# Create your views here.
def indexPage(request):
    if 'cust_email' not in request.session:
        context = {
            'games' : Games.objects.all()
        }
        return render(request, 'index.html', context)
    else:
        user = request.session['cust_email']
        user_id = Customers.objects.get(cust_email = user)
    
        context = {
            'games' : Games.objects.all(),
            'cart_count' : Cart.objects.filter(cust_id = user_id).count()
            }
        return render(request, 'index.html',context)

def render_account_page(request):
    if request.session.get('is_authenticated', False):
        return render(request, 'user_account.html')
    else:
        return redirect(reverse('render_customer_login_page'))

def view_cart(request):
    if request.session.get('is_authenticated', False):
        return render(request, 'Cart/viewcart.html')
    else:
        return redirect(reverse('render_customer_login_page'))

def add_to_cart(request,id):
    
    if request.session.get('is_authenticated', False):
        game = Games.objects.get(product_key = id)
        user = request.session['cust_email']
        user_id = Customers.objects.get(cust_email = user)
        #return HttpResponse(user_id.cust_id)
        try:
            cart = Cart.objects.create(
                cust_id = user_id,
                is_paid = False
            )
            cartitem = CartItems.objects.create(cart = cart, game = game)
            
        except Exception as e:
            return HttpResponse(e)
        return redirect(reverse(indexPage))
    else:
        return redirect(reverse('render_customer_login_page'))