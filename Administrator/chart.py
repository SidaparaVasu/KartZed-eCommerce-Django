from django.shortcuts import render
from Authapp.models import *
from Vendor.models import *

def games_per_vendor_pie_chart(request):
    labels = []
    data = []
    data_len = []
    queryset1 = Vendors.objects.all()
    queryset2 = Games.objects.all()
    for vendor in queryset1:
        for game in queryset2:
            if game.vendor_reference_id == vendor.vendor_id:
                data.append(game.game_name)
        labels.append(vendor.company_name)
        data_len.append(len(data))
        data = [] 

    return data_len,labels