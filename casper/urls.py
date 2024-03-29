
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
  

urlpatterns = [
    path('', include('main_page.urls')),
    path('shop/', include('shop_page.urls')),
    path('blog/', include('blog_page.urls')),
    path("delivery/", include('delivery_page.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
