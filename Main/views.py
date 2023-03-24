from django.shortcuts import render, redirect, HttpResponse
from os import *
from pathlib import Path

# Create your views here.
def indexPage(request):
    return render(request, 'index.html')