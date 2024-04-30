from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include


handler404 = 'core.views.handler404'


urlpatterns = [
    path('admin/', admin.site.urls),

    path('home/', include('home.urls')),
    path('news/', include('news.urls')),
    
    path('', include('users.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


