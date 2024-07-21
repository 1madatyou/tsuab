from django.urls import path

from .views import DiplomaThesesList, ManualsList, EducationalMaterialList


urlpatterns = [
    path("theses/", DiplomaThesesList.as_view(), name="theses_list"),
    path("manuals/", ManualsList.as_view(), name="manuals_list"),
    path("library/", EducationalMaterialList.as_view(), name="materials_list"),
]
