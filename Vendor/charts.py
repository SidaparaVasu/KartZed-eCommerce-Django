from django.http import JsonResponse
from django.shortcuts import render
from .models import Games
from Authapp.models import *

def pie_chart(request):
    vendor_data = Vendors.objects.get(vendor_unique_keyid = request.session['vendor_unique_keyid'])
    games = Games.objects.filter(vendor_reference_id = vendor_data.vendor_id)
    g_name_list = []
    g_availstock = []

    queryset = games.order_by('-avail_stock')[:5]
    for game in queryset:
        g_name_list.append(game.game_name)
        g_availstock.append(game.avail_stock)

    # return render(request, 'pie_chart.html', {
    #     'g_name_list': g_name_list,
    #     'g_availstock': g_availstock,
    # })

    return g_name_list,g_availstock

def price_histogram(request):
    vendor_data = Vendors.objects.get(vendor_unique_keyid = request.session['vendor_unique_keyid'])
    # return vendor_data
    games = Games.objects.filter(vendor_reference_id = vendor_data.vendor_id)

    data = {
        'labels': [g.game_name for g in games],  # X-axis labels
        'data': [p.game_price for p in games],  # Y-axis data
    }

    return JsonResponse(data)
