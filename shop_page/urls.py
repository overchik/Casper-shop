from django.conf.urls import url
from django.views.generic import ListView, DetailView
from shop_page.models import Goods
from . import views

urlpatterns = [
    url(r'^$', views.post_goods, name='shop_page_url'),  
]
