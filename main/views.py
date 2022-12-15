from django.shortcuts import get_object_or_404, render
from .models import ShopingList


def index(request):
    latest_list = ShopingList.objects.order_by('-pubDate')[:5]
    context = {
        'latest_list': latest_list,
    }
    return render(request, 'main/index.html', context)

def shopingList(request, listID):
    list = get_object_or_404(ShopingList, pk=listID)
    return render(request, 'main/viewList.html', {
        'list': list, 
        'listID':listID
    })
