from django.urls import path

from .views import Contacts, EmployeesList, EmployeesDetail


urlpatterns = [
    path("", Contacts.as_view(), name="contacts"),
    path(
        "employees",
        EmployeesList.as_view(),
        name="employees-list",
    ),
    path(
        "employees/<int:pk>",
        EmployeesDetail.as_view(),
        name="employees-detail",
    ),
]
