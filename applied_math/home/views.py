from django.views.generic.base import TemplateView

from .models import GalleryPhoto
from news.models import News


class Home(TemplateView):
    template_name = "home/home.html"

    def get_context_data(self, **kwargs):
        last_news = News.objects.all()[:3]
        gallery_photos = GalleryPhoto.objects.filter(is_show=True)
        context = super().get_context_data(**kwargs)
        context.update({"last_news": last_news, "gallery_photos": gallery_photos})
        return context


class History(TemplateView):
    template_name = "home/history.html"
