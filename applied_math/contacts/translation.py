from modeltranslation.translator import register, TranslationOptions

from .models import Employee, EmployeeContact


@register(Employee)
class EmployeeTranslationOptions(TranslationOptions):
    fields = ["position", "surname", "name", "patronymic"]


@register(EmployeeContact)
class EmployeeContactTranslationOptions(TranslationOptions):
    fields = ["title"]
