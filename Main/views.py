from django.shortcuts import render, redirect, HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from os import *

from Email.views import Email


# Create your views here.
def indexPage(request):
    return render(request, 'index.html')

def render_account_page(request):
    return render(request, 'user_account.html')
