from django.conf.urls import url
from django.views.generic import ListView, DetailView
from shop_page.models import Goods

urlpatterns = [
    url(r'^$', ListView.as_view(queryset=Goods.objects.all().order_by("-date")[:20], template_name="shop_page/shop_page.html")),  
]
