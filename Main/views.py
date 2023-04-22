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
    user = request.session['cust_email']
    user_id = Customers.objects.get(cust_email = user)
    #cart_count : Cart.objects.get(cust_id = user_id).count()
    
    context = {
        'games' : Games.objects.all(),
        'cart_count' : Cart.objects.filter(cust_id = user_id).count()
        }
    return render(request, 'index.html',context)

def render_account_page(request):
    return render(request, 'user_account.html')

def view_cart(request):
    return render(request, 'Cart/viewcart.html')

def add_to_cart(request,id):
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