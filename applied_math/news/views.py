from typing import Any
from django.views.generic import ListView, DetailView

from .models import News


class NewsList(ListView):
    template_name = 'news/news_list.html'
    model = News
    context_object_name = 'news'
    paginate_by = 6

    
class NewsDetail(DetailView):
    model = News
    context_object_name = 'n'