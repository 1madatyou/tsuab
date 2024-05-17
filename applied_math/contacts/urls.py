from django.urls import path

from .views import Contacts


urlpatterns = [
    path('', Contacts.as_view(), name='contacts'),
]