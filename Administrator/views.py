from django.shortcuts import render

# Create your views here.
def indexAdmin(req):
    return render(req,'indexAdmin.html')