from django.shortcuts import render
from .models import Games

def pie_chart(request):
    labels = []
    data = []

    queryset = Games.objects.order_by('-avail_stock')[:5]
    for game in queryset:
        labels.append(game.game_name)
        data.append(game.avail_stock)

    # return render(request, 'pie_chart.html', {
    #     'labels': labels,
    #     'data': data,
    # })

    return labels,data