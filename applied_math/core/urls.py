from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include


from .views import home_redirect


handler404 = 'core.views.handler404'


urlpatterns = [
    path('admin/', admin.site.urls),


    path('home/', include('home.urls')),
    path('news/', include('news.urls')),
    
    path('', home_redirect),
    path('', include('users.urls')),

]

admin.site.site_header = "Администрирование"
admin.site.index_title = "Кафедра прикладной математики"



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


