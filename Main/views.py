from django.shortcuts import render, redirect, HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from os import *
from Vendor.models import *

from Email.views import Email


# Create your views here.
def indexPage(request):
    games = Games.objects.all()
    return render(request, 'index.html',context = {'games':games})

def render_account_page(request):
    return render(request, 'user_account.html')

def view_cart(request):
    return render(request, 'Cart/viewcart.html')

def add_to_cart(request,id):
    game = Games.objects.get(product_key = id)