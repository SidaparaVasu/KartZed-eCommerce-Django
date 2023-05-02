from django.shortcuts import get_object_or_404, render, redirect, HttpResponse
from django.template.loader import render_to_string
from django.http import HttpResponseRedirect, JsonResponse
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
from django.conf import settings
import stripe
stripe.api_key = settings.STRIPE_SECRET_KEY


# Create your views here.
def indexPage(request):
    if request.session.get('is_authenticated', False):
        cust_unique_keyid = request.session['cust_unique_keyid']
        user_id = Customers.objects.get(cust_unique_keyid = cust_unique_keyid)
    
        context = {
            'games' : Games.objects.all(),
            'cart_count' : Cart.objects.filter(cust_id = user_id).count()
        }
        
        return render(request, 'index.html',context)
    else:
        context = {
            'games' : Games.objects.all()
        }
        return render(request, 'index.html', context)

def view_browse(request):
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
        categoryID = request.GET.get('category')
        if categoryID:
            games=Games.object.filter(game_modes = categoryID)
        else:
            games = Games.objects.all()
        context = {
            # 'imp' : imp,
            'games' : games,
            'cart_count' : Cart.objects.filter(cust_id = user_id).count(),
            'modes' : GameModes.objects.all()
        }
        
        return render(request, 'Browse/browse.html',context)
    else:
        categoryID = request.GET.get('category')
        print(categoryID)
        if categoryID:
            print(categoryID)

            x = GameModes.objects.filter(game_mode_id = categoryID)
            games=Games.object.filter(game_modes = categoryID)
        else:
            games = Games.objects.all()
        context = {
            'games' : games,
            'modes' : GameModes.objects.all()
        }
        return render(request, 'Browse/browse.html', context)

def render_account_page(request):
    if request.session.get('is_authenticated', False):
        user_data = Customers.objects.get(cust_unique_keyid = request.session['cust_unique_keyid'])
        user_points = UserBalancePoints.objects.get(customer=user_data)
        return render(request, 'user_account.html', context={'user_data': user_data,'user_points':user_points})
    else:
        return redirect(reverse('render_customer_login_page'))

def view_cart(request):
    if request.session.get('is_authenticated', False):
        user = Customers.objects.get(cust_unique_keyid = request.session['cust_unique_keyid'])
        cart_data = Cart.objects.filter(cust_id = user.cust_id)
        # return HttpResponse(cart_data)
        
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
        return render(request, 'Cart/cart.html', context={'Games': GameList})
    else:
        return redirect(reverse('render_customer_login_page'))

""" View details Start """
def view_game_detail(request, product_key):
    product = Games.objects.get(product_key = product_key)
    images = GameImages.objects.filter(game_id = product.gid)
    cartItemForCurrentGame = CartItems.objects.filter(game_id = product.gid) 
    if cartItemForCurrentGame.count() < 1:
        return render(request, 'product-page.html', context = {
            'Game' : product, 'Images':images, 'isAdded': False
        })
    else:
        current_user = Customers.objects.get(cust_unique_keyid = request.session['cust_unique_keyid'])
        user_id = current_user.cust_id
        cart_data = Cart.objects.filter(cust_id = user_id)
        item_list = []
        for c_data in cart_data:
            item_list.append(CartItems.objects.filter(cart_id = c_data.cart_id))
        index = 0
        for item in item_list:
            if item[index].game_id == product.gid:              
                return render(request, 'product-page.html', context = {
                    'Game' : product, 'Images':images, 'isAdded': True
                })
    return render(request, 'product-page.html', context = {
        'Game' : product, 'Images':images, 'isAdded': False
    })
    
""" View details End """

def add_to_cart(request,product_key):
    if request.session.get('is_authenticated', False):
        game = Games.objects.get(product_key = product_key)
        url = reverse(view_game_detail, args=[product_key])
        
        user = request.session['cust_unique_keyid']
        user_id = Customers.objects.get(cust_unique_keyid = user)
        try:
            cart = Cart.objects.create(
                cust_id = user_id,
                is_paid = False
            )
            cartitem = CartItems.objects.create(cart = cart, game = game)
            messages.success(request, "Game Added successfully!")
            return redirect(url)    
        except Exception as e:
            return HttpResponse(e)
    else:
        return redirect(reverse('render_customer_login_page'))

def delete_cart_item(request,id):
    obj = get_object_or_404(CartItems,game=id)
    cartitem = CartItems.objects.get(game=id)
    #return HttpResponse(cartitem.cart.cart_id)
    obj1 = get_object_or_404(Cart,cart_id=cartitem.cart.cart_id)
    if request.method == "GET":
        obj1.delete()
        return redirect(reverse(view_cart))
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
    if request.method == 'GET':
        contact_name    = request.GET.get('contact_name')
        contact_email   = request.GET.get('contact_email')
        contact_message = request.GET.get('contact_message')
        try:
            Contact.objects.create( 
                contact_name    = contact_name,   
                contact_email   = contact_email,  
                contact_message = contact_message,
            ) 
            messages.error(request,"Thanks for your contacting us!")
            return redirect(reverse(indexPage))
        except Exception as e:
            messages.error(request,"Message Coudn't sent! Try again!")
            return render(request, 'Contact/contact.html')
                
    return render(request, 'Contact/contact.html')


