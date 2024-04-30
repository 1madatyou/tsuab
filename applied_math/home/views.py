from django.views.generic.base import TemplateView
from django.db.models import Prefetch

from news.models import News, NewsPicture


class Home(TemplateView):
    template_name = 'home/home.html'

    def get_context_data(self, **kwargs):
        last_news = News.objects.all()[:3]
        context = super().get_context_data(**kwargs)
        context.update({'last_news': last_news})
        return context

