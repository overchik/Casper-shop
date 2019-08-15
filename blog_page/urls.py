from django.conf.urls import url
from django.views.generic import ListView, DetailView
from blog_page.models import Posts

urlpatterns = [
    url(r'^$', ListView.as_view(queryset=Posts.objects.all().order_by("-date")[:20], template_name="blog_page/blog_page.html")),  
]
