from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns


from .views import home_redirect


handler404 = 'core.views.handler404'

admin.site.site_header = "Администрирование"
admin.site.index_title = "Кафедра прикладной математики"

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),


]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('home/', include('home.urls')),
    path('support/', include('support.urls')),
    path('news/', include('news.urls')),
    path('materials/', include('materials.urls')),
    path('contacts/', include('contacts.urls')),
    
    path('', home_redirect),
    path('', include('users.urls')),
)





if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


