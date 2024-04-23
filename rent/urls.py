
from django.contrib import admin
from django.urls import path, include
from django.conf  import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('escalate_rent/', include('vehicles.urls')),
    path('escalate_rent/', include('users.urls')),
    path('escalate_rent/', include('api.urls'))
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)