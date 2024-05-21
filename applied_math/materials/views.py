from django.views import generic

from .models import DiplomaThesis, Manual


class DiplomaThesesList(generic.ListView):
    """Представление списка дипломных работ"""
    model = DiplomaThesis
    context_object_name = 'theses'
    template_name = 'materials/theses_list.html'
    paginate_by = 6


class ManualsList(generic.ListView):
    """Представление списка методических указаний"""
    model = Manual
    context_object_name = 'manuals'
    template_name = 'materials/manuals_list.html'
    paginate_by = 6