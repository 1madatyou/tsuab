from django.views import generic

from .models import DiplomaThesis


class DiplomaThesesList(generic.ListView):
    """Представление списка дипломных работ"""
    model = DiplomaThesis
    context_object_name = 'theses'
    template_name = 'theses/theses_list.html'
    paginate_by = 6