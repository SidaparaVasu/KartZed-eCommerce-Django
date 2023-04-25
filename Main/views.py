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
    if request.session.get('is_authenticated', False):
        cust_unique_keyid = request.session['cust_unique_keyid']
        user_id = Customers.objects.get(cust_unique_keyid = cust_unique_keyid)
        chk = Cart.objects.filter(cust_id = user_id).count()
        imp = []
        if chk > 0:
            chk1 = CartItems.objects.all()   
            c_items_id = []         
            for data1 in chk1:
                c_items_id.append(data1.game.gid)
            print(c_items_id)

            chk2 = Games.objects.all()
            for data2 in c_items_id:
                #print(data2)
                c_g_items = Games.objects.filter(gid = data2)
                for data3 in c_g_items:
                    imp.append(data3.gid)
                    #print(imp)
            #return HttpResponse()
                
        else :
            pass    
        context = {
            'imp' : imp,
            'games' : Games.objects.all(),
            'cart_count' : Cart.objects.filter(cust_id = user_id).count()
        }
        
        return render(request, 'index.html',context)
    else:
        context = {
            'games' : Games.objects.all()
        }
        return render(request, 'index.html', context)

def render_account_page(request):
    if request.session.get('is_authenticated', False):
        user_data = Customers.objects.get(cust_unique_keyid = request.session['cust_unique_keyid'])
        return render(request, 'user_account.html', context={'user_data': user_data})
    else:
        return redirect(reverse('render_customer_login_page'))

def view_cart(request):
    if request.session.get('is_authenticated', False):
        user = Customers.objects.get(cust_unique_keyid = request.session['cust_unique_keyid'])
        cart_data = Cart.objects.filter(cust_id = user.cust_id)
        cartIDs = []
        for data in cart_data:
            cartIDs.append(data.cart_id)
            # print(data.cart_id)
        
        cartItemsList = []
        for id in cartIDs:
            cart_items = CartItems.objects.filter(cart_id = id)
            # return HttpResponse(cart_items)
            for citem in cart_items:
                cartItemsList.append(citem.game_id)
        
        print(len(cartItemsList))
        GameList = []
        for c_item_id in cartItemsList:
            games = Games.objects.filter(gid = c_item_id)
            for game in games:
                GameList.append(game)
        print(GameList)
        # return HttpResponse("hello")
        return render(request, 'Cart/cart.html', context={'Games': GameList})
        """ net puru  """
    else:
        return redirect(reverse('render_customer_login_page'))

def add_to_cart(request,id):
    # return HttpResponse(id)
    if request.session.get('is_authenticated', False):
        game = Games.objects.get(product_key = id)
        # chk = CartItems.objects.filter(game = game.gid)
        # if len(chk) > 0:
        #     is_added = True
        #     return redirect(reverse(indexPage),context = {'is_added':is_added}) 
        # else :
        user = request.session['cust_unique_keyid']
        user_id = Customers.objects.get(cust_unique_keyid = user)
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
        