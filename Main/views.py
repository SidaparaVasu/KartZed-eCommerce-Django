from django.shortcuts import get_object_or_404, render, redirect, HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.db.models import Q
from os import *
from Administrator.views import *
from Vendor.models import *
from Administrator.models import * 
from .models import *
from Email.views import Email
from .forms import *


# Create your views here.
def indexPage(request):
    if request.session.get('is_authenticated', False):
        cust_unique_keyid = request.session['cust_unique_keyid']
        user_id = Customers.objects.get(cust_unique_keyid = cust_unique_keyid)
        # chk = Cart.objects.filter(cust_id = user_id).count()
        # imp = []
        # if chk > 0:
        #     chk1 = CartItems.objects.all()   
        #     c_items_id = []         
        #     for data1 in chk1:
        #         c_items_id.append(data1.game.gid)
        #     print(c_items_id)

        #     chk2 = Games.objects.all()
        #     for data2 in c_items_id:
        #         #print(data2)
        #         c_g_items = Games.objects.filter(gid = data2)
        #         for data3 in c_g_items:
        #             imp.append(data3.gid)
        #             #print(imp)
            #return HttpResponse()
                
        # else :
        #     pass    
        context = {
            # 'imp' : imp,
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

def delete_cart_item(request,id):
    obj = get_object_or_404(CartItems,game=id)
    cartitem = CartItems.objects.get(game=id)
    #return HttpResponse(cartitem.cart.cart_id)
    obj1 = get_object_or_404(Cart,cart_id=cartitem.cart.cart_id)
    if request.method == "GET":
        if obj.delete():
            obj1.delete()
            messages.success(request,"Cart Item deleted successfully!")
            return redirect(reverse(view_cart))
        else:
            messages.error(request,"Cart Item couldn't delete!")
    return redirect(reverse(view_cart))

""" Offer CRUD Start """

def view_offer(request):

    offer = Offer.objects.all()
    return render(request,'offer/offer.html',context ={'offer':offer})

def insert_offer(request):
    if request.method == 'POST':
        offer_name  = request.POST.get('offer_name')
        offer_description  = request.POST.get('offer_description')
        offer_tc  = request.POST.get('offer_tc')
        
        try:
            Offer.objects.create( 
                offer_name = offer_name,
                offer_description = offer_description,
                offer_tc  = offer_tc 
                )
            messages.success(request, "Offer Added successfully!")
            return redirect(reverse(view_offer))
        except Exception as e:
            messages.error(request, "Offer is alreay exists /  insertion failed!")
            return redirect(reverse(view_offer))
    messages.error(request, "Processor Insertion failed!")
    return redirect(reverse(view_offer))

def delete_offer(request,id):
    obj = get_object_or_404(Offer,offer_id=id)
    
    if request.method == "GET":
        if obj.delete():
            messages.success(request,"Offer deleted successfully!")
            return redirect(reverse(view_offer))
        else:
            messages.error(request,"Offer couldn't delete!")
    return redirect(reverse(view_offer))

""" Offer CRUD End """


""" Contact Us Start """

def contact_view(request):
    return render(request, 'Contact/contact.html')

def insert_contact(request):
    #return HttpResponse("yo")
    if request.method == 'POST':
        contact_name    = request.POST.get('contact_name')
        contact_email   = request.POST.get('contact_email')
        contact_message = request.POST.get('contact_message')
        try:
            Contact.objects.create( 
                contact_name    = contact_name,   
                contact_email   = contact_email,  
                contact_message = contact_message,
            )
        except Exception as e:
            return HttpResponse(e)
                
    return render(request, 'Contact/contact.html')


""" Contact Us End """

""" View details Start """
def view_game_detail(request, product_key):
    product = Games.objects.get(product_key = product_key)
    #return HttpResponse(product.game_description)
    context = {
        'games' : product
        }

    return render(request, 'viewgame.html',context)

""" View details End """

""" user points balance """
def buy_points(request):
    context = {
        'balance' : Plan.objects.all()
    }
    return render(request,'Balance/buy_points.html',context)

def check_payment(request,id):
    
    return render(request,'Balance/buy_points.html')


""" user points balance """


""" Search :: Browse Start"""

def view_browse(request):
    return render(request,'Browse/browse.html')

def view_search(request):
    query = request.GET.get('search')
    results = Games.objects.filter(Q(game_name__icontains=query))
    context = {'query': query, 'results': results}
    return render(request,'Browse/browse.html',context)

""" Search End """