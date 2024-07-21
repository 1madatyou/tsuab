from django.urls import path

from .views import Support, SupportDone


urlpatterns = [
    path("", Support.as_view(), name="support"),
    path("done", SupportDone.as_view(), name="support_done"),
]
