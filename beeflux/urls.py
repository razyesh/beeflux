from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('post.urls')),
    path('core/', include('core.urls')),
    path('company/', include('account.urls')),
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('',include('entrance.urls')),
    path('', include('base.urls')),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
=======
]+static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

>>>>>>> f90f46c4a9b20a8bfc5821af3bdede8a12af3ad1
