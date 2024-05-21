from django.urls import path

from .views import DiplomaThesesList


urlpatterns = [
    path('', DiplomaThesesList.as_view(), name="theses_list")
]