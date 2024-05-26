from django.urls import path

from .views import Home, History


urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('history', History.as_view(), name='history'),
]
