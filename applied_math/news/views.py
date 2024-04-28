from django.views.generic import TemplateView


class NewsList(TemplateView):
    template_name = 'news/news_list.html'