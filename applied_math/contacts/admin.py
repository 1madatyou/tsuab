from django.http import HttpResponseRedirect
from django.contrib import admin

from .models import Employee, EmployeeContact


class EmployeeContactInline(admin.TabularInline):
    model = EmployeeContact


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    fields = ['surname', 'name', 'patronymic', 'position', 'image']
    inlines = [
        EmployeeContactInline
    ]
    change_form_template = 'contacts/employee_change_form.html'

    def response_change(self, request, obj):
        if "_set-main" in request.POST:
            try:
                main_employee = Employee.objects.get(is_main=True)
                main_employee.is_main = False
                main_employee.save()
            except Employee.DoesNotExist:
                pass

            obj.is_main = True
            obj.save()
            self.message_user(request, "Сотрудник назначен главным")
            return HttpResponseRedirect(".")
        return super().response_change(request, obj)




    