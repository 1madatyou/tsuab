from typing import Any
from django.views import generic

from .models import Employee


class Contacts(generic.TemplateView):
    template_name = "contacts/contacts.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)

        try:
            main_employee = Employee.objects.get(is_main=True)
        except Employee.DoesNotExist:
            main_employee = Employee.objects.last()

        context.update(
            {
                "main_employee": main_employee,
                "last_employees": Employee.objects.all()[:6],
            }
        )
        return context


class EmployeesList(generic.ListView):
    template_name = "contacts/employees_list.html"
    context_object_name = "employees"
    model = Employee


class EmployeesDetail(generic.DetailView):
    template_name = "contacts/employees_detail.html"
    context_object_name = "e"
    model = Employee
