from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('motive/', include([
        path('', include('MOTIVE_project.common.urls')),
        path('forum/', include('MOTIVE_project.forum.urls')),
        path('profile/', include('MOTIVE_project.profiles.urls')),
    ])),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
