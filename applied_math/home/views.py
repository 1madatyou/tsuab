from django.views.generic.base import TemplateView
from django.views.generic import FormView

from news.models import News 
from .forms import SupportTicketForm


class Home(TemplateView):
    template_name = 'home/home.html'

    def get_context_data(self, **kwargs):
        last_news = News.objects.all()[:3]
        context = super().get_context_data(**kwargs)
        context.update({'last_news': last_news})
        return context
    

class Support(FormView):
    template_name = 'home/support.html'
    form_class = SupportTicketForm
    





