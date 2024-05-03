from django.contrib import admin
from django.urls import path

from .views import Home, Support


urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('support', Support.as_view(), name='support'),
]