""" Contact Us End """

""" user points balance """
def buy_points(request):
    context = {
        'balance_points' : Plan.objects.all()
    }
    return render(request,'Balance/buy_points.html',context)

def check_payment(request, id):
    # checkout = Plan.objects.get(plan_id=id)
    context = {
        'checkout' : Plan.objects.get(plan_id= id),
        'key' : settings.STRIPE_PUBLISHABLE_KEY,
    }
    return render(request,'Balance/checkout.html',context)


def charge(request,id):
    if request.method=='POST':
        plan = Plan.objects.get(plan_id=id)
        charge = stripe.PaymentIntent.create(
            amount=plan.amount,
            currency='inr',
            payment_method_types=['card'],
            description='Payment for items in cart',
        )
        cust_cur_key = request.session['cust_unique_keyid']
        cust_cur_id = Customers.objects.get(cust_unique_keyid = cust_cur_key)
        points_bal = UserBalancePoints.objects.get(customer = cust_cur_id.cust_id)
        new_bal = points_bal.points + plan.points
        points_bal.points = new_bal
        points_bal.save() 
        return redirect(reverse('render_account_page'))

""" user points balance """


""" Search :: Browse Start"""

# def view_browse(request):
#     return render(request,'Browse/browse.html')

def view_search(request):
    query = request.GET.get('search')
    results = Games.objects.filter(Q(game_name__icontains=query))
    context = {'query': query, 'results': results}
    return render(request,'Browse/browse.html',context)

""" Search End """


def view_orders(request):
    if request.session.get('is_authenticated', False):
        user_obj = Customers.objects.get(cust_unique_keyid = request.session['cust_unique_keyid'])
        order_obj = Orders.objects.get(user_id = user_obj.cust_id)
        order_items_obj = OrderItems.objects.filter(order_id = order_obj.oid)
        return render(request, 'view-orders.html')
    else:
        return redirect(reverse('render_customer_login_page'))

def generate_order_id():
    """
    Generates a random order id of the specified length.
    """
    length=12
    key = ''.join([str(random.randint(0, 9)) for _ in range(length)])
    return int(key)

# """ purchase"""
def view_order_summary(request):
    user_data = Customers.objects.get(cust_unique_keyid = request.session['cust_unique_keyid'])
    balance_obj = UserBalancePoints.objects.get(customer_id = user_data)
    user_balance_points = balance_obj.points

    total_qty = int(request.POST.get('total_qty'))
    total_points = int(request.POST.get('total_points'))
    
    if user_balance_points < total_points:
        messages.error(request, "Insufficient Balance! Buy More Points to Purchase")
        return redirect(reverse(buy_points))
    else:
        total_game_in_cart = request.POST.get('total_game_in_cart')
        
        games = {}
        
        for counter in range(1, int(total_game_in_cart)+1):
            games[counter] = {
                "product_key":request.POST.get(f'prod_{counter}'),
                "points":request.POST.get(f'points_{counter}'),
                "qty":request.POST.get(f'quantity_{counter}')
            }
        
        # Store Ordered Data in 'Orders' Collection
        order_id = generate_order_id()
        
        save_order = Orders.objects.create(
            order_id = order_id,
            user = user_data
        )
        save_order.save()
        
        # Getting Data from 'Orders' Collection
        order_obj = Orders.objects.get(order_id = order_id)
        
        flag = False
        
        for counter in range(1, int(total_game_in_cart)+1):
            game_ins = Games.objects.get(product_key = games[counter]['product_key'])
            try:
                save_order_items = OrderItems.objects.create(
                    order = order_obj,
                    game = game_ins,
                    quantity = games[counter]['qty'],
                    points = games[counter]['points']
                )
                save_order_items.save()
                flag = True
            except Exception as e:
                flag = False
        
        if flag:
            messages.success(request, "Order Placed Successfully!")
            balance_obj.points -= total_points
            balance_obj.save()
            
            # removing cart items after purchasing
            cart_obj = Cart.objects.filter(cust_id_id = user_data.cust_id)
            # return HttpResponse(cart_obj[0].cart_id)
            cnt = 0
            for c in cart_obj:
                cart_items_obj = CartItems.objects.filter(cart_id = c.cart_id)
                cart_items_obj.delete()
            cart_obj.delete()
        
            return redirect(reverse(view_orders))
        else:
            messages.error(request, "Failed to Place Order, Please try again later!")
            return redirect(reverse(view_cart))
    return render(request,'Order/place_order.html')

# """ end"""