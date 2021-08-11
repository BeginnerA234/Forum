import debug_toolbar

from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .yasg import urlpatterns as yasg_urls

from backend import settings

urlpatterns = [
    path('__debug__/', include(debug_toolbar.urls)),
    path('admin/', admin.site.urls),

    path('', include('custom_user.urls')),
    path('api/', include('custom_user.api.urls')),
    path('api/forum/', include('forum.api.urls')),
]

urlpatterns += yasg_urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
