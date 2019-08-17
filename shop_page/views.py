from django.shortcuts import render

from .models import Goods

def post_goods(request):
    goods = Goods.objects.all()
    return render(request, 'shop_page/shop_page.html', {'goods':goods})
